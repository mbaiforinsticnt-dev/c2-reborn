# C2-01 Ground-Up evidence ledger

## Authority order

1. Physical Nokia C2-01 (Moti's RM-721 handset).
2. RM-721-specific firmware or direct evidence.
3. RM-722 / product 059F5P7 content, explicitly labelled inference.
4. Generic Series 40 6th Edition SDK.
5. Audits and third-party guides, used as leads only.

Conflicts are recorded. Evidence is never averaged.

## Current corpus

- Supplied extracted firmware archive: 715 files; SHA-256 `0835f2b036850ec7ad550f93c0aea316ee96c26110ddb1b103eddc900e08ac80`.
- Four original themes: Black, Dark, Light, Nokia. Each original `.nth` and every unpacked member is retained.
- 57 AAC tones.
- 19 JAD + 19 JAR Java packages.
- 8 native `.nfl` packages.
- 394 WBXML and 117 ConfML configuration files, plus XML/INI/CSV configs.
- Orange C2-01 menu-map PDF is retained as carrier-specific guide evidence. Orange custom items are excluded from the product.
- `firmware-inventory.csv` records every firmware file, byte count, category, SHA-256, and evidence label.
- `theme-assets.csv` records every unpacked theme member and SHA-256.
- `apps.json` records application identity/version/vendor from each JAD.

## Physical evidence already established

- Moti's handset is RM-721, Series 40 6th Edition, 3G.
- Conversation view exists on the physical C2-01 despite being absent from the generic emulator firmware.
- Gallery first asks Photos / Music & videos / All content.
- Add recipient includes New number for unsaved digits.
- Messaging Options includes Conversations / New message / Inbox view / Message log / SIM messages / Memory status.
- Calculator softkeys differ from the SDK emulator; the physical handset wins.
- Hardware has one continuous chrome navigation ring, blue key legends, no side volume buttons; volume uses navigation Up/Down.
- Physical screen recordings and screenshots define exact route, softkey, Options, Back, persistence and state-transition contracts where available.

## Known disagreements

| Area | Physical RM-721 | Generic SDK / other | Decision |
|---|---|---|---|
| Messaging | Threaded Conversations and Inbox-view toggle | Flat Inbox on 6260-slide SDK | Physical wins |
| Gallery entry | Photos / Music & videos / All content chooser | Different older Gallery model | Physical wins |
| Calculator softkeys | Options / Exit | Options / Clear in SDK | Physical wins |
| Idle/navigation shortcuts | C2-01-specific, partly pending capture | SDK generations differ | Do not infer from SDK |
| Firmware menu ordering | Physical observations govern | RM-722 EURO-F `menusettings.xml` gives variant order and `labelgrid` | Use structure/assets; label ordering as inference until physical corroboration |

## Physical evidence still needed

- Complete cold-boot and idle-screen sequence, including status indicators.
- Every idle arrow-key destination.
- Full top-level and nested menu traversal from factory state.
- Gallery folders and media-type chooser, including empty and populated states.
- Countdown timer, interval timer and alarm firing/snooze flows.
- Camera, video recorder, radio, voice recorder, equaliser and Maps key-by-key flows.
- Browser Home, bookmarks, address entry, loading, errors and Back history.
- Applications/Games launch, permission prompts, Options and exit behavior.
- Theme application transition and all Black-theme chrome states.
- Physical screenshots at native 240x320 for pixel-diff baselines where possible.

## Phase 1 baseline decision

The first shell uses only original Black theme artwork for the native-size 240x320 LCD canvas: `menu-screen_240x320.png`, `status_area_240x46.png`, `softkey_area_240x38.png`, `softkey_left/center/right_80x38.png`, `grid_menu_select_74x79.png` for the firmware-configured `labelgrid`, and the native softkey pieces. It does not claim Nokia font fidelity. Behavior is deliberately shallow until direct evidence exists.


## v0.2 implementation reconciliation

The live main menu now follows the enabled `mainmenu` entries in the supplied `menusettings.xml`, in order: Organiser, Contacts, E-mail, Browser, Messaging, Gallery/content, Store, Media, Applications, Settings, Log. This order remains labelled RM-722/059F5P7 EURO-F inference and will yield to physical RM-721 evidence. Exact original E-mail, Nokia Browser and Store icons are used because those entries have matched firmware app packages. Native system-menu icons are neutral placeholders, not invented Nokia graphics, until MCU/PPM extraction proves them.

## v0.3 native rendering and control audit

Black `theme.xml` names `grid_menu_select_74x79.png` directly for the grid-menu selected background but provides no crop rule. v0.3 therefore renders that selector at its native 74x79 pixels and lets it extend behind the 62-pixel cell while clipping only at the grid viewport. Matched app icons render at their natural dimensions: E-mail 48x48, Nokia Browser 46x48, Store 42x47. The on-screen navigation ring has explicit pointer targets for Up, Down, Left, Right and OK. Six native system-menu icons (Organiser, Contacts, Messaging, Gallery, Media, Applications) were recovered byte-for-byte from `rm721__11.40.ppm_f` and render at their native 43x43 pixels. They are exact for v11.40 EURO-F; physical handset evidence remains authoritative. Settings and Log use positively identified 43x43 PPM icons.

## v0.4 PPM native menu icons

Six menu icons recovered byte-for-byte from `rm721__11.40.ppm_f` now replace neutral letters: Organiser, Contacts, Messaging, Gallery, Media and Applications. All are RGBA PNG, 43x43, rendered at native dimensions. Their authority is v11.40 EURO-F firmware evidence; a conflicting physical RM-721 capture wins. Candidate alternates in the extraction package were not used. Settings and Log remain neutral pending a positive icon-to-menu binding.

## v0.5 Settings and Log binding

Settings and Log use byte-exact 43x43 RGBA PNGs recovered from the v11.40 EURO-F PPM. Settings is the wrench at PPM offset `0x00297462`; Log is the green-down/blue-up arrows at `0x00296e52`. The semantic binding is supported by their coherent main-menu icon-table run (Contacts -> Log -> Settings -> Applications), the emulator visuals, and `menusettings.xml` entities. This is strong firmware/emulator evidence, still subordinate to a conflicting physical RM-721 capture.

## v0.6 selector geometry and Phase 2 entry

Neither Black `theme.xml` nor the supplied configs declare an offset or crop for `grid_menu_select_74x79.png`. Its 79-pixel height is fully opaque across that height. The menu content band between the 45/46-pixel status area and 38-pixel softkey area is 237 pixels, exactly three 79-pixel cells. v0.6 therefore removes the separate 24-pixel HTML menu title, places Menu/count in the status line, and uses three native 79-pixel rows. This fits the native selector without overlap or scaling. This is firmware/theme geometry evidence, subject to physical RM-721 correction.

The `softkey_left/center/right_80x38.png` filenames describe their slot, but the decoded members are 80x37. `theme.xml` binds them to each softkey position without a stretch rule. v0.6 renders the pieces at 80x37 over the 240x38 softkey-area background, leaving one background pixel rather than stretching.

Phase 2 navigation begins with D-pad/keyboard movement, page-aware status/count, OK/Select opening a visible evidence-labelled shallow screen for every main-menu entry, and Back returning to the selected grid item. These are navigation scaffolds, not claims about deep physical behavior.

## v0.7 physical grid correction

Physical Nokia C2-01 screenshots published in GSMArena's 18 March 2011 review supersede the v0.6 arithmetic-only interpretation: https://www.gsmarena.com/nokia_c2_01-review-579p3.php and direct screenshot https://fdn.gsmarena.com/vv/reviewsimg/nokia-c2-01/sshots/gsmarena_008.jpg. The 360x480 physical capture (1.5x the 240x320 LCD) shows Menu in the top/status band and a 3x3 labelled grid. Its selected Messaging background occupies about 89-93 captured pixels vertically, about 59-62 logical pixels, and does not overlap the row below. Black `theme.xml` supplies a 74x79 selector without runtime geometry. v0.7 uses 62-pixel cells and clips the native selector inside each cell without rescaling it. This is a measurement from review imagery, not a claim of pixel-exact physical calibration; Moti's own capture wins if it differs.

The same screenshot's Options menu proves `Main menu view >` and `Organise`; v0.7 adds that shallow list. Screenshot 009 proves the Main menu view choices Single, List, Grid, Grid with labels.

Sparse page navigation is not visible in available physical captures. v0.7 removes modulo-11 jumps and clamps/toggles within the two-item sparse page as a conservative scaffold pending physical evidence. This behavior is labelled pending, not parity.

OrganizerMenu in supplied `menusettings.xml` contains Alarm clock, Calendar, Maps, To-do list, Notes, Java Calculator, Countdown timer, Stopwatch and Dictionary. v0.7 shows all nine in the shallow evidence screen.

## v0.8 review-variant and overlay evidence

The GSMArena physical review unit's grid order is Calendar, Contacts, Mail, Internet, Messaging, Photos, Store, Music, Games. The supplied RM-722/059F5P7 `menusettings.xml` target is Organiser, Contacts, E-mail, Browser, Messaging, Gallery/content, Store, Media, Applications, Settings, Log. This is recorded as a product-code/theme/variant disagreement, not averaged: the build continues to follow its labelled supplied firmware target until Moti's RM-721 handset arbitrates.

Physical screenshot 009 shows the Main menu Options overlay extending through the normal softkey zone and drawing its own blue Select/Back strip. v0.8 follows that overlay structure and renders the physically visible radio-button choices: Single, List, Grid, Grid with labels. The physical review unit's green selector belongs to its default theme; this build intentionally uses the supplied Black theme selector. That colour difference is not treated as a parity defect.

The physical grid top band shows Menu and time but no positional `1/11` counter, so v0.8 removes the counter.

## v0.9 software and hardware separation contract

Owner architecture direction: the 240x320 LCD software is a self-contained module; the outer phone shell and full keypad are a separate hardware/controller module. The controller emits semantic key events and the screen reacts. v0.9 implements this separation as `screen.js` and `controller.js`, with a complete test keypad: left/right softkeys, navigation directions, OK, call/end, and 1-9/*/0/#. The hardware geometry is an initial testing scaffold pending direct front-on RM-721 keypad measurements; its behavior and module boundary are the current milestone.

## v0.10 front-face keypad geometry

The v0.10 controller geometry is redrawn against a front-on physical C2-01 photograph hosted by Wikimedia Commons and corroborated by independent TechRadar, PhoneArena, GSMArena and CNET review/product imagery. The physical face uses a compact three-part control panel: softkey bars at the upper outer corners; a tall, silver-edged rounded-square navigation/OK assembly at center; call/end keys below the softkeys and beside the navigation key. The twelve number keys form a tight, nearly gapless 3x4 deck rather than floating pill buttons. v0.10 follows those proportions while retaining separate hit targets for testability.

The strongest front-on reference is https://commons.wikimedia.org/wiki/File:Nokia_C2-01.JPG (original 1920x2560). Corroborating pages: https://www.techradar.com/reviews/phones/mobile-phones/nokia-c2-01-936316/review/10 ; https://www.phonearena.com/reviews/Nokia-C2-01-Review_id2723 ; https://www.gsmarena.com/nokia_c2_01-3638.php ; https://www.cnet.com/reviews/nokia-c2-01-review/ . Moti's own handset photo will override this review/reference geometry when supplied.

Numeric direct-selection shortcuts, star/hash page movement, call-to-Log and End-to-home are test-scaffold behavior only. They are not asserted as physical C2-01/S40 semantics. The on-page trace is visibly prefixed `TEST SCAFFOLD` to maintain that boundary.

## v0.11 no-dead-keys contract

Owner rule: no dead keys. Every controller key in every software state must create a visible response. An evidenced route executes normally. A test shortcut stays explicitly labelled as such. Where physical/S40 behavior or screen depth is not yet evidenced, the software shows an honest visible `not evidenced` response rather than silently doing nothing. v0.11 implements this in the software module with a numbered `TEST` key-response strip, distinct from the hardware controller trace. Repeated presses increment the response number and visibly pulse, so a repeated key cannot masquerade as a dead press.

## v0.12 menu coverage priority

Owner scope: Ground-Up is a full UI reference for future projects, with menu coverage as the first priority. Dead Ovi/web services and executable Java apps are not blockers; their visible surfaces remain honest reference stubs. v0.12 converts every enabled main-menu entry into a navigable list. Organiser, Contacts, Browser, Messaging, Gallery, Media, Applications, Settings and Log lists are transcribed in order from the supplied RM-722/059F5P7 `menusettings.xml`. E-mail and Store are native-link Java/service entries in that firmware and are labelled reference-only. List selection works with Up/Down; Open visibly names the selected route as not yet implemented, maintaining the no-dead-keys rule.

## v0.13 evidenced main-menu views

Physical screenshot 009 exposes the Main menu view choices Single, List, Grid, and Grid with labels. v0.13 implements all four as actual menu presentations rather than placeholder app screens. Single shows one large icon and label; List shows eight compact icon/label rows; Grid uses the 3x3 icon geometry without labels; Grid with labels preserves the original 3x3 label grid. The same menu data, selector, open route, no-dead-key feedback and hardware controller drive every view. Long first-submenu lists now scroll the selected row into view.

## 9 AM audit interpretation and end state

A visible diagnostic response is not evidence of a correct functional route. Replay reports must count these separately: `functional route` means the requested state/navigation change occurred; `diagnostic-only` means the numbered test strip acknowledged a key whose real behavior remains unbuilt or unevidenced. Zero dead presses therefore establishes input observability, not full UI fidelity.

The TEST strip is temporary instrumentation. Release end state: it moves outside the 240x320 product LCD or is hidden behind an explicit diagnostic mode once all routes are implemented and audited. It stays visible during this construction phase.

Only Grid with labels has measured physical C2-01 geometry. Single/List/Grid exist physically as choices in screenshot 009, but their v0.13 presentation geometry remains unverified pending physical captures. Numeric, star/hash, Call and End routes remain test shortcuts. E-mail/Store are reference-only and their JAD/application details UI is unbuilt.

## v0.14 JAD application identity UI

Applications > Applications now opens a navigable 19-entry installed-application reference generated from the preserved JAD descriptors. Each row shows exact MIDlet name and version; Details shows vendor and descriptor filename and explicitly states that executable Java UI is outside current scope. This supplies firmware-grounded identity coverage without pretending to run Java. It includes E-mail 1.3.53, Ovi Store 2.4.0, OviBrowser 1.0.1, Operette 4.2.55, Nokia apps and supplied games. Back returns to the Applications first submenu. Diagnostic acknowledgement and functional state transitions remain separately auditable.

## v0.15 catalog transition correction and replay rule

The 10 AM audit identified that a visible diagnostic can mask a missing functional state transition. v0.15 makes catalog movement a dedicated `moveCatalog(delta)` state transition, records before/after indices in the visible response, gives every catalog row a stable audit index, and constrains the catalog list to a scrolling region above the softkey bar. Selected rows scroll into that region. Acceptance tests must assert `catalogSel` and the selected row actually change and that the selected row's bounds remain inside the list viewport; a changing diagnostic strip alone does not pass.

## v0.16 catalog Options, metadata bounds and observable state

Catalog Options is now a functional three-row reference menu: Application details, Descriptor source, and Java scope. Each selection closes Options and changes the fixed metadata panel using the selected JAD record. These are UI-reference actions, not a claim about original S40 catalog Options wording. The metadata panel is fixed at 46px with anywhere-wrapping and hidden overflow, so long vendor/descriptor strings cannot steal list viewport height or overlap softkeys.

For transition-bound auditing, every render writes a machine-readable snapshot to `lcd.dataset.uiState`: view, main selection, submenu selection, catalog selection, menu mode, Options open state, and Options selection. This is diagnostic observability only and does not change product behavior. Tests can now bind a verified pre-state to the expected post-state instead of inferring state from a diagnostic message.

## v0.17 frozen-quality-bar visual pass

Owner feedback set the frozen C2 Reborn root as the visual quality bar while Ground-Up keeps its separate architecture and broader evidence ledger. v0.17 studies that live frozen build without modifying it: layered silver side rails, narrow earpiece, C2/NOKIA face treatment, darker recessed LCD bezel, tighter controller panel, silver navigation surround, glossy call/end keys, compact near-black key deck, cyan legends, and stronger depth/shadows. Ground-Up retains its exact 240x320 software content box, original Black theme artwork, module separation, menu coverage, and audit instrumentation. This is visual convergence, not source inheritance; root stays byte-identical.

## v0.18 first-submenu depth surfaces

Owner clarified that a diagnostic acknowledgement is still a dead option. v0.18 replaces the 93 first-submenu `not implemented` endpoints with functional UI-reference surfaces. Every first-submenu row now opens a bounded screen with a route-specific description and four navigable controls chosen by grounded category (organiser, contacts, messaging, settings, media, gallery/apps, logs, browser/services). Up/Down changes control selection; Select toggles a visible Ready/Active state; Back returns to the exact parent list; Options opens About/Reset and Reset clears local test state. These are explicitly UI-reference surfaces, not claims that backend services, personal data, Java execution, media hardware, or physical per-screen geometry are implemented.

## Offline backend target

Owner direction: recreate backend behavior too, aiming for a proper Nokia phone that is simply not connected to the network. Hardware-dependent technology may remain unavailable until after the entire phone/UI is set up. Backend work follows menu coverage: local persistence and Nokia-like state transitions for profiles/settings, time/alarm, organiser data, contacts, messaging, call logs, gallery/media metadata and UI state. Network-backed and hardware-backed features must show honest offline/unavailable states, not silently fail. This expands the target beyond UI reference while preserving evidence labels: implemented behavior must still be distinguished from physical/Nokia-verified behavior and scaffolding.

## Owner scope ordering: experience assets before optional runtimes

The complete offline-phone target includes sounds, tones, wallpapers, themes and behavior. Working web access is not important. Java game/runtime support is explicitly optional and unimportant relative to phone setup; leave web and games until last and ask the owner before starting that part. The 57 AAC tones, four supplied themes and their wallpapers/assets are therefore first-class upcoming implementation sources. JAD/JAR packages remain catalogued evidence, not an instruction to build a runtime.

## v0.19 endpoint-specific Nokia reference surfaces

The 12 PM audit correctly distinguished category templates from authentic endpoint depth. v0.19 replaces generic content on priority Organiser, Settings, Messaging, Media, Log and Browser endpoints with per-screen models mined from the frozen root, which itself was built from physical/SDK evidence. Examples: Alarm 07:00/Off/Repeat/Tone; Calendar Today/Make note/Week/Date; Calculator Standard/Scientific/Loan; Profiles General/Silent/Meeting/Outdoor; Tones and Display setting rows; Create message types; camera Capture/Self-timer/Effects; radio station controls; stopwatch/countdown time faces; and explicit offline browser/address states. Visual kinds add time faces, media-preview surfaces, message rows and offline panels. Remaining non-priority endpoints use category models and stay identified as UI-reference behavior rather than physically verified geometry.

## v0.20 provenance correction and real action routes

Frozen C2 Reborn is a discovery lead, not primary evidence. Every v0.19 row/control first found there is marked **unverified frozen-source lead** unless separately matched below. Already supported independently: main/first-submenu structure from supplied `menusettings.xml`; theme geometry/artwork from supplied NTH files; Grid-with-labels and Main menu view dialog from GSMArena physical screenshots; native Calculator and Themes findings in frozen comments that cite live SDK capture remain emulator leads, not physical proof. Alarm, Calendar, To-do, Notes, Countdown, Stopwatch, Profiles, Tones, Display, Messaging, Camera, Radio, Voice recorder, Log and Browser per-screen rows introduced in v0.19 currently remain unverified frozen-source leads pending handset, emulator, firmware-resource or contemporary-source corroboration. They must not be called Nokia-verified.

v0.20 replaces the generic toggle on three high-value actions with real stateful routes: Alarm time opens an editor whose hour changes with Up/Down and saves locally; Camera Capture opens a captured-reference result (explicitly no camera hardware); Go to address/Address opens an entry screen where number keys append and Select confirms offline. Pre/post state exposes `actionType` and `actionValue`. Other controls retain temporary local toggles until their actions are built. Endpoint Left/Right remains an evidence gap; diagnostic response is kept and is not counted as functional fidelity.

## v0.21 offline backend foundation, tones and themes

A local persistent backend now stores profile, selected supplied theme, ringing tone, volume, alarm and future organiser/contact/message/log collections in browser localStorage. This is implemented offline behavior, not claimed original database format. Tones > Ringing tone opens a real selector over all 57 exact AAC files from the supplied firmware; Up/Down selects, Select persists and attempts local audio preview. Themes > Select theme opens the four supplied NTH identities (Black, Dark, Light, Nokia); selection persists. Alarm save now persists in the same phone state. Exact theme visuals beyond Black remain upcoming; selecting a theme records state without yet hot-swapping every asset.

## v0.22 live theme behavior

Theme selection now changes the actual LCD theme asset set immediately and survives reload. The software swaps seven matched assets from each supplied NTH extraction: menu background, status area, grid selector, softkey area and left/center/right softkey pieces. Only the four supplied identities are accepted: Black, Dark, Light and Nokia. This is directly grounded in the supplied theme packages. The Settings > Themes lead reads the persisted active theme; Tones and Alarm leads likewise read their stored backend values.

## v0.23 profiles and ring-volume backend

Profiles is now functional offline state: selecting any displayed profile opens activation, Up/Down traverses all seven frozen-source profile leads, Select persists the active profile and the Profiles screen reads it back. Tones > Ring volume opens a seven-step meter; Up/Down changes the level and Select persists it. The profile names remain unverified frozen-source leads pending independent provenance; persistence and state behavior are Ground-Up implementation, not Nokia database claims.

## v0.24 address persistence and observable audio preview

Address Save now writes to `phoneState.addressHistory` (deduplicated, newest first, capped at 20) before localStorage persistence; the confirmation explicitly says offline address. The action editor no longer repeats the page heading, preventing the address field/help from clipping under the TEST strip. Tone preview now has visible states: not started, loading, playing, blocked (press Select again), or unavailable. Browser playback compatibility is reported from `playing`, `error`, and rejected `play()` signals instead of failing silently. The exact supplied AAC is retained; no transcoding is claimed yet.

## v0.25 local contacts backend

Contacts > Add new contact and Names > Add now open a real two-field local editor. The prototype generates a neutral local name (`Contact N`) and accepts a number from hardware number keys; Select stores `{name, number}` in `phoneState.contacts` (capped at 100) and persists it. Names reads the stored contact list back. No personal or synced records are used. This is a functional offline backend slice, but automatic placeholder naming is Ground-Up test behavior, not a Nokia-authentic text-entry claim; T9/name editing remains future work.

## v0.26 local message drafts backend

Messaging > Create message and any endpoint control labelled Create message now open a working offline draft editor. Number keys enter a recipient number; Select stores a timestamped local draft with a fixed test body in `phoneState.messages`, capped at 100, and persists it. Inbox and Drafts report the stored local counts. Nothing is transmitted. Recipient digit entry and persistence are functional, while the fixed body and lack of S40 text composition are explicitly prototype behavior pending a proper text-entry engine.

## v0.27 offline dialler and call-log backend

The green Call key now opens a functional offline dialler from any non-dialler state. Number keys enter a number; Call or the centre Call softkey records an `{number, status: offline attempt, createdAt}` entry in local `phoneState.callLog`, capped at 100. All calls and Dialled numbers read the stored log back, including after reload. No network call is placed and the UI says offline attempt. This replaces the prior generic Call-key shortcut to Log with an actual local state transition.

## v0.28 persistent local Notes slice

Organiser > Notes > Make a note now opens a functional offline note editor. Number keys supply temporary test text; Select stores a timestamped record in `phoneState.notes`, capped at 100 and persisted. Reopening Notes reads the local note count. This removes another generic Ready/Active toggle, while clearly avoiding a false claim of Nokia T9 fidelity: proper multi-tap/T9 composition remains required before authentic free-text behavior can be claimed.

## v0.29 working offline calculator

Organiser > Calculator now opens a real local arithmetic surface rather than toggling Ready/Active. Hardware digits build operands, `*` inserts addition, and centre Select computes the sum without `eval`. Repeated use stays in the calculator and its screen state is exposed through the existing diagnostic state. Addition is deliberately the first bounded operation; scientific/loan calculator rows remain UI-reference endpoints pending deeper evidence.

## v0.30 working offline stopwatch

Organiser > Stopwatch now opens a live local stopwatch. Centre Select starts and stops a 100 ms display refresh, `*` resets while stopped, and Back safely stops the interval while retaining elapsed time in the current runtime. Time formatting is calculated from elapsed milliseconds. No generic Ready/Active state stands in for timing behavior. Persistence across reload is not claimed.

## v0.31 working offline countdown timer

Organiser > Countdown timer now opens a real local countdown. While stopped, Up/Down adjusts the duration in one-minute steps; Select starts/stops, `*` resets to one minute, and completion emits a visible Timer result. Back stops the running interval and retains the remaining runtime duration. The timer is runtime-local and reload persistence is not claimed.

## v0.32 persistent local Calendar notes

Organiser > Calendar > Make a note now opens a functional local date editor. Up/Down changes the day relative to today; Select stores an ISO-date record with an explicit offline test note in `phoneState.calendar`, capped at 100 and persisted. Calendar reads the saved count after reload. The fixed note text is prototype behavior; authentic Nokia note-type and text-entry flows remain to be built.

## v0.33 persistent local To-do notes

Organiser > To-do list > Add now opens a local task editor. Up/Down changes the explicit test task number; Select stores `{body, done:false, createdAt}` in `phoneState.todos`, capped at 100 and persisted. To-do list reads the saved count after reload. Placeholder task naming is Ground-Up test behavior pending the common text-entry engine.

## v0.34 confirmed local clear/delete actions

Four destructive menu endpoints now operate on the matching local backend collections instead of toggling: Contacts > Delete all contacts, Messaging > Delete messages, Browser > Clear cache (local address history), and Log > Clear log lists. Each opens a confirmation surface showing the local record count; centre Select clears and persists, while Back cancels. No external or personal source is touched.

## v0.35 complete local Alarm clock state

Alarm clock now exposes and persists separate enabled state and time. Selecting `Alarm: Off/On` toggles it immediately and updates the live lead. Alarm time opens with the stored value instead of resetting to 07:00; Up/Down adjust hours and Left/Right adjust minutes in five-minute steps. Select persists the edited time. No real-time notification firing is claimed yet.

## v0.36 persistent Date and time preferences

Settings > Date and time now renders the live local clock in the selected 12/24-hour format. Date & time format opens a real choice and persists it; Auto-update toggles and persists an explicit local preference. No carrier/network time synchronization is performed or claimed. Time zone and manual date editing remain reference rows pending deeper implementation.

## v0.37 persistent Display settings

Settings > Display now reads local display state. Home screen toggles and persists; Font colour opens and persists Automatic/White/Black/Blue choices; Main menu view opens the already working four-mode view dialog directly. Wallpaper remains a reference endpoint because applying supplied wallpaper evidence still needs its own provenance pass. Font-colour state is stored and shown, but full palette application is not yet claimed.

## v0.38 persistent Main menu view

The existing physical-reference four-mode Main menu view selector now stores its selection in `phoneState.menuMode` and restores it on reload. This closes the state gap between Display > Main menu view and the top-level Options route: both mutate the same persisted setting. Menu content and geometry are unchanged.

## v0.39 calculator subtraction

The local calculator now supports chained subtraction through `#` as well as chained addition through `*`. Select tokenizes signed integer terms and reduces them without `eval`. Invalid trailing operators are prevented. This deepens the bounded standard calculator while scientific and loan modes remain reference rows.

## v0.40 confirmed Restore factory settings

Settings > Restore factory settings now opens an explicit confirmation and restores only phone preferences to Ground-Up defaults: profile, theme, tone/volume, alarm, clock, display and main-menu view. Locally stored contacts, notes, to-dos, drafts, calendar notes, call log and address history are retained and the UI says so before confirmation. Select applies/persists the reset; Back cancels. A separate delete-personal-data flow is not inferred.

## v0.41 visible font-colour application

The v0.37 Display > Font colour preference now changes the rendered LCD text palette immediately and after reload. White, Black and Blue apply explicit colour tokens; Automatic leaves theme CSS in control. Restore factory settings reapplies Automatic. This closes the prior stored-only caveat without changing theme assets.

## v0.42 supplied wallpaper selector

Settings > Display > Wallpaper now selects and persists Theme default, Analog clock, or Menu background. The latter two use images from the active supplied `.nth` theme extraction (`analog_clock_background_240x320.png` and the theme-specific menu/background file); changing theme refreshes the wallpaper path. The selection applies to the LCD layer and factory reset returns Theme default. No external artwork is introduced.

## v0.43 functional local Lights control

Settings > Lights now exposes a five-step Display light control. Up/Down changes the level, Select persists it and applies bounded LCD brightness filters; Restore default returns level 3. This is explicit Ground-Up local behavior because the firmware route provides the endpoint but no physical brightness scale has yet been captured. Keypad light and notifications remain reference rows.

## v0.44 source-integrity repair: action movement dispatcher

Audit found movement statements accidentally concatenated into the action-render chain, creating unreachable duplicate branches for lights, wallpaper, font colour, time format and to-do. Those branches are removed. All directional action changes now live in one named `handleActionArrow(key)` dispatcher; render branches only render and save branches only save. Each ordinary action type now has one render test, one movement test where applicable, and one save test. `node --check` passes and grep counts are recorded during build. No new endpoint behavior is added in this repair release.

## v0.45 source modularization: action renderer

Action markup is removed from the large `draw()` conditional and placed in one named `renderAction()` function with a switch keyed by action type. A shared `box()` template handles editor structure; each case owns only its body and help text. `draw()` now assigns `submenuList.innerHTML=renderAction()` and sets screen chrome. This follows v0.44's separated movement dispatcher and makes render, movement and save logic independently inspectable. No endpoint behavior is added.

## v0.46 source modularization: action save/activation

The action mutation chain is removed from `handleHardwareKey()` and split into `saveAction()`, `activateTimedAction()`, `previewTone()` and the shared `finishAction()` commit/return helper. Key dispatch now calls one action API. Timers remain runtime-only and do not call the persistence helper; settings and collections do. Tone media event handling is separately inspectable. Together with v0.44-v0.45, action rendering, directional movement, activation/persistence and media preview now have distinct boundaries. No endpoint behavior is added.

## v0.47 persistent Equaliser presets

Media > Equaliser now exposes a working local preset selector instead of Ready/Active toggles. Up/Down cycles Normal, Pop, Rock and Jazz; Select stores the active preset in `phoneState.equaliser`, and reopening/reloading reads it back. The preset is stateful UI/backend behavior only: audio frequency processing is not claimed.

## v0.48 persistent offline FM frequency control

Media > Radio now shows a locally stored FM frequency and an explicit offline state. Set frequency opens a tuner; Up/Down changes by 0.1 MHz and wraps inside the common 87.5–108.0 MHz range; Select persists it. No tuner hardware, audio stream, headset antenna detection, or station scan is claimed. Those rows remain UI references.

## v0.49 persistent Security preferences

Settings > Security now reads local security state. PIN code request toggles and persists; Security level selects None, Memory or Phone and persists. These are explicit offline preference models only: no secret PIN is requested or stored, no lock screen is enforced, and no SIM/security hardware behavior is claimed. Access codes and Certificates remain reference rows.

## v0.50 persistent offline Bluetooth preference

Settings > Connectivity now reports explicit offline state and a local Bluetooth On/Off preference. Selecting the Bluetooth row toggles/persists it and updates the lead. No browser Bluetooth permission, radio discovery, pairing, file transfer, or network state is claimed. Packet data, USB data cable and Network status remain reference rows until real offline simulations can be bounded.

## v0.51 persistent offline Packet data preference

Connectivity > Packet data now selects and persists When needed, Always online or Off, while the Connectivity lead remains explicit that this recreation is offline. The preference does not open a network socket, contact an operator, or claim cellular data behavior. This replaces a generic toggle with bounded local settings behavior.

## v0.52 persistent offline USB data cable mode

Connectivity > USB data cable now selects and persists Ask on connection, PC Suite or Mass storage as a local preference. No USB device API, mount, PC Suite session or file transfer is invoked or claimed. The endpoint now has bounded phone-settings behavior while Connectivity remains explicitly offline.

## v0.53 shared-keypad multi-tap text entry begins

Organiser > Notes now uses a local multi-tap text composer rather than storing literal test digits. Keys follow the labels printed on the supplied controller: 2=abc, 3=def, through 9=wxyz; 1 cycles punctuation, 0 inserts a space, and # changes case. Repeating a key within 900 ms cycles its character; a different key commits and begins the next. Select persists the resulting note. This timing and mapping are Ground-Up keypad behavior pending physical C2-01 timing confirmation, not a T9 dictionary claim.

## v0.54 multi-tap contact names

Contacts > Add new contact now has distinct Name and Number fields. Up/Down changes the active field. Number keys use the v0.53 multi-tap composer in Name and literal digits in Number; # changes name case. Select stores the entered name/number pair, using a neutral Contact N fallback only when name is empty. This replaces the forced placeholder-name editor and reuses one keypad text engine.

## v0.55 multi-tap local message bodies

Messaging > Create message now has distinct To and Message fields. Up/Down changes the active field; number keys enter literal recipient digits in To and use the shared multi-tap composer in Message; # changes message case. Select persists the actual composed draft body rather than the previous fixed test string. Nothing is transmitted.

## v0.56 multi-tap To-do text

Organiser > To-do list > Add now uses the shared multi-tap text engine and persists the composed task body instead of generated `Task N` placeholders. Number keys compose, # changes case, and Select stores `{body, done:false, createdAt}`. To-do completion toggling remains future work; this release improves entry authenticity and backend content.

## v0.57 multi-tap Calendar note text

Calendar > Make a note now has Date and Note fields. Left/Right changes field; Up/Down changes date only while Date is active; number keys compose note text with the shared multi-tap engine while Note is active, and # changes case. Select persists the selected ISO date and actual composed body instead of a fixed placeholder.

## v0.58 local collection readback and To-do completion

Notes, To-do list, Calendar and Drafts now render their locally stored content in the endpoint lead instead of count-only summaries, allowing replay to verify what was persisted from the screen. To-do list > Open toggles the newest task's `done` state and persists it when a task exists; the lead marks open/completed with ○/✓. Add still opens multi-tap entry. Large-collection pagination remains future work.

## v0.59 selectable local Notes and To-do lists

Notes and To-do list now render each stored record as its own selectable detail row rather than joining all content into one lead line. Up/Down uses existing detail navigation. Selecting a note identifies and displays that exact local note; selecting any to-do toggles that row's done state, not only the newest. Make a note/Add remain appended action rows. This removes the first-record-only limitation; edit/delete per item and pagination remain.

## v0.60 selectable Calendar and Draft lists

Calendar and Drafts now render each local record as an individual selectable detail row with Make a note/Create message appended. Selecting a calendar row displays its exact date/body; selecting a draft displays its recipient/body. Selecting the appended row opens the existing editor. This replaces joined lead text and makes persisted records auditable from the handset UI. Per-record edit/delete and pagination remain.

## v0.61 selectable Contacts list

Contacts > Names now renders each local contact as its own row with Add appended. Selecting a contact displays its exact name and number; selecting Add opens the existing multi-tap contact editor. This replaces joined lead text and makes contact persistence auditable from the handset. Per-contact call/edit/delete and pagination remain.

## v0.62 selectable local Call log

Log > All calls and Dialled numbers now render each local offline call attempt as its own row with Clear list appended. Selecting a call displays its number, offline-attempt status and local timestamp. Clear list opens the existing confirmation rather than a generic toggle. This makes call-log persistence and timestamps auditable from the handset; callback/edit-number flows remain.

## v0.63 selectable offline address history

Browser > Last web address now renders each locally confirmed offline address as a selectable row with Clear history appended. Selecting a row displays the exact stored address without contacting it; Clear history uses the existing confirmation. This makes Go to address persistence handset-auditable while working web remains intentionally deferred until the owner gate.

## v0.64 contact-to-dialler route

While a stored Contacts > Names row is selected, the green Call key now opens the offline dialler prefilled with that contact's number. Pressing Call again records the existing offline call attempt. Contacts without a number fall back to the blank dialler. This connects two existing local backend surfaces without placing a network call or claiming a handset-exact shortcut.

## v0.65 per-contact delete confirmation

On a stored Contacts > Names row, the left softkey now opens a Delete contact confirmation showing the exact selected name and number. Centre Select removes that indexed local contact and persists; Back cancels. This replaces generic screen Options for the selected-record state and gives the local Contacts backend per-record deletion. The shortcut and wording are Ground-Up choices pending physical menu capture.

## v0.66 per-record delete confirmations

Stored Notes, To-do list, Calendar and Draft rows now use the selected-row left softkey for an exact-item delete confirmation. The confirmation displays the selected content; Select removes the indexed local record and persists, while Back cancels. This extends v0.65's bounded delete model across the local organiser and messaging collections. Shortcut wording remains Ground-Up pending physical capture.

## v0.67 per-note editing

Selecting a stored Notes row now opens an editor prefilled with that exact note. Multi-tap number keys append or cycle text, # changes case, and * deletes the last character. Select replaces the indexed local note body and persists it; Back cancels by leaving stored state untouched. Left softkey on the row still opens delete confirmation.

## v0.68 per-contact editing

Selecting a stored Contacts > Names row now opens an editor prefilled with that exact name and number. Up/Down changes field; Name uses the shared multi-tap engine and Number uses literal digits; # changes name case and * deletes from the active field. Select replaces the indexed contact and persists; Back cancels. Green Call from the list and left-softkey Delete remain separate routes.

## v0.69 per-draft editing

Selecting a stored Drafts row now opens an editor prefilled with its exact recipient and message. Up/Down changes field; To uses literal digits and Message uses shared multi-tap; # changes message case and * deletes from the active field. Select updates the original indexed draft and persists; Back cancels. Left-softkey per-draft deletion remains separate.

## v0.70 per-calendar-note editing

Selecting a stored Calendar row opens an editor prefilled with its exact ISO date and note body. Left/Right changes Date/Note field; Up/Down changes date while Date is active; Note uses shared multi-tap, # changes case, and * deletes. Select replaces the indexed calendar note and persists; Back cancels. Left-softkey deletion remains separate.

## v0.71 per-To-do editing and separate completion

Selecting a stored To-do row now opens a prefilled body editor. Multi-tap edits, # changes case, * deletes, Select persists and Back cancels. Completion is separated from editing: on a stored To-do row, the green Call key toggles Open/Completed and persists. This gives both operations distinct observable routes. The green-key completion shortcut is Ground-Up pending physical options capture.

## v0.72 live local counters

Applications > Memory status, Log > Message counter and Log > Call duration now read the local backend rather than generic Ready/Active rows. Memory status reports stored Contacts, Messages, Notes and Calendar record counts. Message counter reports local Draft/Sent/Received counts. Call duration explicitly says offline calls are not connected, keeps durations at 00:00, and reports dialled/all attempt counts. No byte-accurate storage or network duration is inferred.

## v0.73 local Draft-to-Sent transition

On a selected Draft row, the green Call key opens a confirmation displaying its exact recipient/body. Select changes only the local message status from draft to sent, adds `sentAt`, persists, and makes the record appear under Sent items; Back cancels. The screen says `Send message offline?` and `moves to Sent items locally`: no SMS/network transmission is performed or implied. This is a backend state simulation pending real radio/service work.

## v0.74 selectable and deletable Sent items

Sent items rows now open their exact recipient, body and local sent timestamp. Left softkey opens exact-message deletion for both Drafts and Sent items. The deletion mapping now resolves each filtered row back to its original `phoneState.messages` index before mutation, fixing a latent wrong-record risk when draft and sent statuses are interleaved. Select/Back confirmation behavior is unchanged.

## v0.75 persistent Phone preferences

Settings > Phone now reads local Language and Flight query state. Language selects English, French, German or Spanish and persists; only the preference/lead changes, and full UI localization is not claimed. Flight query toggles and persists a local mode label but does not control radios. Welcome note and Network mode remain reference rows.

## v0.76 persistent Call preferences

Settings > Call now exposes bounded local Anykey answer and Automatic redial toggles, both persisted and reflected in the rows. Because the recreation never receives or connects a network call, the settings do not trigger call behavior and the lead says Offline call preferences. Speed dialling and Call waiting remain reference rows.

## v0.77 persistent Accessories preference

Settings > Accessories now selects and persists a Default accessory preference: No accessory, Headset, Handsfree or TTY. This is explicit local configuration only; no browser device detection, audio routing or hardware attachment is claimed. Individual Headset/Handsfree/TTY configuration rows remain reference surfaces.

## v0.78 persistent Welcome note

Settings > Phone > Welcome note now opens a prefilled multi-tap editor. Number keys compose, # changes case, * deletes, Select persists and Back cancels. An empty note is shown as Off. The note is local state and is not yet rendered in a startup/power-on sequence because power cycling remains a test scaffold.

## v0.79 persistent offline Network mode preference

Settings > Phone > Network mode now selects and persists Dual mode, GSM or 3G. This is a local preference only: Connectivity continues to say Offline, and no modem, operator selection or browser networking is changed. The values follow the RM-722/059F5P7 route context; physical C2-01 wording remains authoritative if later capture disagrees.

## v0.80 complete bounded Call preference rows

Settings > Call now gives Speed dialling and Call waiting the same local persisted On/Off behavior as Anykey answer and Automatic redial. The lead remains Offline call preferences: these switches do not affect a modem or connected call. All four visible Call rows are now stateful rather than generic toggles.

## v0.81 local Speed dial assignments

Contacts > Speed dials now exposes keys 2–5 as local assignment rows. Selecting a key opens the stored Contacts list; Up/Down chooses a contact and Select stores that contact's number in `phoneState.speedDials`. Reopening/reloading shows the assignment. Long-press dialing and keys 6–9 remain to be added; no network call is made.

## v0.82 complete Speed dial keys and dialler route

Contacts > Speed dials now exposes all assignable number keys 2–9. Assignment behavior remains contact-backed and persisted. On an assigned row, green Call opens the offline dialler prefilled with that number; Call again records the offline attempt. Empty rows report empty. Long-press from the main screen is not inferred.

## v0.83 local Caller group assignment

Contacts > Caller groups now reports counts for Family, Friends, Business and Other. Selecting a group opens the stored Contacts list; Up/Down selects a contact and Select stores that contact's group and updates counts. This is bounded local organization behavior. Group tones/images, unassignment and physical wording remain future work.

## v0.84 caller-group readback and removal

Contacts > Names rows now show each stored contact's assigned caller group. Caller groups adds Remove group: select it, choose a contact and Select to delete that contact's local group assignment. Existing group assignment remains single-group per contact and moving a contact between groups updates counts. Group membership is now directly auditable and reversible from the handset.

## v0.85 reversible Speed dial assignments

On an assigned Contacts > Speed dials row, the left softkey opens a Clear speed dial confirmation showing the exact key and number. Select deletes only that key's local assignment and persists; Back cancels. Empty rows report already empty. Speed dial assignment and offline dialing now have a matching reversible path.

## v0.86 persistent offline Bookmarks

Browser > Bookmarks now renders local saved bookmark rows with Add bookmark appended. Add opens address entry, number keys append to the offline address and Select stores a deduplicated bookmark (50 max). Selecting a bookmark displays it without contact. Working web remains deferred; full alphanumeric URL entry will reuse the text engine later.

## v0.87 per-bookmark delete confirmation

On a stored Browser > Bookmarks row, the left softkey opens a confirmation showing the exact offline bookmark. Select removes only that indexed local bookmark and persists; Back cancels. This makes the v0.86 bookmark collection reversible without contacting any address.

## v0.88 per-call-entry delete confirmation

On a stored Log > All calls or Dialled numbers row, the left softkey opens a confirmation showing the exact number and offline-attempt status. Select deletes only that indexed local call entry and persists; Back cancels. Clear list remains the bulk-delete route.

## v0.89 keypad deletion in numeric/address editors

The `*` key now deletes the last character in Dialler, Go to address and Add bookmark editors. Address and bookmark fields retain the `http://` floor rather than deleting the scheme scaffold. This closes a correction-path gap in those input surfaces. Calculator retains its separate `*` addition behavior, and text editors retain their existing delete behavior where documented.

## v0.90 multi-tap address and bookmark entry

Go to address and Add bookmark now use the shared multi-tap composer, allowing letters and punctuation rather than digits only. `*` deletes while preserving the `http://` floor, and # changes case. This improves offline address fidelity without contacting or loading an address. The input clause was also deduplicated during the change. The keypad mapping/timing keeps the v0.53 Ground-Up disclosure pending physical confirmation.

## v0.91 functional offline idle/home screen

The red End key now returns to a distinct offline idle screen rather than the main menu test scaffold. It shows the live time/date, current profile, local Flight/Offline status, persisted Welcome note and Home screen preference. Centre opens Menu, right softkey opens Names, and left opens an Organiser shortcut. This is Ground-Up idle behavior assembled from existing local state; exact physical idle geometry/softkey bindings still need handset capture.

## v0.92 persistent local reference captures

Media > Camera > Capture now saves a timestamped local reference-capture record in `phoneState.photos` (100 max) instead of showing a transient flash only. Gallery > Photos renders each record plus a Camera route; selecting a record shows its exact name, explicit `reference capture` kind and timestamp. No camera pixels or hardware capture is claimed. This is backend/UI behavior for the unavailable-hardware case.

## v0.93 per-capture delete confirmation

On a stored Gallery > Photos reference-capture row, the left softkey opens a confirmation showing the exact capture name and kind. Select removes only that indexed local record and persists; Back cancels. No image bytes exist or are implied, so deletion concerns only the explicit reference-capture metadata.

## v0.94 Gallery inventory readback

Gallery > Gallery now reports Photos count, four supplied themes and all 57 supplied tones. Gallery > Music and videos reports the supplied-local media inventory without claiming absent music/video files. Applications > Memory status remains the local record counter and is now section-scoped, avoiding an endpoint-name collision. This replaces generic Gallery toggles with source-backed inventory rows.

## v0.95 Gallery inventory cross-navigation

The source-backed Gallery inventory rows now lead to their functional surfaces instead of toggling Ready/Active: Photos opens the local Photos list, Themes opens the supplied theme selector endpoint, and Tones opens the supplied 57-tone endpoint. Music and videos > Tones uses the same route. This links the inventory without duplicating backend state or inventing media.

## v0.96 persistent Voice recorder reference metadata

Media > Voice recorder > Record now opens a live local duration timer. First Select starts; second Select stops and stores name, duration, explicit `reference recording` kind and timestamp in `phoneState.recordings`. Reopening lists each record and its duration. No microphone permission, audio bytes or real recording is claimed; this is unavailable-hardware backend/UI behavior matching the Camera reference-capture pattern.

## v0.97 per-reference-recording deletion

On a stored Voice recorder row, the left softkey opens a confirmation showing the exact reference recording name and duration. Select removes only that indexed metadata record and persists; Back cancels. As in v0.96, no audio bytes exist or are implied.

## v0.98 persistent Alarm tone with preview

Alarm clock > Alarm tone now displays the stored alarm tone and opens the full supplied 57-tone selector. Up/Down chooses, Select stores `phoneState.alarmTone`, and preview uses the existing observable loading/playing/blocked/unavailable media-event path without changing the ringing tone. Alarm firing itself remains unimplemented and unclaimed.

## v0.99 STOP-SHIP load repair

The static `endpointModels.Connectivity` object no longer evaluates `phoneState.usbMode` during module initialization. That label remains correctly computed lazily inside `detailModel()` after state initialization. A build guard scans for any `phoneState` token before `detailModel()` and fails if found. This fixes the TDZ `ReferenceError` that broke script load in published v0.94–v0.98. Prior helper-only “OK” results are retracted; future handoff requires a real page load plus rendered DOM/state assertions.

## v0.100 persistent Alarm repeat preference

Alarm clock > Repeat now selects and persists Off, Daily or Weekdays and shows the stored value in the row. This completes the visible local Alarm settings rows for enabled state, time, repeat and tone. Alarm firing/scheduling remains unimplemented and unclaimed.

## v0.101 local Conversations and honest Inbox semantics

Messaging > Conversations now groups local draft/sent records by recipient, shows per-recipient counts, and selecting a row displays each local status/body in that conversation. New message remains appended. Inbox now honestly reports No received messages instead of counting local drafts/sent as inbox mail. No received-message simulation is invented.

## v0.102 local Message settings

Messaging > Message settings now exposes persistent Delivery reports and Save sent messages preferences. Delivery reports remains stored preference only because no transmission occurs. Save sent messages affects the explicit local Draft-to-Sent simulation: On moves the draft to Sent items; Off removes it after the local completion confirmation. Message centres and Character support remain reference rows.

## v0.103 persistent Date format

Settings > Date and time now separates Date format and Time format. Date format selects DMY, MDY or YMD and persists; the offline idle screen applies it immediately. Time format keeps the existing 12/24-hour behavior. The format tokens are explicit Ground-Up choices pending physical wording/ordering capture.

## v0.103 persistent Date format

Settings > Date and time now separates Date format and Time format. Date format selects DMY, MDY or YMD and persists; the offline idle screen applies it immediately. Time format keeps the existing 12/24-hour behavior. The format tokens are explicit Ground-Up choices pending physical wording/ordering capture.

## v0.104 persistent Time zone display preference

Settings > Date and time > Time zone now selects and persists Local, UTC, UTC+1 or UTC-5. This is explicitly a stored display preference only: the live clock remains the browser/local clock until a separate safe clock-conversion model is implemented. No network time or carrier zone is inferred.

## v0.105 Time zone applies to phone clock

The stored Time zone preference now drives a bounded local clock model: Local uses the browser clock; UTC, UTC+1 and UTC-5 convert from the current instant using the browser offset. Status time, Date and time lead, and idle time/date use the same `phoneNow()` source and refresh. No network/carrier time is used. Day rollover follows the selected offset.

## v0.106 manual Clock offset

Date and time adds a persisted Clock offset from -720 to +720 minutes in five-minute steps. When Auto-update is Off, the offset applies to the selected zone clock across status/idle/date-time lead; when Auto-update is On, the offset is ignored and the current zone time wins. This is a safe local manual-time model rather than changing the host clock.

## v0.107 confirmed Message counter reset

Log > Message counter > Reset counters now opens a confirmation showing the number of local message records. Because counters are derived from those records, Select explicitly clears local drafts/sent messages and their counters; Back cancels. It does not claim a counter-only reset that would leave inconsistent data.

## v0.108 honest empty Log categories

Log > Missed calls and Received calls now report explicit empty offline lists rather than generic actionable rows. Positioning and Sync log likewise report no records. Only All calls/Dialled numbers show the locally created offline attempts. This prevents generic Ready/Active controls from implying inbound, positioning or synchronization history that does not exist.

## v0.109 honest empty Messaging categories

Messaging > Outbox, Delivery reports and Saved items now show explicit empty local/offline states instead of generic list controls implying records. Outbox has no queued messages because the local send simulation completes immediately; Delivery reports has no reports because no transmission occurs; Saved items has no records because no save-to-folder action exists yet.

## v0.110 local Saved items workflow

On a selected Draft or Sent item, # moves that local message to Saved items and persists. Saved items now lists records and opens their exact recipient/body; left softkey uses the existing exact-message delete confirmation. This replaces the empty-only Saved items surface. The # shortcut is Ground-Up behavior pending physical options capture, and nothing is transmitted.

## v0.111 local Messaging templates

Messaging > Templates now provides three explicit local test templates: Call me, I will be late and Thank you. Selecting one opens the existing draft editor with that body prefilled and recipient active; Select persists the draft. Create message opens a blank body. The template text is Ground-Up local content, not claimed as Nokia firmware strings.

## v0.112 offline Service command composer

Messaging > Service commands > Enter command now opens the shared multi-tap editor. `*` deletes and Select returns an explicit `confirmed service command offline; not sent` result. No command is transmitted or retained, and History remains 0. This replaces a generic toggle while preserving the offline boundary.

## v0.113 local Voice mailbox number

Messaging > Voice mailbox now stores a local mailbox number. Mailbox number opens a digit editor with `*` deletion; Select persists. Call mailbox offline opens the existing offline dialler prefilled with the stored number, and Clear number removes it. No voicemail service or network call is contacted.

## v0.114 honest offline Info messages

Messaging > Info messages now states Cell broadcast unavailable/offline. Reception toggles a persisted local preference, Topics remains 0, and Language reads the phone-language preference. The switch does not receive broadcasts or invent messages; Read remains an empty reference action.

## v0.115 unified local media counters

Applications > Memory status now also reports local Photos and reference Recordings counts. Gallery > Gallery replaces its generic Memory status row with a live Recordings count that opens Voice recorder. Gallery inventory therefore cross-navigates Photos, Themes, Tones and Recordings, all sourced from the same local backend or supplied asset inventory.

## v0.116 honest Applications support endpoints

Applications > Downloads now reports No local downloads instead of generic folder rows. Applications > Settings states Java runtime Not started, Network access Off and Memory Local only. This preserves the owner's explicit Java/game and working-web gate while replacing generic Ready/Active controls with honest status. The 19 JAD identities remain metadata-only.

## v0.117 explicit offline Browser service endpoints

Ovi, Nokia, Home, Web search, Browser and Operator link 1–3 now state unavailable/offline instead of generic Open reference. Their local controls route to Go to address, Bookmarks and Last web address, preserving useful offline phone behavior without contacting retired/current services. Working web remains owner-gated.

## v0.118 honest Browser transfer endpoints

Browser > Content upload, Upload to blog and Download links now state unavailable/offline and No transfer started rather than presenting generic Open/Active controls. Bookmarks, Last web address and Web settings remain local/reference navigation. No upload, download, file disclosure or network transfer is attempted.

## Ground-Up v0.119 · offline web preferences
Browser > Web settings now has a local backend instead of generic reference controls: an editable home-page value, persistent Show images and Cookies preferences, and a confirmation route that clears only local address history. These settings do not enable network access; retired web services remain unavailable. Evidence level remains labelled RM-722 menu inference for the route, with offline behavior chosen for this recreation.

## Ground-Up v0.120 · honest network-app endpoints
The top-level E-mail and Ovi Store nlink entries now open dedicated offline detail surfaces, and Messaging's Instant messaging, E-mail client, and Mailbox 1-5 routes report no account/session/connection rather than falling through to generic active-looking controls. This is an offline recreation boundary, not evidence that the retired services operated this way. No account, message, download, network connection, Java runtime, or working-web behavior was added.

## Ground-Up v0.121 · Organiser offline endpoints
Organiser > Maps now gives an explicit unavailable/no-map/no-route/no-positioning surface. Organiser > Dictionary now has a small offline lookup composer with multi-tap entry, five labelled local definitions, unknown-word feedback, recent lookup readback, and confirmation-backed local history clearing. The Dictionary route comes from the labelled RM-722 firmware menu; the five definitions and offline backend are recreation choices, not extracted handset dictionary data. No network, GPS, map download, or Java runtime is used.

## Ground-Up v0.122 · local backup backend
Settings > Sync and backup now creates, describes, restores, and clears one local phone-state snapshot with confirmation surfaces. The snapshot remains in this browser's local storage and excludes itself to prevent recursive growth. Restore reapplies menu mode, theme, font colour, light level, and wallpaper as well as local collections and preferences. No sync server, account, network, file export, or external data is used. This backend is a disclosed recreation choice beneath the labelled RM-722 firmware menu route.

## Ground-Up v0.123 · message settings backend
Messaging > Message settings now gives Message centre and Character support the same persistent local backend already used by Delivery reports and Save sent messages. Message centre accepts a local number value; Character support switches between Full and Reduced. These preferences do not contact a carrier or send a message. The route labels come from the labelled RM-722 firmware menu; the browser persistence is a disclosed recreation choice.

## Ground-Up v0.124 · idle-screen shortcuts
Settings > My shortcuts now configures persistent left and right idle-screen softkeys from Organiser, Names, Calendar, Notes, and Messages. Reset restores Organiser/Names; Preview opens idle. Idle labels and both hardware softkeys read the saved choices and open the matching local surface. The menu route is labelled RM-722 firmware evidence; these five assignments and browser persistence are disclosed recreation choices pending physical shortcut-list capture.

## Ground-Up v0.125 · remaining Contacts endpoints
Contacts > Synchronise and Network query now state unavailable/offline with no operation started. Memory options has a persistent Phone/Phone and SIM preference while honestly reporting zero SIM contacts. Own numbers accepts local number entries. Service numbers reports none loaded, and Move/Copy report SIM memory unavailable and No transfer started. No account, network, SIM data, contact disclosure, or transfer is used. Route labels come from the RM-722 menu; local own-number storage and memory preference are disclosed recreation choices.

## Ground-Up v0.126 · honest local media state
Media > Video now explicitly reports no camera hardware, recording, or stored videos instead of generic capture controls. Media > Music player reports a zero-track local library and no current track, with persistent local Repeat and Shuffle preferences. No camera, microphone, media upload, stream, download, or network operation occurs. Route labels come from RM-722 firmware menu evidence; the preference backend is a disclosed recreation choice.

## Ground-Up v0.127 · operator/configuration boundaries
Settings > Operator settings now reports no operator provisioning or network connection. Configuration now has persistent local Default configuration and Preferred access point selectors plus explicit zero personal settings/no provisioning. These values do not create an account, access point, carrier configuration, or network connection. Route labels come from RM-722 firmware menu evidence; selector values and persistence are disclosed recreation choices pending physical capture.

## Ground-Up v0.128 · remaining Log counters
Log > Message recipients now derives a local recipient list and message counts from the recreation's stored messages, with recipient detail and a Create message route when empty. Data counters and Connection timer now explicitly report zero bytes/zero time and no offline network sessions rather than generic active controls. No device history, network counter, carrier data, or external message is read or sent.

## Ground-Up v0.129 · Applications metadata route
Applications > Applications now opens a four-row identity summary and routes to the existing 19-entry JAD metadata catalogue. It labels the supplied game and utility identity counts and continues to say Java runtime Deferred. This improves navigation to supplied descriptor evidence only; it does not start Java/game runtime work, execute a MIDlet, or access a network. The supplied JAD files and parsed apps.json remain the source.

## Ground-Up v0.130 · complete tone preferences
Settings > Tones now gives all four visible rows functional persistent state: Incoming call alert selects Ringing/Ascending/Ring once/Beep once/Off; Ringing tone and Message alert tone independently select from the 57 supplied firmware AAC names and request browser preview; Ring volume retains its 1-7 control. The route and tone files come from labelled RM-722 firmware. Alert-mode choices are disclosed reconstruction pending physical submenu capture. Audio reports the browser's real play outcome.

## Ground-Up v0.131 · Security endpoint boundaries
Settings > Security now labels Access codes Not exposed and Certificates None loaded. Selecting either gives exact readback: this recreation neither shows nor collects PIN/PUK/security credentials and has no certificate inventory. Existing PIN request and Security level remain local preference simulations. No credential, private data, certificate, device secret, or network source is accessed.

## Ground-Up v0.132 · menu exit and submenu Options
The right softkey Exit on the main menu now returns to the offline idle screen instead of emitting a not-implemented response. Options on a submenu list now opens a real two-row overlay: Open selected enters the highlighted route and Return to Menu goes back to the main menu. Both keyboard/controller and blue softkey bar use the same semantic routes. Labels are reconstruction pending physical per-submenu Options captures.

## Ground-Up v0.133 · complete Themes rows
Settings > Themes now gives every visible row an exact result. Select theme retains the four supplied package selector; Theme downloads explicitly says offline/no transfer; Type of view opens the working four-mode main-menu dialog; Theme memory lists Black, Dark, Light and Nokia as supplied firmware packages. No download or network operation occurs. Real-page theme pixel checks cover each package's status/menu/softkey artwork.

## Ground-Up v0.134 · complete Lights rows
Settings > Lights now gives each row persistent local behavior: Display light retains its 1-5 level; Keypad light and Notifications toggle independently; Restore default resets level 3 and both toggles On. The body light-level attribute continues to reflect the selected display level. These browser-side controls simulate preferences only and do not claim physical LED/backlight output. Route labels come from RM-722 menu evidence; values are reconstruction pending handset captures.

## Ground-Up v0.135 · complete Camera reference rows
Media > Camera now explicitly states camera hardware unavailable and treats Capture as reference metadata only. Self-timer, Effect and Quality each have persistent local selectors; new reference captures record those values alongside name/time. No camera, image pixels, microphone, permission prompt, upload, or external source is used. Route labels come from RM-722 menu evidence; selector values and metadata backend are disclosed recreation choices.

## Ground-Up v0.136 · complete Accessories rows
Settings > Accessories now shows the persistent default accessory on its first row and exact Not connected states for Headset, Handsfree and TTY. Selecting a disconnected row explains that no hardware accessory is connected to the browser recreation. The default selector remains local preference state only. No USB, Bluetooth, audio device, serial interface, microphone, or system hardware is queried. Route labels come from RM-722 menu evidence; state wording is an honest recreation boundary.

## Ground-Up v0.137 · complete Profiles list
Settings > Profiles now exposes all seven locally supported profiles in its detail list: General, Silent, Meeting, Outdoor, My style 1, My style 2 and Flight. Each row enters the existing persistent activation selector. Activating Flight also updates the recreation's flight-mode idle state; any other profile clears it. These are local preference simulations with no radio/network operation. Profile names combine menu/firmware evidence with disclosed reconstruction pending physical full-list capture.

## Ground-Up v0.138 · honest residual-route fallback
Any remaining menu label without a dedicated local model now opens an honest four-row fallback rather than generic Open/Active controls. Each class reports its actual boundary: no local data, no account/query/configuration, no external operation or transfer, zero log state, or unavailable offline service. Selecting a fallback row may mark it ready for UI navigation but cannot imply a completed external action. This is a safety/completeness fallback, below physical route evidence, and does not replace dedicated models as evidence arrives.

## Ground-Up v0.139 · complete Video reference settings and capture readback
Media > Video keeps its honest no-camera/no-recording state and adds persistent local Video quality and Video length selectors. It still cannot record or store video. Photo inventory detail now reads back each reference capture's saved effect, quality and timer alongside its timestamp. No media pixels, camera/microphone, permission, upload, or network source is used. Selector values are disclosed reconstruction pending physical video-setting capture.

## Ground-Up v0.140 · complete offline Radio rows
Media > Radio now has persistent local on/off state, 87.5-108.0 MHz tuning, Save current station, and saved-station inventory. Search explicitly says unavailable offline and no scan started because browser recreation has no FM hardware. Tuning switches the local radio state on but produces no audio or hardware operation. No headset antenna, device radio, station scan, stream, upload, or network source is used.

## Ground-Up v0.141 · local Inbox search
Messaging > Inbox now says no received messages and local drafts/sent only. Search local messages opens a multi-tap query composer, searches only the recreation's stored To/body fields, reports match count, and renders matching local status/recipient/body summaries. Inbox view gives exact List/no received messages readback. No device inbox, account, carrier, contact, email, or external message source is read.

## Ground-Up v0.142 · Calendar week/date navigation
Organiser > Calendar now keeps Week view and Go to date functional alongside local note create/edit/delete. Week view summarizes the next seven local dates and note counts. Go to date changes by hardware Up/Down, stores a local date filter, and shows matching-note count; Clear date filter returns to the full local list. No external calendar, account, timezone service, invite, notification, or network source is used.

## Ground-Up v0.143 · Organiser empty states and cross-navigation
Notes > Memory status now reports local slots used; empty Edit/Delete give exact no-local-note results. To-do > Go to calendar opens Calendar; empty Delete gives an exact no-local-to-do result. Empty Calendar View reports no local notes for the selected date. These remove generic Active toggles without adding external data, account access, notification, invite, or network behavior.

## Ground-Up v0.144 · honest Calculator modes
Organiser > Calculator now opens the working integer add/subtract backend only from Standard calculator. Scientific and Loan calculator rows explicitly say Reference only and explain that unsupported scientific functions or financial results are not implied. Instructions gives the exact hardware mapping. This removes the prior behavior where every row silently opened the same standard calculator. No financial advice, rate data, account, or network source is used.

## Ground-Up v0.145 · timer mode fidelity
Organiser > Countdown timer and Stopwatch now route by the highlighted row instead of opening the same timer from every option. Normal countdown and split stopwatch retain their working local controls. Interval timer and lap timing are explicit Reference only boundaries; instructions, Start/Continue, and Reset have coherent row-specific behavior. This preserves labelled menu coverage without claiming unimplemented interval or lap capture.

## Ground-Up v0.146 · explicit offline Maps boundary
Organiser > Maps now gives row-specific results for absent map data, unavailable route guidance, empty positioning records, and Back to Organiser. It does not claim a map package, GPS fix, network position, or route engine. The route stays interactive while preserving the offline/no-data boundary.

## Ground-Up v0.147 · global detail activation-chain repair
The shared detail activation path contained three standalone message/calendar fragments between else-if runs. Earlier row-specific results could fall through and be overwritten by generic activation. Duplicate model-return fragments were removed, valid Sent/Drafts handlers were joined into the shared chain, and the generic fallback is global again. Replays cover Maps, Calculator Scientific, Countdown Interval, and Names.

## Ground-Up v0.148 · Contacts offline query routes
Contacts > Synchronise and Network query now have explicit row behavior. Missing accounts, sync history, network service, and query history read back honestly; Local contacts/Search local Names open Names; Back returns to Contacts. No account, network, remote directory, or synchronisation is claimed.

## Ground-Up v0.149 · service and transfer contact routes
Contacts > Service numbers, Move contacts, and Copy contacts now have explicit empty/offline row behavior. Service/SIM provisioning is not claimed; transfer rows disclose that no operation ran, and Memory options opens the existing contact-memory surface.

## Ground-Up v0.150 · positioning and sync log empty states
Log > Positioning and Sync log now have explicit row behavior for empty records, unavailable settings, zero memory, and Back. No GPS/network-positioning hardware, synchronisation account, or external activity is claimed.

## Ground-Up v0.151 · complete offline e-mail boundaries
E-mail client and Mailbox 1-5 rows now give exact account, connection, local-draft, client, and settings readbacks. They do not configure an account, connect, retrieve, or send mail. This completes the labelled firmware routes while working web and network mail remain deferred.

## Ground-Up v0.152 · instant-messaging boundaries
Both labelled Instant messaging routes now provide exact session, account, network, and settings readbacks. No account, live session, network access, message retrieval, or send is claimed.

## Ground-Up v0.153 · store and application-download boundaries
Ovi Store and Applications > Downloads now give exact connection, download, inventory, settings, and memory readbacks. No retired service connection, download, install, or Java runtime is claimed or started.

## Ground-Up v0.154 · complete zero-state log readbacks
Data counters, Connection timer, Call duration, Missed calls, and Received calls now provide row-specific zero/offline results. No packet transfer, network session, connected call, or received call record is claimed.

## Ground-Up v0.155 · Applications settings boundary
Applications > Settings now gives exact Java-runtime, network-access, local-memory, and Back readbacks. Java runtime remains unstarted and explicitly deferred pending owner approval; no application connection or executable is launched.

## Ground-Up v0.156 · detail-model scope guard
The Applications Settings model predicate is restored to its `detailModel(section,item)` argument instead of reading mutable global menu selection. Activation continues to use the selected menu label because it has no local section variable. Static guards now distinguish those scopes, preventing another `window.section` collision or selection-coupled model.

## Ground-Up v0.157 · Outbox and delivery-report empty states
Messaging > Outbox and Delivery reports now give exact row-specific readbacks for empty queues/reports, message details, deletion, settings, and memory. No network send, queue, or delivery receipt is claimed.

## Ground-Up v0.158 · browser transfer boundaries
Content upload, Upload to blog, and Download links now give exact no-transfer, bookmarks, address-history, and settings readbacks. No working web request, upload, download, blog publish, or remote transfer is started or claimed.

## Ground-Up v0.159 · Gallery media inventory
Gallery > Music and videos now gives exact empty music/video and local memory readbacks, while its supplied Tones row opens the existing firmware-tone surface. No personal media, playback, download, or capture is claimed.

## Ground-Up v0.160 · Gallery hub routing
Gallery > Gallery now routes Photos, Themes, Tones, and Recordings inventory rows to their existing local surfaces. Counts remain derived from local state and the supplied 4 themes/57 tone identities; no personal media or hardware capture is claimed.

## Ground-Up v0.161 · Video and Music player endpoint completion
Video now distinguishes missing camera hardware and empty captures from working local quality/length preferences. Music player distinguishes empty library/now-playing state while retaining local Repeat and Shuffle preferences. No hardware recording, personal media, or playback is claimed.

## Ground-Up v0.162 · Operator settings completion
Settings > Operator settings now provides exact operator, provisioning, and network empty-state readbacks, while Configuration opens the existing local configuration surface. No operator identity, provisioning message, or network connection is claimed.
