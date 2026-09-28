# C2 Reborn: phone behavior map and handover

C2 Reborn is a browser-based, evidence-led reconstruction of a Nokia C2-01 / Series 40 handset. The current public entry point is [the live phone](https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html); the repository's root `index.html` is its deployable source. This is a prototype, **not** Nokia firmware, a real cellular stack, or an Android application. The version label inside the HTML identifies the build; at this writing it is v5.43. Treat this document as a map of the implemented web build, not a guarantee that every menu item has full device behavior.

## How to read this map

A row of the form `label -> page-id` is an entry in the static `route` table in `index.html`; `[dynamic]` means the selection is handled elsewhere by the key dispatcher, often using live state. A page-id is an internal page key, not a URL. Blank target means a setting or inline action, **not** proof that a feature works. The menu arrays below are a *navigation inventory*, not a parity certification. There are also pages built at runtime that are absent from these arrays. Search for the page ID in `draw()`, `selectableRows()`, and `press(k)` before changing it. Handset footage is the highest-priority behavior evidence; the S40 SDK and this implementation can differ. See `ground-up/EVIDENCE-LEDGER.md` for the separate experimental ground-up build and `ICON-CATALOGUE.md` for firmware icon mapping.

## Inputs and navigation

- The outer shell has left/right softkeys, a four-way pad with OK, call/end, and a 12-key keypad. Pointer presses and mapped keyboard keys enter the same `press(k)` dispatcher. `pressStart/pressEnd` distinguish a hold (currently 700 ms) from a short press. The displayed softkey captions depend on screen and mode; they are not universal commands.
- At home, OK/left softkey opens the main menu, the right softkey opens its assigned shortcut, directions use configured navigation shortcuts, and digits can open the dial screen. The on-screen clock is distinct from the small status clock shown in non-home screens. Long-press shortcuts (including 0, # and speed dial keys) are handled separately from short press.
- Up/Down move selection within the current list or field. OK typically opens the selected item; Left/Right may change a picker, move the composer cursor, or switch a calendar/month/grid item depending on page. Options overlays are context-sensitive, and selection in an overlay must be interpreted by `press(k)`, not the static route table alone.
- `go(page)` pushes `{page, sel}` to a history stack and enters the destination; `back()` closes an open overlay first, then restores the prior page and selection. Some task flows bypass `go` and set `page` directly. End key and cancellation paths may reset to home. One OK must not unintentionally execute two nested selections.
- The `Go to` home shortcut has an editable application list and user-configurable shortcuts in Settings > My shortcuts. Lock/keyguard, active call, alarm, forms, media and the calendar have their own input modes. Do not apply generic list behavior to them.

## Root menu and static routing

### menu (9 entries)

- Contacts -> `contacts`
- Organiser -> `organiser`
- Media -> `media`
- Gallery -> `gallery`
- Messaging -> `messaging`
- Apps. -> `apps`
- Log -> `log`
- Settings -> `settings`
- STORE -> `store`

### contacts (10 entries)

- Names -> `names`
- Add new -> `addcontact`
- Synchronise all -> `sync`
- Settings -> `contactsettings`
- Groups -> `groups`
- Speed dials -> `speeddials`
- Service numbers -> `services`
- Del. all contacts -> `deletecontacts`
- Move contacts -> `movecontacts`
- Copy contacts -> `copycontacts`

### organiser (9 entries)

- Alarm clock -> `alarmclock`
- Calendar -> `calendar`
- Maps -> `maps`
- To-do list -> `todolist`
- Notes -> `notes`
- Calculator -> `calculator`
- Countd. timer -> `countdown`
- Stopwatch -> `stopwatch`
- Dictionary -> `dictionary`

### media (6 entries)

- Camera -> `camera`
- Video camera -> `videorecorder`
- Media player -> `musiclibrary`
- Radio -> `radio`
- Voice recorder -> `voicerecorder`
- Equaliser -> `equaliser`

### gallery (9 entries)

- Memory card -> `[dynamic / inline]`
- Images -> `[dynamic / inline]`
- Video clips -> `[dynamic / inline]`
- Music files -> `[dynamic / inline]`
- Themes -> `[dynamic / inline]`
- Graphics -> `[dynamic / inline]`
- Tones -> `[dynamic / inline]`
- Recordings -> `[dynamic / inline]`
- Received files -> `[dynamic / inline]`

### messaging (14 entries)

- Create message -> `createmessage`
- Conversations -> `conversations`
- Drafts -> `drafts`
- Outbox -> `outbox`
- Sent items -> `sent`
- Saved items -> `saved`
- Delivery reports -> `reports`
- E-mail -> `email`
- IMs -> `ims`
- Voice messages -> `voicemessages`
- Info messages -> `infomessages`
- Serv. commands -> `servicecommands`
- Delete messages -> `deletemessages`
- Message settings -> `messagesettings`

### apps (4 entries)

- Games -> `games`
- Collection -> `collection`
- Memory card -> `appmemory`
- Downloads -> `appdownloads`

### log (13 entries)

- All calls -> `allcalls`
- Missed calls -> `missed`
- Received calls -> `received`
- Dialled numbers -> `dialled`
- Msg. recipients -> `recipients`
- Clear log lists -> `clearloglists`
- Video & voice calls -> `callduration`
- Internet call durat. -> `internetcaldur`
- Data counter -> `packetcounter`
- Pack. data timer -> `packettimer`
- Message log -> `messagelog`
- Positioning -> `positioning`
- Sync log -> `synclog`

### settings (15 entries)

- Profiles -> `profiles`
- Themes -> `themes`
- Tones -> `tones`
- Lights -> `lights`
- Display -> `display`
- Date and time -> `datetime`
- My shortcuts -> `myshortcuts`
- Sync and backup -> `syncbackup`
- Connectivity -> `connectivity`
- Call -> `callsettings`
- Phone -> `phonesettings`
- Accessories -> `accessories`
- Configuration -> `configuration`
- Security -> `security`
- Rest. factory sett. -> `factoryreset`

## Submenus and settings index

The following is extracted from the static screen table. A menu entry may change with saved state (for instance, Inbox versus Conversations). Runtime-only pages and details are described separately below.

- **`createmessage`**: Message -> `compose`; Flash message -> `flashmessage`; Audio message -> `audiomessage`; Templates -> `templates`.
- **`recipientpicker`**: Favourites; Recently used; Log; Contacts; Contact groups; New number.
- **`saved`**: Templates -> `templates`; Saved messages -> `savedmessages`.
- **`deletemessages`**: By message -> `inbox`; By folder -> `folders`; All messages -> `confirmdelete`.
- **`messagesettings`**: General settings -> `generalmsg`; Text messages -> `textmsg`; Multimedia messages -> `mms`; E-mail messages -> `emailmessages`; Service messages -> `servicemsg`.
- **`generalmsg`**: Save sent messages; Overwrite sent items; Favourite recipient; Font size; Graphical smileys; Change msg. view.
- **`favourites`**: Contacts; Contact groups; New number; New e-mail addr..
- **`favadd`**: Contacts; Contact groups; New number; New e-mail addr..
- **`favreplace`**: Contacts; Contact groups; New number; New e-mail addr..
- **`textmsg`**: Delivery reports; Message centres -> `messagecentres`; Msg. centre in use -> `centreinuse`; Message validity; Messages sent via; Use packet data; Character support; Rep. via same centre.
- **`centreinuse`**: SIM msg centre 1.
- **`mms`**: Request reports; Allow read report; MMS creation mode; Image size in MMS; Default slide timing; MMS reception; Allow adverts; Configuration sett. > -> `mmsconfig`.
- **`emailmessages`**: New e-mail notif.; Allow mail reception; Reply with orig. msg.; Image size in e-mail; Edit mailboxes -> `emailmailboxes`.
- **`servicemsg`**: Service messages; Message filter; Autom. connection.
- **`mmsconfig`**: Configuration; Account -> `accounts`.
- **`accounts`**: S40 MMS.
- **`emailmailboxes`**: (empty).
- **`calendar`**: Today; All notes; Add note.
- **`callduration`**: Last call  00:00:08; Received calls  00:03:12; Dialled calls  00:05:47; All calls  00:08:59; Clear timers.
- **`packetcounter`**: Data sent; Data received; Clear counters.
- **`packettimer`**: Last session; All sessions; Clear timers.
- **`allsongs`**: S40 Test Tone.
- **`countdown`**: Normal timer -> `normaltimer`; Interval timer -> `intervaltimer`; Settings -> `countdownsettings`.
- **`stopwatch`**: Split timing -> `splittiming`; Lap timing -> `laptiming`.
- **`games`**: Brain Champ.; Block'd; City Bloxx; Bounce Tales; Diamond Rush; Snake III; Sudoku.
- **`collection`**: Facebook; Nokia Browser; My Nokia; Converter; Flickr; Web Search; Store; Size converter; World clock.
- **`appmemory`**: Phone memory; Memory card.
- **`appdownloads`**: Application downloads; Game downloads.
- **`store`**: Nokia.com; Home; Bookmarks; Go to address; Last web addr..
- **`themes`**: Select theme -> `themeselect`; Theme downloads.
- **`callwaiting`**: Activate; Cancel; Check status.
- **`slidecall`**: Open slide to answer; Close slide to end.
- **`tones`**: Incoming call alert; Ringing tone; Ring volume; Incoming call video; Message alert tone; Keypad tones; Other tones; Application tones; Alert for.
- **`display`**: Wallpaper; Home screen; Home screen font col.; Navigation key icons; Notification details; Screen saver; Font size; Operator logo; Cell info display.
- **`homescr`**: Home screen mode; Personalise view; Home screen key.
- **`datetime`**: Date & time settings; Date and time format; Auto-update of time.
- **`connectivity`**: WLAN; Internet telephone -> `intphone`; Bluetooth -> `bluetooth`; Packet data -> `packetdata`; USB data cable.
- **`datatransfer`**: Server sync; PC synchronisation.
- **`phoneswitch`**: Synchronise; Copy to this; Copy from this.
- **`serversync`**: Synchronised data; Sync settings; Automatic sync; Rules for incom. sync.
- **`pcsync`**: User name; Password.
- **`positioning`**: Position log.
- **`profileopts`**: Activate; Personalise; Timed.
- **`bluetooth`**: Bluetooth; Conn. to audio access.; Paired devices; Active devices; My phone's visibility; My phone's name.
- **`intphone`**: Accounts -> `intaccounts`; Connection tones.
- **`intaccounts`**: (empty).
- **`packetdata`**: Packet data conn.; Packet data settings -> `gprsmodem`; HS packet access.
- **`gprsmodem`**: Active access point; Edit active access pt. -> `gprsedit`.
- **`gprsedit`**: Alias for access point; Packet data acc. pt..
- **`calldivert`**: Voice calls; Video calls; All fax calls; All call types.
- **`divertvoice`**: All voice calls; If busy; If not answered; If out of reach; If not available; No voice call diverts.
- **`divertvideo`**: All video calls; If busy; If not answered; If out of reach; If not available; No video call divert.
- **`divertall`**: Always; If busy; If not answered; If out of reach; If not available; No call diverts.
- **`divertopt`**: Activate; Cancel; Check status.
- **`divertdest`**: To voice mailbox; To other number.
- **`sync`**: Synchronise contacts.
- **`contactsettings`**: Memory in use; Contacts view; Name display; Font size; Memory status.
- **`fontsize`**: Messaging; Contacts; Web.
- **`wallpaperlist`**: Photos; Open Gallery; Slide set; Open Camera; Graphic downlds.; Adjust image.
- **`screensaver`**: Photos; Open Gallery; Slide set; Video clip; Open Camera; Analogue clock; Digital clock; Graphic downlds.; Adjust image; Time-out; Off.
- **`groups`**: Family; Friends; Business.
- **`services`**: Service numbers unavailable.
- **`deletecontacts`**: From phone memory; From SIM card; All contacts.
- **`movecontacts`**: From phone to SIM; From SIM to phone.
- **`copycontacts`**: From phone to SIM; From SIM to phone.
- **`security`**: PIN code request; Call barring service; Fixed dialling; Closed user group; Security level; Access codes; Code in use; Authority certificates; User certificates; Security module sett..
- **`phonesettings`**: Language settings; Memory status; Automatic keyguard; Security keyguard; Voice recognition; Flight query; Phone updates; Network mode; Operator selection; Help text activation; Start-up tone.
- **`accessories`**: TV cable; Charger.
- **`tvcable`**: Activate TV-out; TV standard.
- **`charger`**: Default profile; Lights.
- **`configurations`**: No configurations.
- **`accesspoints`**: No access points.
- **`personalaccounts`**: (empty).
- **`configuration`**: Default config. sett.; Activ. def. in all apps.; Preferred access pt.; Connect to support; Personal config. sett..
- **`factoryreset`**: Restore settings only; Restore all.
- **`infomessages`**: Info service; Topics; Language; Info topics on SIM.
- **`tofolder`**: Saved messages; Templates.
- **`servicecommands`**: Editing options >.
- **`messageview`**: Conversations -> `conversations`; Inbox -> `inbox`.
- **`messagelog`**: Sent messages; Received messages; Draft messages.
- **`simmessages`**: No SIM messages.
- **`memorystatus`**: Phone -> `phonememory`; 32 -> `memorycarddetail`.
- **`galpicker`**: Themes; Graphics; Tones; Recordings; Received files; Playlists; 32; Images; Video clips; Music files; Themes.
- **`graphicdownloads`**: Ovi; Wallpapers; Screen savers; Clip-art; Frames.
- **`writinglanguage`**: English; Deutsch; Français; Italiano; Nederlands; Español; Türkçe; Português.
- **`predictionoptions`**: Prediction on; Word suggestions.
- **`slideoptions`**: Insert slide; Delete slide; Next slide.
- **`composeinsert`**: Symbol; Contact detail.

## Runtime screens and state movement

### Messaging

- Messaging > Create message > Message enters `compose`. Its focus moves through **To**, **Text**, and the insert strip. The To field accepts letters directly, shows contact matches while typing, and Match opens a full-screen indexed Names picker; choosing a number returns to the addressed composer. Numeric entry and the body have their own multi-tap/T9 handling. The insert strip is a real focus target with left/right item movement; inspect each insert action separately before claiming full attachment support.
- Sending checks for nonempty body and parsable recipients, normalizes duplicate numbers, appends an outbound item to the corresponding conversation, and updates Sent items. Sending in this prototype updates local data; it does **not** send an SMS or MMS. Numbered threads use `number-<digits>` keys. The prefilled conversation and synthetic rows are demo data; synthetic rows without a number must not invent a reply destination.
- Conversations, Inbox, Drafts, Outbox, Sent items and Saved items share message state but have different list and options logic. Inbox is a configurable alternative to the Conversations landing view, via Messaging options > Inbox view. Read/unread status changes on opening messages. Sent/received icons differ; the source has firmware-derived image data for row icons. Delete actions use a Yes/No confirmation; cancel must leave the selected item intact. Multi-mark/filter state is cleared when leaving Conversations.
- Drafts and templates are local. Delivery reports, service commands, e-mail and IM screens do not imply actual network integration. Check `press(k)` for each action.

### Contacts and call log

- Contacts > Names renders the saved contact list, alphabetic search, detail screen and actions. Add/Edit contact writes a structured record (names, mobile/home number, email, address, birthday and more) to saved state. Contact matching also feeds composer To, recipient picker, call display and call-log labels. A changed contact label should be checked in all of those surfaces.
- Contacts Settings, Groups, Synchronise all, Speed dials, Service numbers, delete/move/copy are distinct screens. Copy number refers to transfer between contact memories, **not** copying text to a clipboard. The detailed SIM/phone flow needs physical-device evidence; do not infer completeness from the menu title.
- Call starts `incall`, adds a dialled call to Log, and tracks duration on end; flight mode blocks it. This is an on-screen simulation, not a carrier call. Log groups All/Missed/Received/Dialled and includes recipient/history, timers and counters. Saving from log can enter contact creation. Contacts, active call, log and message recipients share number-based identities; preserve the chosen number, not just its display name. Network-dependent call divert or status controls must be marked as simulated/unverified unless separately evidenced.

### Gallery, camera, media and recorder

- Gallery has top-level memory card, images, video, music, themes, graphics, tones, recordings and received files. Lists and file actions can be stateful: rename, delete, move/copy, details, view or use image. Consult the dynamic gallery branch of `draw()`/`press(k)`; the static `screens.gallery` table only enumerates the root.
- Camera and video camera enter capture screens. Captures are local demo artifacts stored in `galCaptures`, then surfaced in gallery. Media player has its own library/playback state. Radio has volume and station controls. Voice recorder routes recordings into media/gallery state. Browser permissions and device APIs must be assessed before an APK claims to capture real media or provide radio.

### Organiser and time

- Organiser routes to Alarm clock, Calendar, Maps, To-do list, Notes, Calculator, Countd. timer, Stopwatch and Dictionary. Calendar uses day/month views, note details and a typed note editor; the note types are Reminder, Meeting, Call, Birthday, Anniversary and Memo. Its date/time, repeat and alarm fields have page-specific input handlers. To-do and Notes have separate saved collections. Countdown and stopwatch use timers and intervals. These are local app behaviors, not Android reminders, notifications or calendar sync.
- Date/time settings, shortcuts and profile/theme preferences affect multiple screens. A theme change must be checked in lists, forms, dialogs, calendar notes, messaging and the composer, not just at home. Settings > Sync and backup offers local backup/restore behavior; do not present it as a cloud backup.

## State, rendering and assets

- The production prototype is a single HTML file with inline CSS, HTML, JavaScript and embedded data-URL images. `draw()` renders the screen selected by `page`; `sel` is the current row, while overlays, form focus, pending confirmations and timers have their own transient variables. `screens` lists static labels; `route` contains some static destinations; `opts` lists many context menus. Dynamic rows come from state and helper functions such as `selectableRows()`. Never assume these three tables fully define an interaction.
- `STATE_VERSION` is currently 6. `phoneState` starts from `defaultState` and is migrated by `migrateState()` from browser `localStorage['c2state']`; `persist()` writes it back. `messageStore` is nested in `phoneState` with its own schema 1 normalization, threads, inbox, saved/hidden/marked records and numbered thread keys. Other saved state includes contacts, calls, drafts, notes, calendar, gallery edits/captures, profiles, themes, player/radio, shortcuts, timers and settings. Inspect the exact versioned schema before changing it; preserve existing users' saved state with a migration.
- Browser storage belongs to the origin and profile. It is **not** a backend database, cloud sync, SIM store, telephony service or durable cross-device account. Deleting browser data resets local state. Demo contacts, messages and call rows are fixture data; do not ship them as if they came from a user's handset.
- Many firmware assets are embedded as base64 data URLs; the catalogue distinguishes shipped, verified, candidate and unidentified assets. Do not replace an uncertain icon with a crop of personal handset footage. Maintain the actual image asset mapping when moving to an APK.

## Development and verification

1. Edit the root `index.html` as the deployable build; `2-index.html` and `ground-up/` are separate artifacts, not automatically merged. Keep source versions and verification evidence clearly labeled. Do not assume the presence of a branch named `dev`: inspect the current repository before choosing a branch.
2. Run the local regression/interaction checks appropriate to the change. Then open the deployed site and press through the affected flows on the real rendered UI. A successful upload or matching hash proves bytes, **not** that a screen boots or a key behaves correctly. Compare the published file bytes with the frozen artifact, then take screenshots of live behavior. GitHub Pages can lag the repository update.
3. Compare critical LCD interactions with physical C2-01 footage first; use SDK emulator captures as a secondary source. Document deviations and untested hardware-dependent actions instead of silently improvising. Use `ICON-CATALOGUE.md` to keep asset meaning traceable.
4. This README commit is documentation only; it does not alter the HTML, deploy a build, or package an APK. Follow the current handover decision before any separate deployment.

## APK handover: decisions still to make

- First choose WebView wrapping versus a native UI rewrite. A WebView can preserve CSS, keyboard dispatch and localStorage more directly, but it does not turn simulated SMS, calls, SIM contacts, Bluetooth, radio, camera or synchronization into working Android services. A native rewrite must port the screen/key state machine and interaction contracts, not just screenshot the LCD.
- Map every physical Android key and on-screen key to the semantic `press(k)` inputs; preserve short/long-press thresholds, softkeys, history/back behavior and modal precedence. Test keyboard and touch independently. Decide how Android Back interacts with the in-phone right softkey and End.
- Define a versioned storage migration from `c2state`, including messageStore schema, existing drafts/contacts/calendar/gallery and backup data. Decide whether to import browser-origin localStorage on the same device; WebView does not automatically inherit Chrome's storage. Get user consent and platform permissions before importing real contacts/messages or enabling any network service.
- Classify each feature as fixture, local interactive simulation, or actual Android integration, and show those distinctions in the app. Request only permissions needed for implemented functionality. Do not ask for SMS/call log/contacts permissions merely because the replica has those menu labels.
- Keep firmware visual evidence and font/layout parity checks separate from functional tests. Validate light and dark themes, long names, empty lists, large message stores, time/date boundaries, orientation/scale, accessibility and keyboard repeat. Build from a frozen source commit and compare the APK's bundled HTML/assets with that commit.

The detailed executable behavior remains in `index.html`. This map is an entry point for a new developer or agent and should be updated when routes or state transitions change.

## Options-menu inventory

This is a static index of `opts`, not a promise that every option is live. An option's submenu and effect are handled inside `press(k)` and state-specific branches; inspect those before extending it. Some Options menus are synthesized dynamically and are absent here.

- **`alertformark`**: Unmark all; Undo selections.
- **`configurations`**: Set as default; Delete.
- **`accesspoints`**: Details.
- **`rcptcontacts`**: Done; Mark all; Unmark all.
- **`logpicker`**: Add recipient.
- **`persview`**: Content options.
- **`datatransfer`**: Edit.
- **`pcsyncname`**: Insert character.
- **`pcsyncpass`**: Insert character.
- **`menu`**: Main menu view; Organise.
- **`messaging`**: Conversations; New message; Inbox view; Message log; SIM messages; Memory status.
- **`drafts`**: New message; Inbox view; Folder details; Message log; SIM messages; Memory status.
- **`outbox`**: New message; Inbox view; Folder details; Message log; SIM messages; Memory status.
- **`sent`**: Open; Delete; New message; Inbox view; Folder details; Message log; SIM messages; Memory status.
- **`saved`**: New message; Inbox view; Folder details; Message log; SIM messages; Memory status.
- **`inbox`**: Reply; Reply as; Delete; Call; Use detail; Forward; Edit; Move; Copy as template; Message details; Conversation view; New message.
- **`conversations`**: Call; Conversation details; Delete conversation; Inbox view >; New message >; Mark >; Mark all.
- **`conversation`**: Reply; Delete; Call; Move; Go to Drafts; Conversation details; Mark.
- **`msgopen`**: Delete; Send copy; Edit; Move; Use detail; Copy to Calendar; Copy as template; Message details.
- **`stopwatch`**: Split timing; Lap timing.
- **`compose`**: Send; Preview; Insert; Add recipient >; Add subject; Search; Clear field; Insert contact detail; Insert symbol ▸; Editing options ▸; Writing language ▸; Prediction options ▸; Change to multim.; Save message >; Sending options >; Exit editor.
- **`contacts`**: Open; Search; Add new; Memory status.
- **`names`**: Search; Call; Send message >; View conversations; Find on map; Add new >; Edit >; Delete contact; Marking options >.
- **`contact`**: Add detail >; Call; Edit; Delete; Send message >; View conversations; Add image >; Use number; Set as default; Change type >; Copy number; Send business card >; Add to group; Speed dial.
- **`log`**: View; Call; Send message; Save; Delete; Clear lists; Call timers.
- **`missed`**: Call; Send message; Save to contacts; Delete; Clear list.
- **`settings`**: Open; Search.
- **`profiles`**: Activate; Personalise; Timed.
- **`galfolder`**: Downloads ▸; Use image; Delete; Send ▸; Move; Copy; Rename; Edit image; Rotate ▸; Print; Details; Type of view ▸; Sort ▸; Open in sequence; Add folder; Memory status; Search; Mark; Mark all.
- **`galphoto`**: Use image; View full screen; Delete; Move; Copy; Rename; Zoom; Set contrast; Edit image; Rotate ▸; Print; Details; Open in sequence.
- **`galmark`**: Open; Delete marked; Send marked ▸; Move marked; Copy marked; Details; Type of view ▸; Sort ▸; Marking options ▸.
- **`gallery`**: Downloads ▸; Delete folder; Move folder; Copy folder; Rename folder; Details; Type of view ▸; Sort ▸; Add folder; Memory status; Search; Mark; Mark all.
- **`organiser`**: Open; Make a note; Week view; Go to date; Go to today; Settings; Memory status.
- **`calendar`**: Make a note ▸; Week view; Go to date; Go to today; Delete notes ▸; Settings; Memory status; Go to To-do list.
- **`calview`**: View; Make a note ▸; Delete.
- **`calopen`**: Send as message; Edit; Delete.
- **`calnote`**: Search; Clear field; Insert symbol ▸; Editing options ▸; Writing language ▸; Prediction options ▸.
- **`caltypes`**: Select.
- **`todolist`**: Add; Delete; Mark note as done; Use detail ▸; Sort by deadline; Send ▸; Delete notes ▸; Memory status; Go to Calendar; Save to Calendar.
- **`todoempty`**: Memory status; Go to Calendar.
- **`todoview`**: Mark note as done; Delete; Use detail ▸; Send ▸; Go to Calendar; Save to Calendar.
- **`notes`**: Make a note; Delete; Edit; Use detail >; Send note >; Delete all notes; Memory status.
- **`noteview`**: Delete; Use detail >; Send note >; Editing options >.
- **`noteedit`**: Insert time and date; Search; Clear field; Insert symbol ▸; Editing options ▸; Writing language ▸; Prediction options ▸.
- **`todoedit`**: Clear field; Insert symbol ▸; Editing options ▸; Writing language ▸; Prediction options ▸; Dictionary; Cancel.
- **`timernote`**: Search; Clear field; Insert symbol ▸; Editing options ▸; Writing language ▸; Prediction options ▸.
- **`addcontact`**: Search; Clear field; Insert symbol ▸; Editing options ▸; Writing language ▸; Prediction options ▸.
- **`foldername`**: Clear field; Insert character; Editing options ▸; Writing language ▸.
- **`usedetail`**: Number; Internet telephone; E-mail address; Web address; User ID.
- **`sendnote`**: Send as message; Via calendar; Via Bluetooth.
- **`usedetailnumber`**: Save.
- **`contactmark`**: Mark; Mark all.
- **`contactadddetail`**: Mobile; Telephone; E-mail address; Web address.
- **`businesscard`**: Via multimedia; Via text message; Via Bluetooth.
- **`noteediting`**: Copy; Copy all; Cut; Paste.
- **`insertword`**: Save.
- **`apps`**: Open; Move; Move to folder; Organise; Add folder; Memory status.
- **`store`**: Open; Home; Bookmarks; Go to address; Downloads; Settings.
- **`goto`**: Select options; Organise.
- **`dial`**: Call; Save; Send message; Add to contact.
- **`incall`**: Loudspeaker; Mute; Hold; Contacts; Main menu; End call.
- **`player`**: Music library; Now playing; Shuffle; Repeat; Equaliser; Settings.
- **`themes`**: Open; Theme downloads; Type of view; Sort; Search; Memory status.
- **`tones`**: Change; Play; Save.
- **`display`**: Change; Open; Restore default.
- **`datetime`**: Change; Restore default.
- **`bluetooth`**: Open; New search; Details; Delete pairing.
- **`calculator`**: Scientific calculator; Loan calculator; Instructions; Exit.
- **`scientific`**: Standard calculator; Loan calculator; Instructions; Exit.
- **`loancalc`**: Calculate; Standard calculator; Scientific calculator; Instructions; Exit; Editing options.
- **`loanediting`**: Paste.
- **`infomessages`**: Info service; Topics; Language; Info topics on SIM.
- **`tofolder`**: Saved messages; Templates.
- **`servicecommands`**: Editing options >.
- **`messageview`**: Conversations; Inbox.
- **`memorystatus`**: Open.
- **`phonememory`**: Open.
- **`messagelog`**: Open; Clear log.
- **`simmessages`**: Open.
- **`messagedetails`**: Open.
- **`writinglanguage`**: Select.
- **`predictionoptions`**: Select.
- **`sendingoptions`**: Change.
- **`composeinsert`**: Select.
- **`contactsearch`**: Search.
- **`logtimers`**: Open.
- **`callduration`**: Clear timers.
- **`packetcounter`**: Clear counters.
- **`packettimer`**: Clear timers.
- **`camera`**: Capture; Self-timer; Effects; Settings.
- **`videorecorder`**: Record; Video settings; Memory in use.
- **`radio`**: Switch off; Save station; Stations; Search stations; Set frequency; Settings.
- **`voicerecorder`**: Record; Recordings list; Memory in use.
- **`equaliser`**: Edit; Rename.
- **`maps`**: Open map; Search; Favourites; Settings.
- **`recipients`**: Call; Send message; Save to contacts; Clear list.
- **`voicemessages`**: Call voice mailbox; Voice mailbox no.; Info.
- **`ims`**: Sign in; Saved conversations; Settings.
- **`packetdata`**: Packet data conn.; Packet data settings.
- **`browser`**: Open; Home; Bookmarks; Go to address; Last web addr.; Downloads; Settings.

## Trace a screen precisely

1. Locate its incoming entry in `route` or a direct `go('page-id')` in `press(k)`; note the caller and any focus state it sets.
2. Find its `draw()` branch and `selectableRows()` source. A dynamic list can differ from `screens[page]` in length, sorting, availability and row icons.
3. Inspect `press(k)` for modal precedence, selected-row action, short/long press, softkeys and form-specific navigation. Inspect `opts[page]` and dynamic Options overrides separately.
4. Follow every state write to `persist()` and verify the return path via `back()` or direct page assignment. Check every other screen that reads the same collection. For a delete or destructive action, verify the confirmation and cancellation routes.
5. Test the resulting pixels and behavior in the browser on both dark and pale themes, then compare with real handset evidence where available. A table row or source-level handler alone does not prove parity.
