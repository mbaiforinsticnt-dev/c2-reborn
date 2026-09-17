const menu=[
['Organiser','OrganizerMenu','assets/icons/organiser.png'],['Contacts','MainPB','assets/icons/contacts.png'],['E-mail','nlink:8','assets/icons/email.png'],['Browser','BrowserMenu','assets/icons/browser.png'],['Messaging','MessagesMenu','assets/icons/messaging.png'],['Gallery','ContentBaseMenu','assets/icons/gallery.png'],['Store','nlink:2','assets/icons/store.png'],['Media','MediaMenu','assets/icons/media.png'],['Applications','ApplicationsMenu','assets/icons/applications.png'],['Settings','SettingsMenu','assets/icons/settings.png'],['Log','CallListsMenu','assets/icons/log.png']
];
const shallow={Organiser:'Alarm clock · Calendar · Maps · To-do list · Notes · Calculator · Countdown timer · Stopwatch · Dictionary','Contacts':'Names · Add new · Groups · Speed dials','E-mail':'Original firmware application entry',Browser:'Nokia / Ovi browser entry',Messaging:'Create message · Inbox / Conversations · Drafts · Sent · Settings',Gallery:'Physical media chooser pending capture',Store:'Original Ovi Store application entry',Media:'Camera · Video · Player · Radio · Voice recorder · Equaliser',Applications:'Games · Collection · Downloads · Settings',Settings:'Profiles · Themes · Tones · Display · Time · Connectivity',Log:'All calls · Missed · Received · Dialled · Timers'};
let selected=0,view='menu',optionsOpen=false,optionSel=0;
function draw(){optionsBox.classList.toggle('hidden',!optionsOpen);if(optionsOpen){let a=view==='viewDialog'?['◯ Single','◯ List','◯ Grid','◉ Grid with labels']:['Main menu view ›','Organise'];optionsBox.innerHTML='<div class="optionsBody">'+a.map((x,i)=>`<div class="option ${i===optionSel?'selected':''}">${x}</div>`).join('')+'</div><div class="dialogSoft"><span>Select</span><span>Back</span></div>'};if(view==='menu'||view==='viewDialog'){let start=Math.floor(selected/9)*9;grid.innerHTML=menu.slice(start,start+9).map((x,j)=>`<div class="cell ${start+j===selected?'selected':''}" data-contract="${x[1]}"><img src="${x[2]}" alt=""><span>${x[0]}</span></div>`).join('');grid.parentElement.classList.remove('hidden');appscreen.classList.add('hidden');screenTitle.textContent='Menu';count.textContent='';leftSoft.textContent='Options';centerSoft.textContent='Select';rightSoft.textContent='Exit'}else{grid.parentElement.classList.add('hidden');appscreen.classList.remove('hidden');let x=menu[selected];screenTitle.textContent=x[0];count.textContent='';appTitle.textContent=x[0];appText.textContent=shallow[x[0]]+' · Route contract: '+x[1];leftSoft.textContent='Options';centerSoft.textContent='Open';rightSoft.textContent='Back'}}
function move(key){if(optionsOpen){let n=view==='viewDialog'?4:2;if(key==='ArrowUp')optionSel=(optionSel+n-1)%n;if(key==='ArrowDown')optionSel=(optionSel+1)%n;draw();return}if(view!=='menu')return;let pageStart=Math.floor(selected/9)*9,pageEnd=Math.min(menu.length-1,pageStart+8),col=(selected-pageStart)%3,row=Math.floor((selected-pageStart)/3);if(pageStart===9){if(key==='ArrowLeft')selected=Math.max(9,selected-1);if(key==='ArrowRight')selected=Math.min(10,selected+1);if(key==='ArrowUp'||key==='ArrowDown')selected=Math.min(pageEnd,pageStart+col);draw();return}if(key==='ArrowRight')selected=row*3+(col+1)%3;if(key==='ArrowLeft')selected=row*3+(col+2)%3;if(key==='ArrowDown')selected=((row+1)%3)*3+col;if(key==='ArrowUp')selected=((row+2)%3)*3+col;draw()}
function activate(){if(optionsOpen){if(view==='viewDialog'){if(optionSel===3){optionsOpen=false;view='menu';draw()}else{let chosen=['Single','List','Grid'][optionSel];optionsOpen=false;view='app';draw();screenTitle.textContent='Main menu view';appTitle.textContent=chosen;appText.textContent=chosen+' view is evidenced as an option; rendering that layout is pending.'}return}if(optionSel===0){view='viewDialog';optionSel=3;draw()}else{optionsOpen=false;view='app';draw();screenTitle.textContent='Organise';appTitle.textContent='Organise';appText.textContent='Menu reorder mode waits for physical key-by-key evidence.'}return}if(view==='menu'){view='app';draw();let c=document.querySelector('.cell.selected');c?.classList.add('pressed');setTimeout(()=>c?.classList.remove('pressed'),120)}else{appText.textContent=shallow[menu[selected][0]]+' · Deeper behavior waits for route evidence.'}}
function back(){if(optionsOpen&&view==='viewDialog'){view='menu';optionSel=0;draw();return}if(optionsOpen){optionsOpen=false;draw();return}if(view==='app'){view='menu';draw()}}function openOptions(){if(view==='menu'){optionsOpen=true;optionSel=0;draw()}else{appText.textContent+=' · Options behavior pending direct evidence.'}}
let responseSequence=0;
function showKeyResponse(key,response){
 responseSequence+=1;
 keyFeedback.textContent=`TEST ${responseSequence} · ${key}: ${response}`;
 keyFeedback.classList.remove('pulse');
 void keyFeedback.offsetWidth;
 keyFeedback.classList.add('pulse');
 setTimeout(()=>keyFeedback.classList.remove('pulse'),140);
}
function handleHardwareKey(key){
 let response='';
 if(key.startsWith('Arrow')){
  if(optionsOpen){move(key);response=(key==='ArrowUp'||key==='ArrowDown')?'moved option selection':'no horizontal option route evidenced'}
  else if(view==='menu'){move(key);response=`selected ${menu[selected][0]}`}
  else response='no directional route evidenced on this shallow screen';
 }
 else if(key==='Enter'||key==='SoftCenter'){
  if(optionsOpen){activate();response=view==='viewDialog'?'opened Main menu view choices':optionsOpen?'selected option':'confirmed selection'}
  else if(view==='menu'){let label=menu[selected][0];activate();response=`opened ${label}`}
  else {activate();response='deeper route is not yet evidenced'};
 }
 else if(key==='SoftLeft'){
  if(view==='menu'){openOptions();response='opened Options'}
  else {openOptions();response='Options route pending direct evidence on this screen'};
 }
 else if(key==='SoftRight'||key==='Escape'){
  if(optionsOpen&&view==='viewDialog'){back();response='returned to Options'}
  else if(optionsOpen){back();response='closed Options'}
  else if(view==='app'){back();response='returned to Menu'}
  else response='Exit route is not implemented in this browser test';
 }
 else if(key==='End'){optionsOpen=false;view='menu';draw();response='returned to Menu (test scaffold)'}
 else if(key==='Call'){selected=10;view='app';draw();response='opened Log (test scaffold)'}
 else if(/^[1-9]$/.test(key)){
  if(view==='menu'&&!optionsOpen){selected=Math.min(menu.length-1,Number(key)-1);draw();response=`selected ${menu[selected][0]} (test shortcut)`}
  else response='numeric action not evidenced in this state';
 }
 else if(key==='0'){
  if(view==='menu'&&!optionsOpen){selected=9;draw();response='selected Settings (test shortcut)'}
  else response='numeric action not evidenced in this state';
 }
 else if(key==='Star'){
  if(view==='menu'&&!optionsOpen){selected=Math.max(0,selected-9);draw();response=`selected ${menu[selected][0]} (test page shortcut)`}
  else response='star action not evidenced in this state';
 }
 else if(key==='Hash'){
  if(view==='menu'&&!optionsOpen){selected=Math.min(menu.length-1,selected+9);draw();response=`selected ${menu[selected][0]} (test page shortcut)`}
  else response='hash action not evidenced in this state';
 }
 else response='key route not yet evidenced';
 showKeyResponse(key,response);
}
document.addEventListener('c2-key',e=>handleHardwareKey(e.detail.key));
addEventListener('keydown',e=>{let k=e.key;if(k==='*')k='Star';if(k==='#')k='Hash';if(k.startsWith('Arrow')||k==='Enter'||k==='Escape'||/^[0-9]$/.test(k)||k==='Star'||k==='Hash'){e.preventDefault();handleHardwareKey(k)}});
// The blue software softkey bar remains tappable, while the separate hardware module sends the same key events.
leftSoft.addEventListener('pointerdown',e=>{e.preventDefault();handleHardwareKey('SoftLeft')});
rightSoft.addEventListener('pointerdown',e=>{e.preventDefault();handleHardwareKey('SoftRight')});
centerSoft.addEventListener('pointerdown',e=>{e.preventDefault();handleHardwareKey('Enter')});
optionsBox.addEventListener('pointerdown',e=>{let bar=e.target.closest('.dialogSoft span');if(!bar)return;e.preventDefault();handleHardwareKey(bar===bar.parentElement.firstElementChild?'Enter':'SoftRight')});
function clock(){let d=new Date();time.textContent=String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0')}draw();clock();setInterval(clock,1000)
