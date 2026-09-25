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
| p0505 | — | Mobile phone glyph | ICONMOBILE (contact detail: mobile) | sheet verification | 126 |
| p0159 | — | House / home glyph | ICONHOME (contact detail: home) | sheet verification | 126 |
| p0523 | — | Person glyph | ICONPERSON (contact detail) | sheet verification | 126 |
| p0641 | — | Sync / two-arrow cycle | SYNCsync (Sync row) | sheet verification | 126 |
| p0771 | — | Data transfer arrows | SYNCdata | sheet verification | 126 |
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
| p0181 | — | Magnifier | rcptMag search glass (currently CSS circle+line) | CANDIDATE — open individually before swap |
| p1058 / p1061 / p1062 | 56×56 | Green check marks — SQUARE badges | cbOk slot CLOSED 25 Sep: the build's cb/cbOk check badge is dead CSS - defined once, never rendered anywhere. No badge on screen to match. If a check badge is ever added, these are the candidates (verify shape against a firmware screen first) |
| p0456–p0463 | 30×30 | Radio-button states: hollow ring (unselected), ring+dot (selected); white variants for dark highlight rows | radioDot CSS circles | VERIFIED on firmware (Menu→Options→Main menu view); build CSS already structurally identical — swap deferred as low-value chrome |
| p1043 | 56×56 | Memory card + transfer arrows | future "card busy/transfer" state | VERIFIED family member |
| p0464–p0467 | 56×56 | Memory card + hourglass / warning / lock / "?" | future card-state icons | VERIFIED family members |
| p0900 | — | Floppy disk | SYNCcreate (Create backup) | CANDIDATE (montage-verified) |
| p0898 | 24×24 | Blue down arrow | SYNCcopyin (copy to phone) | CANDIDATE (montage-verified) |
| p0746 | — | Blue up arrow | SYNCcopyout (copy from phone) | CANDIDATE (montage-verified) |
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

- **SYNCswitch** (Phone switch row): want a two-phones glyph; sheet1 231 = phone+red X (NO), 232 = phone+red arrows (unverified). Not yet matched.
- **SYNCrestore** (Restore backup): expected to mirror SYNCcreate (floppy/card + up arrow). Not yet matched.
- **SYNCpc** (PC sync): PC/monitor glyph not found in 30×30 set (p0506 is a speaker). Check 24×24 and 56×56 sets.
- **Wallpaper swoosh**: build draws the idle background as SVG. Firmware default wallpaper may be user data rather than an icon; if the pack yields nothing it gets NAMED, not invented.
- **S40A font**: one firmware font still unmapped (5 genuine Nokia TTFs shipped in pass 125).

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
| p0507 | 30x30 | PC synchronisation (Data transfer row 2) - laptop. GREYED by firmware (no PC paired) |

Notes: build previously used fabricated stand-ins for all SYNC* slots plus p0771 for Data transfer and p0641 for phoneswitch Synchronise - both corrected to firmware assets. Phone switch firmware labels are "Synchronise / Copy to this / Copy from this" (build had "Copy from phone / Copy to phone" in the wrong order). Grey rule: firmware greys Restore backup (no backup present) and PC synchronisation; build now greys the same rows visually. Whether greyed rows are also skipped by the selection cursor is UNVERIFIED (needs handset/emulator nav evidence).
