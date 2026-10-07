from pathlib import Path
s=Path('/tmp/h/w314.html').read_text()
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
function composeImagePick(){galTarget={op:'Image',browse:'',trail:[],pane:composeImage()?'unsupported':null,unsupportedTitle:'Image'};go('galfoldertarget')}
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
Path('/tmp/h/w315.html').write_text(s)
print(len(s.encode()))
