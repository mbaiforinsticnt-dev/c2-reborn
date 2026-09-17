const menu=[
['Organiser','OrganizerMenu','assets/icons/organiser.png'],['Contacts','MainPB','assets/icons/contacts.png'],['E-mail','nlink:8','assets/icons/email.png'],['Browser','BrowserMenu','assets/icons/browser.png'],['Messaging','MessagesMenu','assets/icons/messaging.png'],['Gallery','ContentBaseMenu','assets/icons/gallery.png'],['Store','nlink:2','assets/icons/store.png'],['Media','MediaMenu','assets/icons/media.png'],['Applications','ApplicationsMenu','assets/icons/applications.png'],['Settings','SettingsMenu','assets/icons/settings.png'],['Log','CallListsMenu','assets/icons/log.png']
];
const submenus={
Organiser:['Alarm clock','Calendar','Maps','To-do list','Notes','Calculator','Countdown timer','Stopwatch','Dictionary'],
Contacts:['Names','Add new contact','Synchronise','Network query','Memory options','Caller groups','Speed dials','Service numbers','Own numbers','Delete all contacts','Move contacts','Copy contacts'],
Browser:['Ovi','Nokia','Home','Web search','Browser','Operator link 1','Operator link 2','Operator link 3','Bookmarks','Go to address','Last web address','Content upload','Upload to blog','Download links','Web settings','Clear cache'],
Messaging:['Create message','Inbox','Conversations','Instant messaging','Mailbox 1','Mailbox 2','Mailbox 3','Mailbox 4','Mailbox 5','Drafts','Outbox','Sent items','Saved items','Delivery reports','E-mail client','Instant messaging 2','Voice mailbox','Info messages','Service commands','Delete messages','Message settings'],
Gallery:['Photos','Music and videos','Gallery'],
Media:['Camera','Video','Music player','Radio','Voice recorder','Equaliser'],
Applications:['Applications','Downloads','Settings','Memory status'],
Settings:['Operator settings','Profiles','Themes','Tones','Lights','Display','Date and time','My shortcuts','Sync and backup','Connectivity','Call','Phone','Accessories','Configuration','Security','Restore factory settings'],
Log:['All calls','Missed calls','Received calls','Dialled numbers','Message recipients','Clear log lists','Call duration','Data counters','Connection timer','Message counter','Positioning','Sync log'],
'E-mail':['E-mail application (Java reference only)'],Store:['Ovi Store application (service reference only)']
};
const appCatalog=[{"name":"Facebook","version":"1.3.5","vendor":"Nokia","descriptor":"Facebook.jad"},{"name":"OviBrowser","version":"1.0.1","vendor":"Nokia","descriptor":"OviBrowser_EUS.jad"},{"name":"Brain Champion","version":"1.1.22","vendor":"Nokia","descriptor":"bc_EUF.jad"},{"name":"Block'd","version":"1.4.7","vendor":"Electronic Arts Inc.","descriptor":"blockd_EUF.jad"},{"name":"City Bloxx","version":"1.0.22","vendor":"Nokia","descriptor":"bloxx_EUF.jad"},{"name":"Bounce Tales","version":"2.0.24","vendor":"Nokia","descriptor":"bounce2_EUF.jad"},{"name":"Calculator","version":"3.30","vendor":"Nokia","descriptor":"calc2_EUF.jad"},{"name":"My Nokia","version":"1.8.2","vendor":"Nokia","descriptor":"cherry_EUF.jad"},{"name":"Converter","version":"1.81","vendor":"Nokia","descriptor":"conv_EUROPE.jad"},{"name":"Diamond Rush","version":"1.1.7","vendor":"Nokia","descriptor":"diamond_EUF.jad"},{"name":"Flickr","version":"3.0.12","vendor":"Nokia","descriptor":"flickr_EUF.jad"},{"name":"Web Search","version":"1.1.59","vendor":"Nokia","descriptor":"isuite_EUF.jad"},{"name":"E-mail","version":"1.3.53","vendor":"Nokia","descriptor":"nmsemail_EUF.jad"},{"name":"Instant Messaging","version":"1.3.45","vendor":"Nokia","descriptor":"nmsim_EUF.jad"},{"name":"Operette","version":"4.2.55","vendor":"Opera","descriptor":"operette_hifi_nokia_s40_14_chapi-all.jad"},{"name":"Ovi Store","version":"2.4.0","vendor":"Nokia","descriptor":"ovistore_ovistore15.jad"},{"name":"Size converter","version":"2.17","vendor":"Nokia","descriptor":"sico_EUF.jad"},{"name":"Snake III","version":"3.07.3","vendor":"Nokia","descriptor":"snake3d_EUF.jad"},{"name":"World clock","version":"3.37","vendor":"Nokia","descriptor":"wocl_EUF.jad"}];
const endpointModels={
 'Alarm clock':{kind:'time',lead:'07:00',rows:['Alarm: Off','Alarm time','Repeat','Alarm tone']},
 Calendar:{lead:'Today · No calendar notes',rows:['View','Make a note','Week view','Go to date']},
 'To-do list':{lead:'No to-do notes',rows:['Open','Add','Delete','Go to calendar']},
 Notes:{lead:'No notes',rows:['Make a note','Edit','Delete','Memory status']},
 Calculator:{lead:'0',rows:['Standard calculator','Scientific calculator','Loan calculator','Instructions']},
 'Countdown timer':{kind:'time',lead:'00:00:00',rows:['Normal timer','Interval timer','Settings','Start']},
 Stopwatch:{kind:'time',lead:'00:00:00.0',rows:['Split timing','Lap timing','Continue','Reset']},
 Profiles:{lead:'General · active',rows:['General','Silent','Meeting','Outdoor']},
 Themes:{lead:'Black · active',rows:['Select theme','Theme downloads','Type of view','Memory status']},
 Tones:{lead:'Ringing tone · Nokia tune',rows:['Incoming call alert','Ringing tone','Ring volume','Message alert tone']},
 Display:{lead:'Black theme display',rows:['Wallpaper','Home screen','Font colour','Main menu view']},
 'Date and time':{kind:'time',lead:new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'}),rows:['Date & time settings','Date & time format','Auto-update of time','Time zone']},
 Connectivity:{lead:'Offline',rows:['Bluetooth','Packet data','USB data cable','Network status']},
 Security:{lead:'Phone security',rows:['PIN code request','Security level','Access codes','Certificates']},
 'Create message':{kind:'messages',lead:'New message',rows:['Message','Flash message','Audio message','Templates']},
 Inbox:{kind:'messages',lead:'No personal messages loaded',rows:['Open list','Create message','Search','Inbox view']},
 Conversations:{kind:'messages',lead:'No personal conversations loaded',rows:['Open','New message','Conversation details','Inbox view']},
 Drafts:{kind:'messages',lead:'Drafts · local phone storage',rows:['Open','Create message','Delete','Message details']},
 Camera:{kind:'camera',lead:'Camera preview unavailable in browser',rows:['Capture','Self-timer','Effects','Settings']},
 Video:{kind:'camera',lead:'Video preview unavailable in browser',rows:['Record','Video settings','Memory in use','Back']},
 'Music player':{lead:'No track playing',rows:['Music library','All songs','Playlists','Settings']},
 Radio:{lead:'Headset required · offline',rows:['Switch on','Stations','Search stations','Set frequency']},
 'Voice recorder':{kind:'time',lead:'00:00:00',rows:['Record','Recordings list','Memory in use','Settings']},
 Equaliser:{lead:'Normal',rows:['Activate','Edit','Rename','Reset']},
 'Missed calls':{lead:'No personal call records loaded',rows:['View entries','Clear list','Call duration','Details']},
 'Received calls':{lead:'No personal call records loaded',rows:['View entries','Clear list','Call duration','Details']},
 'Dialled numbers':{lead:'No personal call records loaded',rows:['View entries','Clear list','Call duration','Details']},
 Bookmarks:{kind:'offline',lead:'Offline web reference',rows:['Nokia.com','Home','Add bookmark','Manage']},
 'Go to address':{kind:'offline',lead:'Enter web address · offline',rows:['Address','Recent addresses','Clear field','Settings']}
};
function detailModel(section,item){
 if(endpointModels[item])return endpointModels[item];
 const low=item.toLowerCase();let lead=`${item} UI reference surface from the ${section} menu.`,rows=['Open','Status','Settings','Help'],kind='generic';
 if(/contact|names|numbers|groups|dial/.test(low)){rows=['List','Add','Search','Options'];lead='Contacts reference surface. No personal records are loaded.';kind='contacts'}
 else if(/message|mailbox|sent|outbox|saved/.test(low)){rows=['Open list','Create','Search','Message settings'];lead='Messaging reference surface. Message content is local test data only.';kind='messages'}
 else if(/setting|shortcut|sync|backup|call|phone|accessor|configuration|restore/.test(low)){rows=['Current value','Change','Open','Restore default'];lead='Settings reference surface. Changes stay inside this offline phone.';kind='settings'}
 else if(/photo|gallery|download|application|memory/.test(low)){rows=['Open folder','Items','Memory status','Options'];lead='Content reference surface generated from the firmware menu route.';kind='content'}
 else if(/call|log|timer|counter|recipient/.test(low)){rows=['View entries','Clear list','Duration','Details'];lead='Log reference surface. No personal call records are used.';kind='log'}
 else if(/browser|ovi|nokia|web|cache|operator/.test(low)){rows=['Open reference','Address','Bookmarks','Settings'];lead='Offline web/service reference. No retired service is contacted.';kind='offline'}
 return {lead,rows,kind};
}
const shallow={Organiser:'Alarm clock · Calendar · Maps · To-do list · Notes · Calculator · Countdown timer · Stopwatch · Dictionary','Contacts':'Names · Add new · Groups · Speed dials','E-mail':'Original firmware application entry',Browser:'Nokia / Ovi browser entry',Messaging:'Create message · Inbox / Conversations · Drafts · Sent · Settings',Gallery:'Physical media chooser pending capture',Store:'Original Ovi Store application entry',Media:'Camera · Video · Player · Radio · Voice recorder · Equaliser',Applications:'Games · Collection · Downloads · Settings',Settings:'Profiles · Themes · Tones · Display · Time · Connectivity',Log:'All calls · Missed · Received · Dialled · Timers'};
let selected=0,view='menu',optionsOpen=false,optionSel=0,submenuSel=0,menuMode='labelgrid',catalogSel=0,detailSel=0,detailActivated=false;
function draw(){optionsBox.classList.toggle('hidden',!optionsOpen);if(optionsOpen){let labels=['Single','List','Grid','Grid with labels'];let a=view==='viewDialog'?labels.map((x,i)=>(i===['single','list','grid','labelgrid'].indexOf(menuMode)?'◉ ':'◯ ')+x):view==='catalog'?['Application details','Descriptor source','Java scope']:view==='detail'?['About this screen','Reset test state']:['Main menu view ›','Organise'];optionsBox.innerHTML='<div class="optionsBody">'+a.map((x,i)=>`<div class="option ${i===optionSel?'selected':''}">${x}</div>`).join('')+'</div><div class="dialogSoft"><span>Select</span><span>Back</span></div>'};if(view==='menu'||view==='viewDialog'){let pageSize=menuMode==='single'?1:menuMode==='list'?8:9,start=Math.floor(selected/pageSize)*pageSize;grid.className='grid mode-'+menuMode;grid.innerHTML=menu.slice(start,start+pageSize).map((x,j)=>`<div class="cell ${start+j===selected?'selected':''}" data-contract="${x[1]}"><img src="${x[2]}" alt=""><span>${x[0]}</span></div>`).join('');grid.parentElement.classList.remove('hidden');appscreen.classList.add('hidden');screenTitle.textContent='Menu';count.textContent='';leftSoft.textContent='Options';centerSoft.textContent='Select';rightSoft.textContent='Exit'}else{grid.parentElement.classList.add('hidden');appscreen.classList.remove('hidden');let x=menu[selected];count.textContent='';if(view==='detail'){let section=menu[selected][0],item=(submenus[section]||['UI reference'])[submenuSel],m=detailModel(section,item);screenTitle.textContent=section;appTitle.textContent=item;submenuList.innerHTML=`<div class="detailCard" data-kind="${m.kind||'generic'}"><div class="detailLead">${m.lead}</div><div class="detailRows">${m.rows.map((r,i)=>`<div class="detailRow ${i===detailSel?'selected':''}">${r}<span class="detailValue">${i===0?(detailActivated?'Active':'Ready'):'›'}</span></div>`).join('')}</div></div>`;appText.textContent='Functional UI-reference route · '+section+' / '+item;leftSoft.textContent='Options';centerSoft.textContent='Select';rightSoft.textContent='Back'}else if(view==='catalog'){screenTitle.textContent='Applications';appTitle.textContent='Installed applications';submenuList.innerHTML=appCatalog.map((a,i)=>`<div class="submenuRow ${i===catalogSel?'selected':''}" data-catalog-index="${i}">${a.name} ${a.version}</div>`).join('');appText.textContent=appCatalog[catalogSel].vendor+' · '+appCatalog[catalogSel].descriptor+' · JAD metadata reference';leftSoft.textContent='Options';centerSoft.textContent='Details';rightSoft.textContent='Back'}else{screenTitle.textContent=x[0];appTitle.textContent=x[0];let rows=submenus[x[0]]||['UI reference pending evidence'];submenuList.innerHTML=rows.map((r,i)=>`<div class="submenuRow ${i===submenuSel?'selected':''}">${r}</div>`).join('');appText.textContent='Firmware route: '+x[1];leftSoft.textContent='Options';centerSoft.textContent='Open';rightSoft.textContent='Back'}requestAnimationFrame(()=>submenuList.querySelector('.selected')?.scrollIntoView({block:'nearest'}))}lcd.dataset.uiState=JSON.stringify({view,selected,submenuSel,catalogSel,detailSel,detailActivated,menuMode,optionsOpen,optionSel})}
function move(key){if(optionsOpen){let n=view==='viewDialog'?4:view==='catalog'?3:2;if(key==='ArrowUp')optionSel=(optionSel+n-1)%n;if(key==='ArrowDown')optionSel=(optionSel+1)%n;draw();return}if(view!=='menu')return;if(menuMode==='single'||menuMode==='list'){if(key==='ArrowDown'||key==='ArrowRight')selected=(selected+1)%menu.length;if(key==='ArrowUp'||key==='ArrowLeft')selected=(selected+menu.length-1)%menu.length;draw();return}let pageStart=Math.floor(selected/9)*9,pageEnd=Math.min(menu.length-1,pageStart+8),col=(selected-pageStart)%3,row=Math.floor((selected-pageStart)/3);if(pageStart===9){if(key==='ArrowLeft')selected=Math.max(9,selected-1);if(key==='ArrowRight')selected=Math.min(10,selected+1);if(key==='ArrowUp'||key==='ArrowDown')selected=Math.min(pageEnd,pageStart+col);draw();return}if(key==='ArrowRight')selected=row*3+(col+1)%3;if(key==='ArrowLeft')selected=row*3+(col+2)%3;if(key==='ArrowDown')selected=((row+1)%3)*3+col;if(key==='ArrowUp')selected=((row+2)%3)*3+col;draw()}
function activate(){if(optionsOpen){if(view==='detail'){optionsOpen=false;detailActivated=optionSel===0?detailActivated:false;draw();appText.textContent=optionSel===0?'Functional UI-reference screen; physical geometry pending route evidence.':'Test state reset.';return}if(view==='catalog'){let a=appCatalog[catalogSel],messages=[`${a.name} ${a.version} · ${a.vendor}`,`Descriptor: ${a.descriptor} · exact supplied JAD metadata`,`Executable Java UI is outside current scope; identity retained for UI reference.`];optionsOpen=false;draw();appText.textContent=messages[optionSel];return}if(view==='viewDialog'){menuMode=['single','list','grid','labelgrid'][optionSel];optionsOpen=false;view='menu';draw();return}if(optionSel===0){view='viewDialog';optionSel=['single','list','grid','labelgrid'].indexOf(menuMode);draw()}else{optionsOpen=false;view='app';draw();screenTitle.textContent='Organise';appTitle.textContent='Organise';appText.textContent='Menu reorder mode waits for physical key-by-key evidence.'}return}if(view==='menu'){view='app';draw();let c=document.querySelector('.cell.selected');c?.classList.add('pressed');setTimeout(()=>c?.classList.remove('pressed'),120)}else{appText.textContent=shallow[menu[selected][0]]+' · Deeper behavior waits for route evidence.'}}
function back(){if(optionsOpen&&view==='viewDialog'){view='menu';optionSel=0;draw();return}if(optionsOpen){optionsOpen=false;draw();return}if(view==='app'){view='menu';draw()}}function openOptions(){if(view==='menu'){optionsOpen=true;optionSel=0;draw()}else{appText.textContent+=' · Options behavior pending direct evidence.'}}
function moveCatalog(delta){
 const before=catalogSel;
 catalogSel=(catalogSel+delta+appCatalog.length)%appCatalog.length;
 draw();
 return {before,after:catalogSel,item:appCatalog[catalogSel]};
}
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
  else if(view==='app'&&(key==='ArrowUp'||key==='ArrowDown')){let rows=submenus[menu[selected][0]]||['UI reference pending evidence'];submenuSel=(submenuSel+(key==='ArrowDown'?1:-1)+rows.length)%rows.length;draw();response=`selected ${rows[submenuSel]}`}
  else if(view==='catalog'&&(key==='ArrowUp'||key==='ArrowDown')){let transition=moveCatalog(key==='ArrowDown'?1:-1);response=`selected ${transition.item.name} (${transition.before}→${transition.after})`}
  else if(view==='detail'&&(key==='ArrowUp'||key==='ArrowDown')){let m=detailModel(menu[selected][0],submenus[menu[selected][0]][submenuSel]);detailSel=(detailSel+(key==='ArrowDown'?1:-1)+m.rows.length)%m.rows.length;draw();response=`selected ${m.rows[detailSel]}`}
  else response='no horizontal route evidenced on this list';
 }
 else if(key==='Enter'||key==='SoftCenter'){
  if(optionsOpen){activate();response=view==='viewDialog'?'opened Main menu view choices':optionsOpen?'selected option':'confirmed selection'}
  else if(view==='menu'){let label=menu[selected][0];submenuSel=0;activate();response=`opened ${label}`}
  else if(view==='app'&&menu[selected][0]==='Applications'&&submenuSel===0){view='catalog';catalogSel=0,detailSel=0,detailActivated=false;draw();response='opened 19 JAD application identities'}
  else if(view==='catalog'){let a=appCatalog[catalogSel];appText.textContent=`${a.name} ${a.version} · ${a.vendor} · ${a.descriptor} · executable Java UI outside current scope`;response=`showed ${a.name} JAD details`}
  else if(view==='detail'){let m=detailModel(menu[selected][0],submenus[menu[selected][0]][submenuSel]);detailActivated=!detailActivated;draw();response=`${m.rows[detailSel]} ${detailActivated?'activated':'ready'}`}
  else {let rows=submenus[menu[selected][0]]||['UI reference pending evidence'];view='detail';detailSel=0;detailActivated=false;draw();response=`opened ${rows[submenuSel]} reference surface`};
 }
 else if(key==='SoftLeft'){
  if(view==='menu'){openOptions();response='opened Options'}
  else if(view==='catalog'){optionsOpen=true;optionSel=0;draw();response='opened application reference Options'}
  else if(view==='detail'){optionsOpen=true;optionSel=0;draw();response='opened screen Options'}
  else {openOptions();response='Options route pending direct evidence on this screen'};
 }
 else if(key==='SoftRight'||key==='Escape'){
  if(optionsOpen&&view==='viewDialog'){back();response='returned to Options'}
  else if(optionsOpen){back();response='closed Options'}
  else if(view==='catalog'){view='app';draw();response='returned to Applications'}
  else if(view==='detail'){view='app';draw();response='returned to '+menu[selected][0]}
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
