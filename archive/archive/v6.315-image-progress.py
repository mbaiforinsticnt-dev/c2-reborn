from pathlib import Path
import hashlib,sys
base=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/tmp/h/w314.html')
assert hashlib.sha256(base.read_bytes()).hexdigest()=='9354502623c56eec225153e3ac9d150fdf1d2f77f50c464c375486202383296c'
s=base.read_text()
def rep(a,b):
 global s
 assert s.count(a)==1,(a[:80],s.count(a));s=s.replace(a,b)
rep("else if(composeFocus===2){if(composeAttachment===3", "else if(composeFocus===2){if(composeAttachment===0){composeImagePick();return}if(composeAttachment===3")
rep("function galTargetOptions(){let t=galTarget,r=galTargetRows()[sel];return", "function galTargetOptions(){let t=galTarget,r=galTargetRows()[sel];if(t.op==='Image')return (r&&!r.folderRow?['Open']:[]).concat(['Details','Type of view ▸','Sort ▸',t.search?'View all':'Search']);return")
rep("function galTargetCancel(){let t=galTarget;galTarget=null;open=false;back();open=true;", "function galTargetCancel(){let t=galTarget;galTarget=null;open=false;back();if(t.op==='Image'||t.op==='ImagePreview'){draw();return}open=true;")
rep("rows=rows.map(f=>({...f,key:f.key||f.id}));if(folder)","if(t.op==='Image')rows=rows.filter(f=>f.folderRow||!!(f.src||f.big));rows=rows.map(f=>({...f,key:f.key||f.id}));if(folder)")
rep("soft('Options',rows.length?(r?.folderRow?(t.op==='Move'?'Move':'Copy to'):'Open'):(t.query?'View all':'Add'),t.query?'Clear':'Back');", "soft(t.op==='Image'&&!rows.length&&!t.search?'':'Options',rows.length?(r?.folderRow?(t.op==='Image'?'Open':t.op==='Move'?'Move':'Copy to'):(t.op==='Image'?'Insert':'Open')):(t.query?'View all':t.op==='Image'?'':'Add'),t.query?'Clear':'Back');")
rep("if(k==='LSK'){open=true;os=0;draw();return}if(k==='UP' ||k==='DOWN'||k==='LEFT'||k==='RIGHT')", "if(k==='LSK'){if(t.op==='Image'&&!rows.length&&!t.search)return;open=true;os=0;draw();return}if(k==='UP' ||k==='DOWN'||k==='LEFT'||k==='RIGHT')")
rep("let c=a[os];if(optionDisabled(c))return;open=false;if(c==='Open drive'", "let c=a[os];if(optionDisabled(c))return;open=false;if(t.op==='Image'&&c==='Open'){t.preview={...r};t.pane='preview';t.previewOpen=false;t.zoom=0;t.full=false;draw();return}if(c==='Open drive'")
rep("if(k==='OK'){if(!r){open=true;os=galTargetOptions().indexOf('Add folder');", "if(k==='OK'){if(t.op==='Image'){if(!r)return;if(r.folderRow){t.trail.push({browse:t.browse||'',sel});t.browse=r.key;sel=0;draw();return}composeImageInsert(r);return}if(!r){open=true;os=galTargetOptions().indexOf('Add folder');")
rep("if(['RSK','BACK','END'].includes(k)){t.pane=t.previewDetails?'preview':null;","if(['RSK','BACK','END'].includes(k)){if(t.op==='Image'&&t.pane==='unsupported'){galTargetCancel();return}t.pane=t.previewDetails?'preview':null;")
rep("if(t.pane){let a=galTargetMenuRows();if(k===","if(t.op==='Image'&&t.pane==='unsupported'){if(['RSK','BACK','END'].includes(k))galTargetCancel();return}if(t.pane){let a=galTargetMenuRows();if(k===")
rep("t.pane=null;t.zoom=0;if(t.search)sel=0", "if(t.op==='ImagePreview'){galTargetCancel();return}t.pane=null;t.zoom=0;if(t.search)sel=0")
rep("function storeDraft(){let t=draft.trim();if(!t)return false;", "function storeDraft(){let t=draft.trim();if(!t&&!composeObjs.length)return false;")
rep("o.kind=mmsMode?'mms':'sms';o.subject=composeSubject||''", "o.kind=mmsMode?'mms':'sms';o.subject=composeSubject||'';o.objects=JSON.parse(JSON.stringify(composeObjs))")
s=s.replace("body:draft,subject:composeSubject||''}","body:draft,subject:composeSubject||'',objects:JSON.parse(JSON.stringify(composeObjs))}")
rep("else if(draftOpenDemo>=0){draftDemo[draftOpenDemo].body=draft;","else if(draftOpenDemo>=0&&composeObjs.some(o=>o.kind==='image')){phoneState.drafts.unshift({kind:'mms',to:recipientText,body:draft,subject:composeSubject||'',objects:JSON.parse(JSON.stringify(composeObjs))});phoneState.drafts=phoneState.drafts.slice(0,20)}else if(draftOpenDemo>=0){draftDemo[draftOpenDemo].body=draft;")
rep("draftDemo[draftOpenDemo].subject=composeSubject||''", "draftDemo[draftOpenDemo].subject=composeSubject||'';draftDemo[draftOpenDemo].objects=JSON.parse(JSON.stringify(composeObjs))")
rep("subject:o.subject||'',user:true", "subject:o.subject||'',objects:o.objects||[],user:true")
rep("subject:d.subject||'',user:false", "subject:d.subject||'',objects:d.objects||[],user:false")
rep("composeOrigin='draft';mmsMode=x.kind==='mms';", "composeOrigin='draft';composeObjs=JSON.parse(JSON.stringify(x.objects||[]));attView=0;rmObjPrompt=false;mmsMode=x.kind==='mms';")
rep("cancelTap();if(!recipientText&&!draft){back()}","cancelTap();if(!recipientText&&!draft&&!composeObjs.length){back()}")
rep("if(draft.trim()){composeExitConfirm=true;draw()}","if(draft.trim()||composeObjs.length){composeExitConfirm=true;draw()}")
rep("if(page==='compose'&&draft.trim()){composeExitConfirm=true;", "if(page==='compose'&&(draft.trim()||composeObjs.length)){composeExitConfirm=true;")
rep("function migrateState(raw){","function cleanComposeObjects315(a){return Array.isArray(a)?a.filter(o=>o&&o.kind==='image'&&typeof o.src==='string'&&/^data:image\\//.test(o.src)).slice(0,1).map(o=>({kind:'image',name:cleanText(o.name,200),size:cleanText(o.size,80),src:o.src,key:cleanText(o.key,200)})):[]}function migrateState(raw){")
rep("subject:cleanText(v.subject,200)}:cleanText","subject:cleanText(v.subject,200),objects:cleanComposeObjects315(v.objects)}:cleanText")
# image UI is scoped to actual inserted images, not business cards
rep("+'<label>Text:</label><div class=\"textField ","+composeImageRow()+'<label>Text:</label><div class=\"textField ")
rep("(mmsMode?'New multimedia <span", "(mmsMode?(composeOrigin==='draft'?'Multimedia':'New multimedia')+' <span")
# known general remove behavior retained, scoped image submenu handled by wrapper
extra=r'''
<script id="imageInsert315">
function composeImage(){return composeObjs.find(o=>o.kind==='image')}
function composeImageRow(){let o=composeImage();return o?'<label>Image:</label><div class="composeImageField '+(composeFocus===3?'focus':'')+'"><img src="'+STRIP_IC.image+'" alt=""><div>'+esc(o.name)+'</div></div>':''}
function composeImagePick(){galTarget={op:'Image',browse:'',trail:[],pane:composeObjs.length?'unsupported':null,unsupportedTitle:'Image'};go('galfoldertarget')}
function composeImageInsert(r){let changed=!mmsMode;composeObjs.push({kind:'image',name:r.n,size:r.s||'',src:r.big||r.src,key:r.key});galTarget=null;open=false;back();mmsMode=true;composeFocus=3;if(changed)notice='Message changed to multimedia';draw()}
function composeImagePreview(){let o=composeImage();if(!o)return;galTarget={op:'ImagePreview',browse:'',trail:[],pane:'preview',preview:{n:o.name,s:o.size,src:o.src},zoom:0,full:false};go('galfoldertarget')}
var _drawImage315=draw;draw=function(){_drawImage315.apply(this,arguments);if(page==='compose'&&composeImage()&&!notice&&!open&&!pageSub&&!composeExitConfirm&&!rmObjPrompt&&!attView){soft('Options',composeFocus===2?'Insert':composeFocus===0?(recipientText?'Send':'Add'):'Send',composeFocus===0?(recipientText?'Clear':'Back'):composeFocus===1&&draft?'Clear':'Close')}};
var _rowsImage315=pageSubRows;pageSubRows=function(){if(pageSub==='imageRemove')return [{t:'Image',dis:false}];return _rowsImage315.apply(this,arguments)};
var _sendImage315=sendDraft;sendDraft=function(){if(composeImage()){go('imageUnsupported');return}return _sendImage315.apply(this,arguments)};
var _pressImage315=press;press=function(k){
 if(page==='imageUnsupported'){if(['RSK','BACK','END'].includes(k))back();return}
 if(page==='compose'&&composeImage()){
  if(composeExitConfirm){if(k==='RSK'||k==='BACK'){composeExitConfirm=false;draw();return}if(k==='LSK'){draft='';recipientText='';composeObjs=[];mmsMode=false;composeExitConfirm=false;history=[];page='messaging';sel=0;draw();return}if(k==='OK'){if(!storeDraft())return;draft='';recipientText='';composeObjs=[];mmsMode=false;composeExitConfirm=false;history=[];page='messaging';sel=0;notice='Message saved to<br>Drafts';draw();return}return}
  if(pageSub==='imageRemove'&&(k==='OK'||k==='LSK')){pageSub=null;optParent=null;open=false;rmObjPrompt=true;draw();return}
  if(open&&!pageSub&&!notice&&!rmObjPrompt){let c=currentOptions()[os];if(k==='OK'&&c==='Preview'){open=false;go('imageUnsupported');return}if(k==='OK'&&(c==='Remove'||c==='Remove >')){pageSub='imageRemove';ps2=0;optParent={list:currentOptions().slice(),os};open=false;draw();return}if(k==='OK'&&(c==='Exit editor'||c==='Cancel')){open=false;composeExitConfirm=true;draw();return}if(k==='OK'&&c==='As draft message'){if(!storeDraft())return;subParent=null;open=false;draft='';recipientText='';composeObjs=[];mmsMode=false;composeExitConfirm=false;history=[];page='messaging';sel=0;notice='Message saved to<br>Drafts';draw();return}if(k==='OK'&&(c==='Change to text msg.'||c==='As template'||c==='To folder')){subParent=null;open=false;go('imageUnsupported');return}}
  if(!open&&!pageSub&&!notice&&!rmObjPrompt&&!attView&&!subjectEditor){if(k==='DOWN'&&composeFocus===0){composeFocus=3;draw();return}if(k==='UP'&&composeFocus===1){composeFocus=3;draw();return}if(composeFocus===3){if(k==='DOWN'||k==='UP'){composeFocus=k==='DOWN'?1:0;draw();return}if(k==='OK'){sendDraft();return}if(['LEFT','RIGHT'].includes(k))return}if((k==='RSK'||k==='END'||k==='BACK')&&composeFocus!==0&&!(composeFocus===1&&draft)){composeExitConfirm=true;draw();return}}
 }
 return _pressImage315.apply(this,arguments)
};
var _drawUnsupported315=draw;draw=function(){_drawUnsupported315.apply(this,arguments);if(page==='imageUnsupported'){document.getElementById('screen').innerHTML='<div class="title">Multimedia</div><div class="emptyNote">Not implemented in this prototype</div>';soft('','','Back')}if(page==='compose'&&composeImage()&&composeExitConfirm){soft('No','Yes','Back')}};
</script>
<style>.composeImageField{min-height:65px;text-align:center;background:linear-gradient(#ddd,#aaa);color:#111;border:1px solid #888;border-radius:3px;padding:4px;box-sizing:border-box}.composeImageField img{height:32px;width:32px;object-fit:contain}.composeImageField div{line-height:18px;font-size:16px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.composeImageField.focus{background:linear-gradient(#555,#111);color:white;outline:1px solid white}.smsEditor:has(.composeImageField) .textField{min-height:18px;height:18px;box-sizing:border-box;padding:2px}.smsEditor:has(.composeImageField) .recipientField{min-height:18px;padding:2px}.smsEditor:has(.composeImageField){overflow-y:auto;max-height:calc(100% - 30px);padding:4px}.smsEditor:has(.composeImageField) label{height:18px;line-height:18px;margin-top:2px}.smsEditor:has(.composeImageField) .composeImageField{height:65px;min-height:65px}.smsEditor:has(.composeImageField) .composeImageField img{height:32px;width:32px}.smsEditor:has(.composeImageField) .recipientField{height:26px;box-sizing:border-box}</style>
'''
rep('</body>',extra+'</body>')
s=s.replace('v6.314','v6.315')
dest=Path(sys.argv[2]) if len(sys.argv)>2 else Path('/tmp/h/w315.html')
assert hashlib.sha256(s.encode()).hexdigest()=='5b4ccdb24ec686d7eb6caa9066d2e9c68cd7e782bf7d0d4676e8a2bcfc2edadb'
dest.write_text(s)
print(len(s.encode()))

