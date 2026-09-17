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
