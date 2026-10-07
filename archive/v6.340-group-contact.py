from pathlib import Path
import hashlib,sys
src=Path(sys.argv[1]);dest=Path(sys.argv[2]);s=src.read_text();assert hashlib.sha256(s.encode()).hexdigest()=='9354502623c56eec225153e3ac9d150fdf1d2f77f50c464c375486202383296c'
p=r'''<script id="groupContact340">
// Highlighted group members share the regular contact Options and green key.
function groupContact340(){return page==='grpview'&&sel>0?gvMembers()[sel-1]:null}
var _gvMenuItems340=gvMenuItems;gvMenuItems=function(kind){let old=_gvMenuItems340.apply(this,arguments),c=groupContact340();if(kind!=='member'||!c)return old;let p=page,ci=contactIndex,o=open,sp=subParent,ps=pageSub,np=namesSubmenu,op=optParent;try{page='contact';contactIndex=phoneState.contacts.indexOf(c);open=false;subParent=null;pageSub=null;namesSubmenu=null;optParent=null;return [...new Set(old.concat(currentOptions()))]}finally{page=p;contactIndex=ci;open=o;subParent=sp;pageSub=ps;namesSubmenu=np;optParent=op}};
var _gvMenuDo340=gvMenuDo;gvMenuDo=function(it,kind){let c=groupContact340();if(kind==='member'&&c&&!['Remove member','Contact details'].includes(it)){contactIndex=phoneState.contacts.indexOf(c);go('contact');open=true;os=currentOptions().indexOf(it);if(os<0){open=false;notice='Contact option unavailable';draw();return}press('OK');return}return _gvMenuDo340.apply(this,arguments)};
var _pressGroupContact340=press;press=function(k){let c=groupContact340();if((k==='CALL'||k==='SEND')&&c&&!gvMenu&&!open&&!notice&&!activeCall&&!rule308Incoming&&!rule308Details&&!transfer309){if(c.number&&c.number!=='(no number)')startCall(c.number);else notifyNoRecipient();return true}return _pressGroupContact340.apply(this,arguments)};
</script>'''
s=s.replace("st.items.map(function(x,i){return '<div class=\"opt'+(i===st.sel?' sel':'')+'\">'+esc(x)+'</div>'}).join('')", "st.items.slice(Math.max(0,Math.min(st.sel-5,st.items.length-7)),Math.max(0,Math.min(st.sel-5,st.items.length-7))+7).map(function(x,i){let first=Math.max(0,Math.min(st.sel-5,st.items.length-7));return '<div class=\"opt'+(i+first===st.sel?' sel':'')+'\">'+esc(x)+'</div>'}).join('')")
s=s.replace('</body>',p+'</body>');dest.write_text(s);print(len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
