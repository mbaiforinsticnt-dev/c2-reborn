# C2-01 Reborn — Firmware Icon Catalogue

Living document. Moti via WhatsApp, 25 Sep 2026, 2:08 PM: "all along I hope you are documenting every icon's meaning a number and potential meaning for future" - this file is that documentation. It records every icon — firmware pack number, verified meaning / where it is used, and potential meanings or substitutes — for future passes. Firmware assets only; anything the firmware does not yield gets NAMED here, never faked.

**Source of assets:** `package_c.ppm` from the C2-01 (RM-721) firmware → 1,433 PNGs, named `pNNNN_WxH.png` (the `pNNNN` number is an extraction index, **not** a semantic id — always open the individual PNG before using it; families cluster numerically).
**Verification source:** Nokia S40 6th Edition SDK emulator screens (LCD shots) + handset shots from Moti where available.
**Statuses:** `SHIPPED` = live in the build · `VERIFIED` = identified on a firmware screen · `CANDIDATE` = visually identified in pack, awaiting firmware-screen evidence · `UNIDENTIFIED` = slot still needs a firmware match · `NAMED` = firmware yields nothing (kept as-is, documented).

---

## 1. Shipped — firmware assets live in the build

| Pack # | Size | Meaning / where used in firmware | Where used in build | Evidence | Pass |
|---|---|---|---|---|---|
| p1044 | 56×56 | Gallery "Memory card" row icon (white card, slanted corner, 3 gold pins) | Gallery Memory card row | emulator Menu→Gallery LCD | 132 |
| p1053 | 56×56 | Blue circle white-i info badge, shown in "No numbers" empty-log dialog | `.infoDialog .ii` badge (39×39, right 8 / bottom 11) | emulator Log→Missed calls LCD | 133 |
| p1054 | 56×56 | Pixel-identical duplicate of p1053 | (substitute for p1053) | binary diff | 133 |
| p1060 | 56×56 | Pixel-identical duplicate of p1053 | (substitute for p1053) | binary diff | 133 |
| p0181 | 30×30 | Magnifier (grey rim, white lens, orange handle) - shown in firmware bottom-docked search field | `.rcptMag` recipient-search glass (24×24 background-image; drawn CSS circle+line removed) | emulator Names→Options→Search LCD (/tmp/emu/s137c_big.png, crop s137c_searchcrop.png) | 137 |
| p0908 | 56×56 | Memory card + phone + red arrow INTO card (phone→card) = Create backup | `listIcons.SYNCcreate` (was a lookalike carved asset; now pack-exact) | emulator Settings→Sync and backup LCD (/tmp/emu/s139e_big.png, carve_sync1.png) | 139 |
| p0909 | 56×56 | Memory card + phone + red arrow INTO phone (card→phone) = Restore backup; GREYED in firmware when no backup file exists, but still focusable and selectable (opens "Select ext. dev.") | `listIcons.SYNCrestore` (FIXED: build's old asset had the arrow pointing the create way) | same LCD evidence; greyed state visible in s139e/s139i/s139j | 139 |
| p0505 | — | Mobile phone glyph | ICONMOBILE (contact detail: mobile) | sheet verification | 126 |
| p0159 | — | House / home glyph | ICONHOME (contact detail: home) | sheet verification | 126 |
| p0523 | — | Person glyph | ICONPERSON (contact detail) | sheet verification | 126 |
| p0641 | — | Sync / two-arrow cycle | SYNCsync (Sync row) | sheet verification | 126 |
| p0771 | — | Data transfer arrows | ~~SYNCdata~~ SUPERSEDED: SYNCdata = p0916 (byte-exact, pass 140) | sheet verification stale | 126 |
| p0619 | 56×56 | Gallery folder: Images | Gallery Images row | gallery family montage | 126-era |
| p0625 | 56×56 | Gallery folder: Video clips | Gallery Video row | gallery family montage | 126-era |
| p0620 / p0624 | 56×56 | Gallery folder: Music (two variants) | Gallery Music row | gallery family montage | 126-era |
| p0623 | 56×56 | Gallery folder: Themes (palette) | Gallery Themes row | gallery family montage | 126-era |
| p0622 | 56×56 | Gallery folder: Recordings | Gallery Recordings row | gallery family montage | 126-era |
| p0621 | 56×56 | Gallery folder: Received files | Gallery Received row | gallery family montage | 126-era |
| p0617 | 56×56 | Gallery folder: Applications (dice) | Gallery Apps row | gallery family montage | 126-era |
| p0616 | 56×56 | Boxes / collection | (gallery family member) | gallery family montage | 126-era |
| 16 smiley faces | ~24×24 | The real C2-01 smiley picker faces, 4×4 grid, firmware order; typed ASCII converts inline | Smiley picker + inline conversion (compose, notes, to-do, cal-note) | emulator Options→Insert symbol→Smiley LCD | 129 |
| DICT icon | — | Dictionary organiser row icon | Organiser Dictionary row | carved from emulator LCD (`icon_dict.png`) | 109 |
| RADIO icon | — | Radio app icon | Radio app | carved from emulator LCD (`icon_radio.png`) | 109 |

Build slots already keyed by pack number (firmware PNGs in the build from earlier passes; precise firmware meaning recorded where known — to be enriched as passes touch them):
`0971 0972 0973(pencil) 0806 0879 0909 0571 0692 0915 0568 0661 0570 0614 0622 0724 0415 1056 1066 0557 0715 0703 0528 0558 0569 0580 0521 0599 0562 0589 0572`

App icons in build (firmware PNGs from early passes; pack numbers not yet recorded — backfill pending): Flickr, Calculator, Sudoku, Store, Converter, Facebook, IMs, WARN, TVcab, CHG, sent_items, saved_items, ims, info_messages, serv_commands, 9001–9004, theme GIFs (black/dark/light/nokia).

## 2. Verified in pack — candidates awaiting placement or screen evidence

| Pack # | Size | Identified as | Potential build slot | Status / blocker |
|---|---|---|---|---|
| p1058 / p1061 / p1062 | 56×56 | Green check marks — SQUARE badges | cbOk slot CLOSED 25 Sep: the build's cb/cbOk check badge is dead CSS - defined once, never rendered anywhere. No badge on screen to match. If a check badge is ever added, these are the candidates (verify shape against a firmware screen first) |
| p0456–p0463 | 30×30 | TWO families: p0456–p0459 = checkboxes (empty / green-check, plain + grey-border), p0460–p0463 = radios (ring+pale center unselected / white ring+black core selected, + glow variants) | multi-mark lists (p0456/p0457) + ALL single-select radio pickers (p0460/p0461) | BOTH SWAPPED into build: radios passes 144+146, checkboxes pass 145 [LCD s144k/s144l + s145o/s145p] |
| p1043 | 56×56 | Memory card + transfer arrows | future "card busy/transfer" state | VERIFIED family member |
| p0464–p0467 | 56×56 | Memory card + hourglass / warning / lock / "?" | future card-state icons | VERIFIED family members |
| p0900 | — | Floppy disk | SYNCcreate (Create backup) | CANDIDATE (montage-verified) |
| p0402 | 320×480 | Analogue clock FACE (dark dial, tick marks) - idle/screensaver clock | screensaver analogue mode (build SSanalog exists) | CANDIDATE - needs emulator screensaver evidence |
| p0403 | 320×480 | Analogue clock background (dark radial gradient) | with p0402 | CANDIDATE - same |
| p0370-p0401 | 296×296 | Analogue clock HANDS, 32 rotation frames | with p0402 | CANDIDATE - same |
| p1419 | 198×198 | Globe photo (Europe/Africa, photographic) | unknown - Gallery default image or sync illustration | CANDIDATE |
| p0898 | 24×24 | Blue down arrow | ~~SYNCcopyin~~ SUPERSEDED: SYNCcopyin = p0914 (byte-exact, pass 140) | stale candidate |
| p0746 | — | Blue up arrow | ~~SYNCcopyout~~ SUPERSEDED: SYNCcopyout = p0913 (byte-exact, pass 140) | stale candidate |
| p0895 | — | Grey/red transfer arrows | alt for SYNCdata | identified, no slot |
| p0901 | — | Blue lock | — | identified, no slot |
| p0930 | — | @ symbol (NOT refresh) | — | identified, no slot |
| p0973 | — | Pencil | — | identified, no slot |
| p0896 | — | Person + X | — | identified, no slot |
| p0910 | — | Beige folder | — | identified, no slot |
| p0178 | — | Handshake | — | identified, no slot |
| p0801 | — | 3G badge | — | identified, no slot |

Sheet-index finds (24×24 sheet1 indices, not yet re-keyed to pack numbers): 16 green refresh · 55 green up arrow · 58 globe+up · 63 blue person card · 76/77 grey house (alt ICONHOME) · 78 blue phone · 203–221 real S40 emoticon set (cross-ref for the 16 shipped smileys) · 223–228 person+badge family · 168–202 green nav arrows/gears · 0–1 floppy · 2 lock · 17/18 headsets · 61/66 wifi · 72–95 Skype/Ovi purple set · 96–167 red/blue app badges.

## 3. Unidentified — slots still needing a firmware match

- **SYNCswitch** (Phone switch row): RESOLVED = p0912 56×56 (phone + green-left/blue-right arrows), byte-exact MSE 0.0 vs build asset (pass 140).
- **SYNCrestore - RESOLVED pass 139**: p0909 (card + phone + red arrow into phone). Greyed in firmware when no backup exists but remains focusable/selectable - nav-skip RESOLVED (firmware cursor stops on greyed rows; build already matches). Open: selecting it in firmware opens a "Select ext. dev." device picker step the build does not model (jumps to the info page) - needs a memory-card-equipped run to map the full flow.
- **SYNCpc** (PC synchronisation): RESOLVED = p0507 30×30 laptop, byte-exact MSE 0.0 vs build asset (pass 140). Row is ENABLED+focusable in firmware (ungreyed in build pass 139).
- **Wallpaper swoosh - NAMED pass 138**: the firmware yields no idle-wallpaper asset. Evidence: full size-scan of all 1,433 pack PNGs (the only 240x320 asset, p1116, is a blue UI template graphic, not wallpaper); SDK `predefgallery/predefgraphics/predefwallpapers` dirs are EMPTY; the build's own firmware-faithful wallpaper picker (WPphotos/WPgal/WPslide/WPcam/WPgraph/WPadj) confirms wallpaper comes from user/theme content. The grey swoosh is theme-compiled art, not a pack icon. The build's drawn swoosh stays as the documented approximation - NAMED, never faked.
- **Sync family: ALL RESOLVED byte-exact (pass 140)**: Phone switch = p0912, Data transfer = p0916, Server sync = p0641 (30×30), Sync and backup header = p0915 (folder + circular arrows, already id'd). Matcher: build-asset-vs-pack masked MSE, LANCZOS resize, MSE 0.0 = byte-exact.
- **S40A font - RESOLVED pass 135**: "Nokia Sans Title SemiBold S40A" (font_7984184.ttf) is the firmware's international companion font, NOT a Latin strike. It has no basic Latin glyphs; it covers Armenian (0531-058A), Hebrew (05D0-05EA), Thai (0E01-0E5B), Georgian (10D0-10FC), Ethiopic (1200-137C), Arabic presentation forms + Indic digit sets. The firmware falls back to it per-glyph for those scripts (verified: idle "Waiting"/"NOKIA"/dialer digits all match the other already-wired strikes, never S40A). Wired into the build as per-glyph fallback after each Nokia family in all four font stacks; live-verified document.fonts.check = true for Armenian/Hebrew/Thai/Georgian/Ethiopic/Arabic-Indic.

## 4. Traps and red herrings

- **p1080 = envelope.** The build's old Gallery slot was *named* "1080" and held a hand-drawn SVG — the number coincidence cost a pass. Pack numbers are extraction indices, never semantics.
- LCD partial repaints leave stale glyph pixels right of the cursor in text fields — read field content LEFT of the cursor only.
- Pack 30×30/24×24/56×56 sets overlap in meaning at different sizes; verify the exact file, not the family.

## 5. Out of scope (hardware frame, not screen UI)

The two inline SVGs on the physical call/end buttons are the C2-01's hardware green/red receivers — not screen icons, not swapped.

## 6. Method

1. Candidate hunt: labelled montages (30×30 sheet0 0–287, 24×24 sheet1 0–242, 56×56 sheets A/B 0419–1416), then open individual PNGs.
2. Firmware meaning: emulator LCD evidence of the actual screen before any swap.
3. Parity montage (LCD crop vs pack PNG) ships with the pass report as proof.
4. Every newly verified icon gets an entry here in the same pass.

---
*Created pass 133 (commit 9b723cd22d). Updated with every icon pass.*


## Pass 134 - Sync and backup family (firmware evidence 25 Sep, emulator LCD shots)
| Pack id | Size | Meaning / where the firmware uses it |
|---|---|---|
| p0912 | 56x56 | Phone switch (syncbackup row 1) - phone + green-left/blue-right arrows |
| p0908 | 56x56 | Create backup (syncbackup row 2) - archive box + phone + red LEFT arrow |
| p0909 | 56x56 | Restore backup (syncbackup row 3) - archive box + phone + red RIGHT arrow. GREYED by firmware when no backup exists |
| p0916 | 56x56 | Data transfer (syncbackup row 4) - globe + white circular refresh |
| p0917 | 56x56 | Synchronise (Phone switch page row 1) - phone + blue/green circular arrows |
| p0914 | 56x56 | Copy to this (Phone switch row 2) - phone + green RIGHT arrow (into this phone) |
| p0913 | 56x56 | Copy from this (Phone switch row 3) - phone + blue LEFT arrow (out of this phone) |
| p0641 | 30x30 | Server sync (Data transfer row 1) - blue up-left + green down-right arrows |
| p0507 | 30x30 | PC synchronisation (Data transfer row 2) - laptop. Row ENABLED+focusable in firmware (pass 139 evidence s139f); earlier greyed claim stale |

Notes: build previously used fabricated stand-ins for all SYNC* slots plus p0771 for Data transfer and p0641 for phoneswitch Synchronise - both corrected to firmware assets. Phone switch firmware labels are "Synchronise / Copy to this / Copy from this" (build had "Copy from phone / Copy to phone" in the wrong order). Grey rule (pass 139 RESOLVED): firmware greys Restore backup (no backup present) but the cursor still stops on it and it stays selectable (opens "Select ext. dev." picker); PC synchronisation is ENABLED+focusable, not greyed. Build matches both - no nav-skip anywhere.

## Pass 140 - Sync family byte-exact verification (firmware LCD + masked-MSE matcher, 25 Sep)

Matcher: build asset vs pack PNG, masked MSE (LANCZOS resize, composite over dark bg, MSE on pack-opaque pixels); MSE 0.0 = byte-exact.

| Pack | Slot | Result |
|---|---|---|
| p0912 | SYNCswitch (Phone switch row) | MSE 0.0 byte-exact |
| p0916 | SYNCdata (Data transfer row) | MSE 0.0 byte-exact |
| p0641 | SYNCsync (Server sync, 30×30) | MSE 0.0 byte-exact |
| p0507 | SYNCpc (PC synchronisation, 30×30 laptop) | MSE 0.0 byte-exact |
| p0917 | SYNCpswsync (Synchronise, Phone switch row 1) | MSE 0.0 byte-exact |
| p0914 | SYNCcopyin (Copy to this) | MSE 0.0 byte-exact |
| p0913 | SYNCcopyout (Copy from this) | MSE 0.0 byte-exact |

Firmware Phone-switch submenu LCD (/tmp/emu/s140c_big.png, carves carve140_*): "Synchronise / Copy to this / Copy from this". Firmware "Copy to this" shows phone + GREEN right arrow = p0914; "Copy from this" shows phone + BLUE left arrow = p0913. The suspected copyin/copyout swap is REFUTED - build assignments match firmware exactly. No build change this pass.

Family map p0906-p0917 (montage /tmp/emu/sync_family_full.png): p0906 wifi-beam UNIDENTIFIED; p0907 phone+card; p0908/p0909 create/restore backup; p0910/p0911 plain folders; p0912 phone switch; p0913 phone + blue LEFT arrow; p0914 phone + green RIGHT arrow; p0915 folder + circular arrows = Sync-and-backup header; p0916 globe + sync badge; p0917 phone + circular arrows.

Stale entries corrected this pass: p0771 (was SYNCdata), p0898/p0746 (were copyin/copyout candidates), SYNCswitch "not yet matched", SYNCpc "unidentified", p0507 "greyed by firmware" (firmware row is enabled, pass 139).

## Pass 141 — messaging envelope/bubble bundle (HEAD 59c7fdb)
- p0955 (56x56, two gold speech bubbles, front w/ lines) = Messaging menu Conversations row icon [Moti photo d9d099c6]
- p0591 (56x56, blue up arrow in grey tray) = Messaging menu Outbox row icon [photo d9d099c6 + LCD cn141_outbox]
- p0522 (30x30, gold bubble w/ lines, right tail) = Conversations list RECEIVED row icon @22px [photo 81ddef27]
- p0525 (30x30, grey bubble w/ lines, left tail) = Conversations list SENT row icon @22px [photo 81ddef27]
- p0522 + red dot (extracted from p0756, composited at build) = Conversations list UNREAD row icon @22px; 2nd line "N unread message(s)" [photo 81ddef27]
- p0760 (30x30, open envelope, flap up, dark interior) = conversation view READ icon @18px [photo 8027f2d8]
- p1066 (56x56, closed env + green down arrow) = conversation view unread/focused incoming icon @18px [photo 8027f2d8]
- p0759 (30x30, env + green check) = conversation view sent icon @18px [LCD cn141_sent]
- p0786 (30x30, env + blue i) = conversation view sent-info icon @18px [LCD]
- Status bar unread envelope = CARVED from Moti's handset photo (image-d9d099c6.jpg status bar, 28x21 white glyph, pass 143 re-carve); pack has no standalone status envelope asset (NAMED); toggled on unread>0; sits RIGHT of battery per handset
- Menu subtitles: Conversations "N unread msgs.", Drafts "N messages", right-aligned [photo d9d099c6]
- List counter now "pos/total" (e.g. 1/179) [photo 81ddef27 shows 2/200]
- REMOVED build-only auto-mark-read-on-scroll in Conversations list (contradicted photo: unread persists until opened)

## Pass 143 — status-bar envelope re-carve (HEAD 377bd3a)
- Pass-141 carve was WRONG: lcd_s141y.png's status bar held signal + battery + profile + time, no envelope - the carve grabbed the LCD BATTERY region and shipped a battery-shaped "envelope" (duplicate-battery look spotted by Moti on the live build).
- Re-carved from Moti's handset Messaging-menu photo (image-d9d099c6.jpg): its status bar shows signal, battery, white outline envelope, bluetooth rune. Envelope asset now a 28x21 white glyph from that photo.
- Order corrected to match handset: battery, then envelope (build had envelope left of battery).
- Pack re-swept (all assets 12-60 x 10-50 px, alpha-shape IoU vs the photo carve): no monochrome status envelope in package_c; only color 30x30 list envelopes (p0536/p0727/p0764/p0766/p0769 + badged p0789/p0544/p0733/p0734). Status envelope stays a NAMED carve from firmware screen evidence.

## Pass 144 — radio-button family resolved (HEAD d4139be)
- Firmware LCD evidence: Settings > Display > Navig. key icons picker IS a radio list (lcd_s144k/s144l): unselected = ring + pale interior, selected = white ring + black core (same glyph focused or not).
- p0460 (30x30, bright ring + pale center) = radio UNSELECTED; p0461 (30x30, white ring + black core) = radio SELECTED [LCD s144k/s144l]. p0462/p0463 = glow variants of the same pair (unselected/selected). p0456-p0459 = checkbox family (empty / green-check, plain + grey-border) - NOT radios.
- Build's radiolist picker (Screen saver / Cell info display On-Off etc.) swapped off CSS-drawn circles onto p0460/p0461 at 28px.
- OPEN question flagged: build's "Content options" (Personalise view) multi-mark list uses the same drawn radio dots, but a multi-mark list on firmware likely uses the p0456/p0457 CHECKBOX pair - needs firmware evidence of that screen before any swap.

## Pass 145 — checkbox family into multi-mark lists (HEAD 003bd6f)
- Firmware LCD evidence: Settings > Display > Home screen > Personalise view > Options > "Select shortcuts" opens the "Shortcut bar links" MULTI-MARK list (lcd_s145o/s145p). Marks are SQUARE CHECKBOXES: unmarked = flat grey empty box, marked = grey box + green check, greyed-marked row ("Application list") = gold folder/box glyph. Softkeys Mark/Unmark + Done.
- p0456 (30x30, flat grey empty box) = checkbox UNMARKED; p0457 (30x30, grey box + green check) = checkbox MARKED [LCD s145p, green-cluster carve + alpha-masked MSE + visual montage]. p0458/p0459 = grey-border variants (heavier frame, not what the LCD shows).
- Build swapped off drawn art in all three multi-mark lists: contentoptions ("Content options", was CSS radioDot circles), gotocheck (Go to > Select options, was CSS box + &#10003;), gotoapps (Go to > Application list picker, same CSS box). All now use CHECK_OFF=p0456 / CHECK_ON=p0457 (28px in shortcutRows, 18px in plain rows). gotocheck keeps GDfold for the greyed "Application list" row - matches the firmware gold glyph.
- Build's contentoptions radioDot CSS class now unused by that page (left in place; other .opt radio dots remain for single-select semantics - future pass candidates for p0460/p0461).

## Pass 146 — radios into the remaining single-select pickers (HEAD 7ac4994)
- Swept the last drawn radio dots: Menu > Options > Main menu view radioPanel (List/Grid/Grid with labels/Tab) and the generic submenuPanel radios (Gallery "Type of view" + gallery sort Ascending/Descending). All single-select semantics - same pattern as the pass-144 On/Off radio lists [LCD s144k/s144l] and the earlier Main-menu-view firmware verification.
- Both render sites now use RADIO_ON=p0461 / RADIO_OFF=p0460 at 18px (.opt .optDot), replacing the 8px CSS radioDot circles. Proof: shot146_menu.png, shot146_gal.png.
- After this pass the CSS .radioDot class has no render sites left (dead CSS, left in place per removals rule). All mark indicators in the build are now firmware assets: radios p0460/p0461, checkboxes p0456/p0457.
- Also fixes pass 145's lost edit: the p0456–p0463 family line above is now actually corrected (the pass-145 write only appended its section and dropped the line edit).

## Pass 147 — genuine Black.nth wallpaper swoosh carved from emulator LCD (HEAD bfefbf3)
- The default idle/menu background was drawn art: an inline SVG swoosh approximation on `.screen`, two CSS ellipse divs (`.swoosh`/`.s1`/`.s2`) on the idle home, and a navy CSS gradient overlay `.homeTheme`. The firmware pack holds no wallpaper asset (largest pack image is 296x296 clock hands), so the genuine Black.nth wallpaper was reconstructed from emulator LCD captures.
- Method: flipped Settings > Display > Home screen > Home screen mode to Off for a clean idle (lcd_s147idleoff.png), then repaired the only two text-covered bands (operator NOKIA shot y40-60, date shot y68-85) by per-pixel mode vote across 24 theme-validated UI screens (n43-n91, p112az/bc, sm3/sm4 series). Zero low-vote pixels, seam delta ~2 lum, donor/base offset ~0.08. Downscaled 363->320 rows, cropped LCD y30..284 (skips status-clock bleed) -> 240x254 PNG.
- Build changes: default `.screen` SVG+PNG background replaced with the carved PNG; `body[data-theme='Black.nth'] .screen` plain gradient PNG replaced with the same carved PNG; drawn swoosh divs hidden and `.homeTheme` overlay removed under Black.nth only (other themes keep their drawn look until their wallpapers are carved - Dark.nth / Light.nth / Nokia.nth / Classic light / Graphite are queued for emulator theme-flip captures).
- Proof: shot147_idle.png, shot147_menu.png vs emulator lcd_s147idleoff.png.
