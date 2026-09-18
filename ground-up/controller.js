const controller=document.querySelector('.controller');
const trace=document.querySelector('#keyTrace');
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
 sendKey(button.dataset.key,button);
});
