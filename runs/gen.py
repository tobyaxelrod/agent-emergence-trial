import json,os
res=json.load(open('results.json')) if os.path.exists('results.json') else {}
from analyze import PLAN
CN={'AN':'Assigned goal, no process','AV':'Assigned goal, vote','FN':'Free choice, no process','FV':'Free choice, vote'}
PN={'archive':'archive','seed':'seed-bank','radio':'radio'}
runs=[]
for n,cell,cfg in PLAN:
    o=res.get(str(n))
    d=dict(n=n,cell=cell,cellName=CN[cell],cfg=cfg,done=bool(o))
    if o:
        nm=o['names'];e=o['execution'];f=o['formation'];p=o['process'];c=o['concentration']
        proj=', '.join(f"{PN[k]} {v['points']}/9" for k,v in e['projects'].items()) or 'none started'
        d.update(names=o['names'],
          formation=f"joined: {', '.join(f'{nm[a]}→{PN[pj]}' for a,pj in f['joined'].items()) or 'nobody'}. Abstained: {', '.join(nm[a] for a in f['abstentions']) or 'none'}. Membership changes: {f['membership_changes']}. First joint commitment: {'round '+str(f['first_joint_commit_round']) if f['first_joint_commit_round'] else 'never'}. First spend: {'round '+str(f['first_spend_round']) if f['first_spend_round'] else 'none'}.",
          execution=f"{proj}. Completed: {', '.join(PN[x] for x in e['completed']) or 'none'}. Turns used {e['turns_used']}/4. Tokens left {e['tokens_left']}/18.",
          disputes='; '.join(f"{x['about']} -> {x['ending']}" for x in o['disputes']) or 'none',
          concentration=f"{round(c['top_share_of_spent']*100)}% of spent tokens at one agent's direction. Adopted proposals: {', '.join(f'{nm[a]} x{k}' for a,k in c['proposals_adopted_by'].items()) or 'none'}.",
          process=f"{p['messages']}/18 messages, {p['words']} words, {p['proposals']} proposals, {p['votes']} votes.",
          deviations='; '.join(o['deviations']) or 'none',
          votes='; '.join(f"{x['id']} by {nm[x['by']]} r{x['round']}: {x['yes']} yes/{x['no']} no/{x['silent']} silent, {x['result']}" for x in o['proposals']) or '',
          notes=' '.join(o['notes']),
          best=e['best_points'],left=e['tokens_left'],
          log=[f"R{t['rnd']} {nm[t['ag']]} ({t['ag']}): {t['text']}" for t in o['transcript']]+[f"R{a['rnd']} spend: {nm[a['ag']]} puts {a['n']} on {PN[a['proj']]}"+('' if a['by']==a['ag'] else f" (directed by {nm[a['by']]})") for a in o['acts']])
    runs.append(d)
done=sum(1 for r in runs if r['done'])
open('/downloads/emergence/src/data.ts','w').write('export const DONE = %d;\nexport const RUNS: any[] = %s;\n'%(done,json.dumps(runs,ensure_ascii=False)))
print('done',done)
