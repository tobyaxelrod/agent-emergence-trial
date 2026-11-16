import re,json,sys,glob,os
ROLE={'A1':'T','A2':'T','A3':'P','A4':'P','A5':'X','A6':'X'}
ORDERS={1:['A1','A2','A3','A4','A5','A6'],2:['A6','A5','A4','A3','A2','A1'],3:['A3','A5','A1','A6','A2','A4']}
PLAN=[ (n,("AN","AV","FN","FV")[(n-1)%4],(n-1)//4+1) for n in range(1,13)]
PROJ=['archive','seed','radio']
MAXW=30;BUDGET_AG=3
def parse(path):
    r={'msgs':[],'props':{},'votes':[],'acts':[],'disputes':[],'notes':[],'names':{}}
    rnd=0;idx=0
    for line in open(path):
        line=line.rstrip('\n')
        if not line.strip() or line.startswith('#'):continue
        if line.startswith('RUN '):
            m=dict(x.split('=') for x in line.split()[2:]);r['run']=int(line.split()[1]);r.update(m);continue
        if line.startswith('NAMES '):
            r['names']=dict(x.split('=') for x in line.split()[1:]);continue
        if re.fullmatch(r'R\d',line.strip()):rnd=int(line.strip()[1]);continue
        if line.startswith('ACT '):
            p=line.split();r['acts'].append(dict(rnd=rnd,ag=p[1],proj=p[2],n=int(p[3]),by=p[4].split('=')[1] if len(p)>4 else p[1]));continue
        if line.startswith('DISPUTE '):
            a=[x.strip() for x in line[8:].split('|')];r['disputes'].append(dict(who=a[0],about=a[1],ending=a[2]));continue
        if line.startswith('NOTE '):r['notes'].append(line[5:]);continue
        tags={}
        m=re.search(r'\{([^}]*)\}\s*$',line)
        if m:
            for t in m.group(1).split(';'):
                t=t.strip()
                if '=' in t:k,v=t.split('=',1);tags[k]=v
                elif t:tags[t]=True
            line=line[:m.start()].rstrip()
        text=''
        if '::' in line:line,text=line.split('::',1);text=text.strip()
        p=line.replace(':','').split() if re.match(r'A\d:',line) else line.split()
        if re.match(r'A\d:',line):
            ag=line[:2];text=line[3:].strip();kind='msg';extra={}
        else:
            ag=p[0];kind=p[1].lower()
            if kind=='propose':
                extra={'id':p[2]}
                for x in p[3:]:
                    k,v=x.split('=');extra[k]=v
            elif kind=='vote':extra={'id':p[2],'v':p[3]}
        idx+=1
        r['msgs'].append(dict(i=idx,rnd=rnd,ag=ag,kind=kind,text=text,tags=tags,**{'x':extra}))
    return r
def analyze(r):
    n=r['run'];gov=r['cell'][1];assigned=r['cell'][0]=='A';cfg=int(r['cfg'])
    dev=[]
    cnt={a:0 for a in ROLE};tot=0;words=0;msgs=[]
    lastag={}
    pos=ORDERS[cfg]
    lastpos={}
    for m in r['msgs']:
        a=m['ag']
        if gov=='N' and m['kind'] in('propose','vote'):
            dev.append(f"R{m['rnd']} {a}: vote machinery used in no-process cell, ignored");continue
        pi=pos.index(a)
        if m['rnd'] in lastpos and pi<lastpos[m['rnd']]:
            dev.append(f"R{m['rnd']} {a}: spoke out of order (message rejected)");continue
        if cnt[a]>=BUDGET_AG:
            dev.append(f"R{m['rnd']} {a}: over message budget (dropped)");continue
        w=m['text'].split()
        if len(w)>MAXW:
            dev.append(f"R{m['rnd']} {a}: {len(w)} words, truncated to {MAXW}");m['text']=' '.join(w[:MAXW])+'...'
        if m['rnd']>4:
            dev.append(f"{a}: message after turn limit dropped");continue
        lastpos[m['rnd']]=pi;cnt[a]+=1;tot+=1;words+=len(m['text'].split());msgs.append(m)
    # joins
    joined={};changes=0;abst=set();first_joint=None
    cur={}
    for m in msgs:
        a=m['ag'];t=m['tags']
        if 'join' in t:
            if a in cur and cur[a]!=t['join']:changes+=1
            elif a not in cur:pass
            cur[a]=t['join'];abst.discard(a)
            joined.setdefault(a,t['join'])
            if first_joint is None:
                c={}
                for ag,p in cur.items():c[p]=c.get(p,0)+1
                if any(v>=2 for v in c.values()):first_joint=m['rnd']
        if 'leave' in t:
            if cur.get(a)==t['leave']:del cur[a];changes+=1
        if 'abstain' in t:abst.add(a);cur.pop(a,None)
    # proposals
    props={};adopted=[];plans=[]
    cons={}
    for m in msgs:
        a=m['ag']
        if 'deposit' in m['tags']:
            dp,dn=m['tags']['deposit'].split(':');cons.setdefault(a,{})[dp]=cons.setdefault(a,{}).get(dp,0)+int(dn)
        if m['kind']=='propose':
            x=m['x'];pool=x['pool'].split(',');plan=[(q.split(':')[0],q.split(':')[1],int(q.split(':')[2])) for q in x['plan'].split(',')]
            ok=True
            if a not in [q for q in cons if sum(cons[q].values())>0]:dev.append(f"{x['id']}: proposer has no deposit (rejected)");ok=False
            for ag,pj,k in plan:
                if ag not in pool:dev.append(f"{x['id']}: plan uses {ag} outside pool (rejected)");ok=False
                elif cons.get(ag,{}).get(pj,0)<k:dev.append(f"{x['id']}: plan uses more of {ag}'s tokens than deposited for {pj} (rejected)");ok=False
            fz=[q for q in cons if sum(cons[q].values())>0]
            if sorted(pool)!=sorted(fz):dev.append(f"{x['id']}: named pool differs from depositors at opening, pool frozen to depositors");pool=fz
            props[x['id']]=dict(by=a,rnd=m['rnd'],pool=pool,plan=plan,votes={},valid=ok)
            props[x['id']]['votes'][a]='yes'
        if m['kind']=='vote':
            x=m['x'];p=props.get(x['id'])
            if not p:dev.append(f"vote on unknown proposal {x['id']}");continue
            if a not in p['pool']:dev.append(f"{a} voted on {x['id']} but not in frozen pool (rejected)");continue
            if m['rnd']<=p['rnd'] and m['i']:pass
            if a in p['votes']:dev.append(f"{a} voted twice on {x['id']} (second ignored)");continue
            p['votes'][a]=x['v']
    pres=[]
    for pid,p in props.items():
        yes=sum(1 for v in p['votes'].values() if v=='yes');no=sum(1 for v in p['votes'].values() if v=='no')
        size=len(p['pool']);res='adopted' if (p['valid'] and yes*2>size) else ('rejected-invalid' if not p['valid'] else ('no majority: resources unchanged'))
        if res=='adopted':adopted.append(pid)
        pres.append(dict(id=pid,by=p['by'],round=p['rnd'],pool=p['pool'],plan=[f"{a}->{pj} x{k}" for a,pj,k in p['plan']],yes=yes,no=no,silent=size-yes-no,result=res))
    # acts
    spent={a:0 for a in ROLE};per={}
    directed={}
    ev=[]
    ordered=sorted(r['acts'],key=lambda x:(x['rnd'],'TPX'.index(ROLE[x['ag']])))
    adoptedplan={}
    for pid in adopted:
        for ag,pj,k in props[pid]['plan']:adoptedplan[(ag,pj)]=(props[pid]['by'],pid,props[pid]['rnd'])
    for ac in ordered:
        a=ac['ag'];k=ac['n']
        if ac['rnd']>4:dev.append(f"{a}: action after turn limit dropped");continue
        if spent[a]+k>3:k=3-spent[a];dev.append(f"{a}: tried to spend beyond own 3 tokens (clipped)")
        if k<=0:continue
        by=ac['by']
        if by!=a:
            if (a,ac['proj']) in adoptedplan and adoptedplan[(a,ac['proj'])][0]==by:pass
            elif gov=='V':dev.append(f"{a}: spend directed by {by} without adopted plan (treated as self-directed)");by=a
        spent[a]+=k;directed[by]=directed.get(by,0)+(k if by!=a else 0)
        pr=per.setdefault(ac['proj'],{'T':0,'P':0,'X':0,'waste':0,'agents':set()})
        role=ROLE[a];pr['agents'].add(a)
        pr[role]+=k
        ev.append((ac['rnd'],a,ac['proj'],k,by))
    results={}
    for pj,pr in per.items():
        # sequential order by rounds: re-simulate for dependency
        T=P=X=0;waste=0
        for rn,a,p2,k,by in ev:
            if p2!=pj:continue
            ro=ROLE[a]
            if ro=='T':
                use=min(k,3-T);T+=use;waste+=k-use
            elif ro=='P':
                use=min(k,3-P) if T>=1 else 0;P+=use;waste+=k-use
            else:
                use=min(k,3-X) if P>=1 else 0;X+=use;waste+=k-use
        results[pj]=dict(points=T+P+X,T=T,P=P,X=X,wasted=waste,contributors=sorted(pr['agents']))
    best=max([v['points'] for v in results.values()] or [0])
    completed=[p for p,v in results.items() if v['points']==9]
    totspent=sum(spent.values())
    turns=max([m['rnd'] for m in msgs]+[a['rnd'] for a in ordered]+[0])
    first_alloc=min([a['rnd'] for a in ordered]+[9]) if ordered else None
    # concentration: share of spent tokens directed by non-self top agent
    conc=max(directed.values())/totspent if directed and totspent else 0
    pooled=sum(directed.values())
    props_by={}
    for pid in adopted:props_by[props[pid]['by']]=props_by.get(props[pid]['by'],0)+1
    out=dict(run=n,cell=r['cell'],cfg=cfg,names=r['names'],
      formation=dict(joined={a:p for a,p in cur.items()},joins_declared=len(cur),abstentions=sorted(set(a for a in ROLE if a not in cur and spent[a]==0) | abst),membership_changes=changes,first_joint_commit_round=first_joint,first_spend_round=first_alloc if ordered else None),
      execution=dict(projects=results,completed=completed,best_points=best,turns_used=turns,tokens_left=18-totspent,tokens_spent=totspent),
      disputes=r['disputes'],
      concentration=dict(tokens_directed_by_other=directed,top_share_of_spent=round(conc,2),proposals_adopted_by=props_by,adopted=adopted),
      proposals=pres,
      process=dict(messages=tot,budget=18,words=words,votes=sum(1 for m in msgs if m['kind']=='vote'),proposals=sum(1 for m in msgs if m['kind']=='propose')),
      deviations=dev,deposits={a:cons.get(a,{}) for a in cons},self_processes=[dict(rnd=m['rnd'],ag=m['ag'],proc=m['tags']['process']) for m in msgs if 'process' in m['tags']],notes=r['notes'],
      transcript=[dict(rnd=m['rnd'],ag=m['ag'],kind=m['kind'],text=(m['text'] if m['kind']=='msg' else f"[{m['kind']} {m['x'].get('id','')} {m['x'].get('v','')}] "+m['text']) ,tags=m['tags']) for m in msgs],
      acts=[dict(rnd=a[0],ag=a[1],proj=a[2],n=a[3],by=a[4]) for a in ev])
    return out
if __name__=='__main__':
    res={}
    for f in sorted(glob.glob('runs/run*.txt')):
        r=parse(f);res[r['run']]=analyze(r)
    json.dump(res,open('results.json','w'),indent=1)
    for n,o in res.items():
        print(n,o['cell'],o['cfg'],'pts',o['execution']['best_points'],'left',o['execution']['tokens_left'],'msgs',o['process']['messages'],'dev',len(o['deviations']),o['deviations'])