# WORK IN PROGRESS, NOT A RELEASE.
# Base v6.314 rollback blob: 27216037c33ea273d94429e36526d84ac757840f
# Candidate blob: 71f4b27bb3eb28e7a6e8d93a4640ef6258b0bfad
# Image test results, 7 Oct 2026, 11:07 London:
# PASS Image centre opens picker
# PASS picker root no destructive options
# PASS folder Back preserves root
# PASS root Back restores composer content and strip
# PASS Images files actual data
# PASS file centre Insert
# PASS file options grounded set
# PASS Open previews without insertion
# PASS Details pane
# PASS insertion converts mms
# PASS Image row drawn
# PASS strip fits editor viewport
# PASS image to Text Down
# PASS image to To Up
# PASS repeat insertion honestly unsupported
# PASS image-only Close prompts
# PASS Close Back cancels without loss
# PASS image-only saved as draft
# PASS draft reopen restores image
# PASS draft reload restores image
# PASS image send not fake text delivery
# PASS unsupported Back restores image
# PASS Remove submenu Image
# PASS Remove confirm
# PASS Remove No preserves
# PASS Remove Yes converts text
# PASS business card preserved
# PASS empty folder Back only
# PASS empty Insert Options inert
# PASS failed draft save retains image and composer
# PASS failed draft save rolls back collection
# PASS draft update no duplicate
# PASS image name escaped
# PASS Close No discards current image cleanly
# PASS unsupported second insert has no active keys
# PASS unsupported repeat Back returns composer
# PASS folder save honestly unsupported
# PASS Options save image-only works
# PASS edited built-in draft image survives reload as user draft
# PASS business-card image mixing guarded
# TOTAL 40
# Existing regression groups: 85 checks pass; 409-line draw sweep eef82c85, no errors.
# Not done: MMS slides, MMS Preview/send, full Options Insert routes, visual parity and complete differential coverage.
# Demo fixture only. No handset footage, private PDFs, real contacts or user media included.
# Root index.html remains v6.314. Recipe is bank-only progress.

