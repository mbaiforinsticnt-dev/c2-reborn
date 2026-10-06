#!/usr/bin/env python3
"""usage: sync.py TEMPLATE_INDEX_HTML OUT_INDEX_HTML OUT_VIEWER_HTML
Reads pool.json (or 1-pool.json, the name GitHub uploads give it) next to this file. Every embedded picture in the template is
matched to its pool entry by orig_sha1 and replaced with the pool's current image.
Then the icon viewer page is regenerated from the same pool."""
import re,json,base64,hashlib,html,sys,os
here=os.path.dirname(os.path.abspath(__file__))
pf=[f for f in ('pool.json','1-pool.json') if os.path.exists(os.path.join(here,f))][0]
pool=json.load(open(os.path.join(here,pf)))['icons']
by={e['orig_sha1']:e for e in pool}
s=open(sys.argv[1],encoding='utf-8').read()
n=0
def rep(m):
    global n
    h=hashlib.sha1(base64.b64decode(m.group(2))).hexdigest()
    e=by.get(h)
    if not e or e['image']==m.group(2): return m.group(0)
    n+=1
    return 'data:image/%s;base64,%s'%(e['mime'],e['image'])
s=re.sub(r'data:image/(png|gif|jpeg|svg\+xml);base64,([A-Za-z0-9+/=]{40,})',rep,s)
open(sys.argv[2],'w',encoding='utf-8').write(s)
rows=''.join('<tr class="%s"><td>%s</td><td class="pic"><img src="data:image/%s;base64,%s"></td><td>%s</td><td>%s</td></tr>'%(e['origin'],html.escape(e['key']),e['mime'],e['image'],html.escape(e['description']),e['origin']) for e in pool)
c={k:sum(1 for e in pool if e['origin']==k) for k in('firmware','replaced','new')}
open(sys.argv[3],'w',encoding='utf-8').write('<!doctype html><meta charset=utf-8><meta name=robots content=noindex><title>C2 Reborn icon pool</title><style>body{font:14px sans-serif;margin:12px}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:3px 6px}.pic{background:#ddd}img{max-width:120px;max-height:80px;image-rendering:pixelated}.new td:first-child{background:#cfe8ff}.replaced td:first-child{background:#ffe9b0}</style><h2>C2 Reborn icon pool</h2><p>%d icons: %d firmware, %d replaced, %d new. Built from pool.json.</p><table><tr><th>ID<th>Picture<th>Description<th>Origin</tr>%s</table>'%(len(pool),c['firmware'],c['replaced'],c['new'],rows))
print('replaced in html:',n,'pool icons:',len(pool))
