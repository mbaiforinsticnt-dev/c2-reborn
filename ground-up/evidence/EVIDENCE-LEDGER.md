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