# Recovery helpers for local demo testing. No network writes.
Path(str(dest)+".test.py").write_text('import sys,json,time\nsys.argv=[\'p\',\'/tmp/h/w315.html\'];exec(open(\'/tmp/c2hdr.py\').read());fresh2();R=[]\ndef ck(n,e):\n v=ev(e);assert v is True,(n,v);R.append(n)\ndef E(s):return ev(s)\nE("notice=\'\';startMessage(\'Demo text\');recipientText=\'+447700900456;\';composeFocus=2;composeAttachment=0;press(\'OK\')")\nck(\'Image centre opens picker\',"page===\'galfoldertarget\'&&galTarget.op===\'Image\'")\nck(\'picker root no destructive options\',"!currentOptions().some(x=>/Delete|Move|Copy|Rename|Add folder/.test(x))")\nE("press(\'OK\');press(\'RSK\')");ck(\'folder Back preserves root\',"page===\'galfoldertarget\'&&galTarget.browse===\'\'")\nE("press(\'RSK\')");ck(\'root Back restores composer content and strip\',"page===\'compose\'&&draft===\'Demo text\'&&recipientText===\'+447700900456;\'&&composeFocus===2&&composeObjs.length===0&&!open")\nE("press(\'OK\');press(\'DOWN\');press(\'OK\')");ck(\'Images files actual data\',"galTargetRows().length===galActualFiles(\'Images\').length&&galTargetRows().every(r=>!!r.src)")\nck(\'file centre Insert\',"document.getElementById(\'sm\').innerText===\'Insert\'")\nE("press(\'LSK\')");ck(\'file options grounded set\',"JSON.stringify(currentOptions())===JSON.stringify([\'Open\',\'Details\',\'Type of view ▸\',\'Sort ▸\',\'Search\'])")\nE("press(\'OK\')");ck(\'Open previews without insertion\',"galTarget.pane===\'preview\'&&composeObjs.length===0")\nE("press(\'RSK\');press(\'LSK\');press(\'DOWN\');press(\'OK\')");ck(\'Details pane\',"galTarget.pane===\'details\'")\nE("press(\'RSK\');press(\'OK\')");ck(\'insertion converts mms\',"page===\'compose\'&&composeImage().name===\'Photo0001.jpg\'&&mmsMode&&notice===\'Message changed to multimedia\'")\nE("notice=\'\';draw()");lcdshot(\'/downloads/html-image315c.png\');ck(\'Image row drawn\',"!!document.querySelector(\'.composeImageField\')&&document.getElementById(\'sm\').innerText===\'Send\'")\nck(\'strip fits editor viewport\',"document.querySelector(\'.attachStrip\').offsetTop+document.querySelector(\'.attachStrip\').offsetHeight<=document.getElementById(\'screen\').clientHeight")\nE("press(\'DOWN\')");ck(\'image to Text Down\',"composeFocus===1");E("press(\'UP\');press(\'UP\')");ck(\'image to To Up\',"composeFocus===0")\nE("composeFocus=2;press(\'OK\')");ck(\'repeat insertion honestly unsupported\',"galTarget.pane===\'unsupported\'&&composeObjs.length===1")\nE("press(\'RSK\');draft=\'\';recipientText=\'\';composeFocus=3;press(\'RSK\')");ck(\'image-only Close prompts\',"composeExitConfirm")\nE("press(\'RSK\')");ck(\'Close Back cancels without loss\',"!composeExitConfirm&&composeObjs.length===1")\nE("press(\'RSK\');press(\'OK\')");ck(\'image-only saved as draft\',"page===\'messaging\'&&phoneState.drafts[0].objects[0].name===\'Photo0001.jpg\'&&phoneState.drafts[0].body===\'\'")\nE("notice=\'\';page=\'drafts\';sel=0;press(\'OK\')");ck(\'draft reopen restores image\',"composeImage().name===\'Photo0001.jpg\'&&mmsMode&&composeOrigin===\'draft\'")\nE("persist()");call(\'Page.reload\');time.sleep(.5);E("notice=\'\';page=\'drafts\';sel=0;press(\'OK\')");ck(\'draft reload restores image\',"composeImage().name===\'Photo0001.jpg\'")\nE("composeFocus=3;press(\'OK\')");ck(\'image send not fake text delivery\',"page===\'imageUnsupported\'");E("press(\'RSK\')");ck(\'unsupported Back restores image\',"page===\'compose\'&&!!composeImage()")\nE("open=true;os=currentOptions().indexOf(\'Remove >\');if(os<0)os=currentOptions().indexOf(\'Remove\');press(\'OK\')");ck(\'Remove submenu Image\',"pageSub===\'imageRemove\'&&pageSubRows()[0].t===\'Image\'")\nE("press(\'OK\')");ck(\'Remove confirm\',"rmObjPrompt");E("press(\'RSK\')");ck(\'Remove No preserves\',"!!composeImage()");E("rmObjPrompt=true;press(\'OK\')");ck(\'Remove Yes converts text\',"!composeObjs.length&&!mmsMode&&notice===\'Message changed to text message\'")\nE("notice=\'\';startMessage();composeFocus=2;composeAttachment=3;press(\'OK\')");ck(\'business card preserved\',"composeObjs[0].kind===\'bcard\'")\nE("notice=\'\';startMessage();composeFocus=2;composeAttachment=0;press(\'OK\');galTarget.browse=\'Recordings\';sel=0;draw()");ck(\'empty folder Back only\',"!galTargetRows().length&&document.getElementById(\'sl\').innerText===\'\'&&document.getElementById(\'sm\').innerText===\'\'&&document.getElementById(\'sr\').innerText===\'Back\'")\nE("press(\'LSK\');press(\'OK\')");ck(\'empty Insert Options inert\',"!open&&!galTarget.pane");E("press(\'RSK\')")\nE("press(\'RSK\');notice=\'\';startMessage();composeFocus=2;composeAttachment=0;press(\'OK\');press(\'DOWN\');press(\'OK\');press(\'OK\');notice=\'\';draft=\'Before\';recipientText=\'\';composeFocus=3;press(\'RSK\');window.realPersist315=persist;persist=()=>{throw Error(\'test storage failure\')};window.before315=JSON.stringify(phoneState.drafts);press(\'OK\')")\nck(\'failed draft save retains image and composer\',"page===\'compose\'&&composeExitConfirm&&composeImage().name===\'Photo0001.jpg\'&&draft===\'Before\'&&notice===\'Unable to save draft\'")\nck(\'failed draft save rolls back collection\',"JSON.stringify(phoneState.drafts)===before315")\nE("persist=realPersist315;notice=\'\';press(\'OK\');notice=\'\';page=\'drafts\';sel=0;press(\'OK\');draft=\'Updated\';composeFocus=3;press(\'RSK\');press(\'OK\')")\nck(\'draft update no duplicate\',"phoneState.drafts.length===JSON.parse(before315).length+1&&phoneState.drafts[0].body===\'Updated\'&&phoneState.drafts[0].objects.length===1")\nE("notice=\'\';page=\'drafts\';sel=0;press(\'OK\');composeImage().name=\'<img src=x onerror=evil>\';draw()")\nck(\'image name escaped\',"document.querySelector(\'.composeImageField\').innerText.includes(\'<img src=x onerror=evil>\')&&document.querySelectorAll(\'.composeImageField img\').length===1")\nE("composeFocus=3;press(\'RSK\');press(\'LSK\')")\nck(\'Close No discards current image cleanly\',"page===\'messaging\'&&composeObjs.length===0&&!mmsMode")\nE("notice=\'\';startMessage();composeFocus=2;composeAttachment=0;press(\'OK\');press(\'DOWN\');press(\'OK\');press(\'OK\');notice=\'\';composeFocus=2;press(\'OK\');press(\'OK\');press(\'LSK\');press(\'DOWN\')")\nck(\'unsupported second insert has no active keys\',"galTarget.pane===\'unsupported\'&&composeObjs.length===1&&!open")\nE("press(\'RSK\')")\nck(\'unsupported repeat Back returns composer\',"page===\'compose\'&&!galTarget&&composeObjs.length===1")\nE("press(\'LSK\');os=currentOptions().indexOf(\'Save message ▸\');press(\'OK\');os=1;press(\'OK\')")\nck(\'folder save honestly unsupported\',"page===\'imageUnsupported\'&&composeObjs.length===1")\nE("press(\'RSK\');press(\'LSK\');os=currentOptions().indexOf(\'Save message ▸\');press(\'OK\');os=0;press(\'OK\')")\nck(\'Options save image-only works\',"page===\'messaging\'&&!composeObjs.length&&phoneState.drafts[0].objects.length===1")\nE("notice=\'\';page=\'drafts\';sel=phoneState.drafts.length;press(\'OK\');draft=\'Demo edit\';composeFocus=2;composeAttachment=0;press(\'OK\');press(\'DOWN\');press(\'OK\');press(\'OK\');notice=\'\';composeFocus=3;press(\'RSK\');press(\'OK\');persist()")\ncall(\'Page.reload\');time.sleep(.5)\nck(\'edited built-in draft image survives reload as user draft\',"phoneState.drafts[0].body===\'Demo edit\'&&phoneState.drafts[0].objects[0].kind===\'image\'")\nE("notice=\'\';startMessage();composeFocus=2;composeAttachment=3;press(\'OK\');notice=\'\';composeAttachment=0;press(\'OK\')")\nck(\'business-card image mixing guarded\',"galTarget.pane===\'unsupported\'&&composeObjs.length===1&&composeObjs[0].kind===\'bcard\'")\nprint(\'\\n\'.join(\'PASS \'+r for r in R));print(\'TOTAL\',len(R));open(\'/tmp/test315.txt\',\'w\').write(\'\\n\'.join(\'PASS \'+r for r in R)+\'\\nTOTAL \'+str(len(R)))\n')
Path(str(dest)+".cdp.py").write_text('import sys,json,time,subprocess,urllib.request,websocket,base64\nF=sys.argv[1] if len(sys.argv)>1 else \'/tmp/c2-v6201-live.html\'\nif not F.startswith(\'/\'):F=\'/tmp/\'+F\ndef _tab():\n    for _ in range(20):\n        try:\n            t=json.load(urllib.request.urlopen(\'http://localhost:9223/json\'))\n            p=[x for x in t if x[\'type\']==\'page\']\n            if p:return p[0][\'webSocketDebuggerUrl\']\n        except Exception:time.sleep(.5)\n    raise SystemExit(\'no chrome\')\n_ws=websocket.create_connection(_tab(),max_size=None)\n_id=[0]\ndef call(m,p=None):\n    _id[0]+=1;_ws.send(json.dumps({\'id\':_id[0],\'method\':m,\'params\':p or {}}))\n    while True:\n        r=json.loads(_ws.recv())\n        if r.get(\'id\')==_id[0]:return r\ndef ev(js):\n    r=call(\'Runtime.evaluate\',{\'expression\':js,\'returnByValue\':True,\'awaitPromise\':True})\n    r=r.get(\'result\',{})\n    if \'exceptionDetails\' in r:return str(r[\'exceptionDetails\'])[:300]\n    return r.get(\'result\',{}).get(\'value\')\ndef fresh2():\n    call(\'Page.enable\');call(\'Emulation.setDeviceMetricsOverride\',{\'width\':420,\'height\':900,\'deviceScaleFactor\':1,\'mobile\':False})\n    call(\'Page.navigate\',{\'url\':\'file://\'+F});time.sleep(1.2)\n    ev("localStorage.clear()");call(\'Page.navigate\',{\'url\':\'file://\'+F});time.sleep(1.5)\n    for _ in range(30):\n        if ev("typeof press===\'function\'&&typeof phoneState!==\'undefined\'")is True:break\n        time.sleep(.3)\n    ev("try{history_clear&&0}catch(e){}")\ndef safe(k):\n    return ev("(()=>{try{press(%s);return \'ok\'}catch(e){return \'ERR \'+e.message}})()"%json.dumps(k))\ndef S(*ks):\n    for k in ks:safe(k)\nT="document.querySelector(\'.lcd\').innerText.replace(/\\\\n/g,\'|\')"\ndef shot(path):\n    r=call(\'Page.captureScreenshot\',{\'format\':\'png\'});open(path,\'wb\').write(base64.b64decode(r[\'result\'][\'data\']))\ndef lcdshot(path):\n    r=json.loads(ev("(()=>{let b=document.querySelector(\'.lcd\').getBoundingClientRect();return JSON.stringify([b.x,b.y,b.width,b.height])})()"))\n    s=call(\'Page.captureScreenshot\',{\'format\':\'png\',\'clip\':{\'x\':r[0],\'y\':r[1],\'width\':r[2],\'height\':r[3],\'scale\':2}});open(path,\'wb\').write(base64.b64decode(s[\'result\'][\'data\']))\n')
