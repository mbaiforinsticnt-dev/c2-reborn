const controller=document.querySelector('.controller');
const trace=document.querySelector('#keyTrace');
let heldButton=null,heldAt=0;
function sendKey(key,button){
 document.dispatchEvent(new CustomEvent('c2-key',{detail:{key,source:'hardware-controller'}}));
 trace.value=`${key}`;
 button?.classList.add('active');
 setTimeout(()=>button?.classList.remove('active'),120);
}
controller.addEventListener('pointerdown',event=>{
 const button=event.target.closest('button[data-key]');
 if(!button)return;
 event.preventDefault();
 button.setPointerCapture?.(event.pointerId);
 heldButton=button;heldAt=performance.now();button.classList.add('active');
});
function releaseKey(event){
 const button=event.target.closest('button[data-key]')||heldButton;
 if(!button||button!==heldButton)return;
 event.preventDefault();
 const duration=performance.now()-heldAt,key=(duration>=650?'Long':'')+button.dataset.key;
 heldButton=null;heldAt=0;button.classList.remove('active');sendKey(key,button);
}
controller.addEventListener('pointerup',releaseKey);
controller.addEventListener('pointercancel',()=>{heldButton?.classList.remove('active');heldButton=null;heldAt=0});
