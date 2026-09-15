# C2 Reborn v4.4 maximum-depth findings report

Audit cut: 2026-09-15 14:28 BST. Frozen public snapshot: https://mbaiforinsticnt-dev.github.io/c2-reborn/ at source SHA-256 `34f55b8f339d7e21dd8afdacb12af33eaa5e11b1beea61e80cd8625dbcd6f01f`. This report describes that snapshot. Later audit files do not change its behavior.

## Verdict

C2 Reborn is a useful public prototype with several evidence-backed screens and working state flows, but it is not yet close to exhaustive C2-01 / S40 parity. The largest gaps are not cosmetic: 44 destinations are generic placeholders; at least 111 of 178 exposed Options entries produce generic notices in clean default state; active-call `Loudsp.` ends the call; blank LSK labels remain active; the handset clips on short mobile viewports; and the owner-evidence physical body, standby treatment and keypad proportions remain materially wrong.

The correct next move is a risk-first fix pass, not broad surface expansion. Fix destructive input/state behavior first, then make existing menus truthful, then rebuild physical/icon fidelity from the supplied evidence assets.

## Coverage and counts

- 111 named findings: 11 Critical, 65 High, 35 Medium.
- 89 named page states rendered and text/softkeys captured.
- 1,958 page/key probes over 89 states × 22 keys.
- 83 declared normal parent/row routes replayed. Every enabled declaration reached its destination; one disabled E-mail row retained misleading Select behavior.
- 178 Options entries inventoried and invoked at runtime across 35 contexts.
- 210 visible list rows inspected for icon assignment. Only 33 image sources are used; one fallback appears on 122 unrelated rows.
- 6 responsive viewports measured: 320×568, 360×640, 390×844, 390×900, 412×915, 768×1024.
- 25 targeted functional smoke cases, including stateful Contacts, Calendar, To-do, Notes, Alarm, Bluetooth, Themes, Drafts, Send, Calculator and Call behavior.
- Physical comparison used owner standby/off photos and the 47.98-second owner walkaround. SDK comparisons used Messaging, Composer, Calculator, Themes, Web, Media player and bright/dim active-call captures. Official guide topology was used only below physical/emulator evidence and Orange custom content was excluded.

## Stop-ship / P0 findings

1. **False active-call control:** RSK is labelled `Loudsp.` but calls `endCall()`. Center `Menu` has no incall behavior; all six active-call Options entries are notices. Calls lack dialling/ringing/connected/failed state, contact-name resolution and duration linkage (A-081, A-085 to A-088).
2. **False softkey activation:** blank LSK opens Options on eight states. Hardware OK and visible center-softkey semantics are conflated (A-025, A-026, A-067).
3. **Invalid empty state:** `calview` throws when no note exists, reproduced in independent clean-state passes (A-022, A-068).
4. **Short viewport clipping:** the handset is 641px tall at 320×568 and 647px at 360×640 while body overflow is hidden, clipping the lower keypad (A-063).
5. **Unescaped mutable text / stale state:** state-backed text goes into `innerHTML` without escaping; local state is a shallow-merged, unversioned blob without migration/reset (A-093, A-101).
6. **Remote/source truth:** the frozen public source is now byte-verified, and audit artifacts are remotely persisted. Local extracted assets and Git history still differ from browser-created remote commits, so links/hashes in this report are the authoritative remote handoff (A-059, A-060).

## Major completeness findings

- 44 route destinations lack dedicated page conditions and use a generic title + `No items` fallback. Camera, Video recorder, Radio, Voice recorder, Equaliser, Countdown and Stopwatch are among them (A-001, A-019, A-041).
- Runtime Options replay shows at least 111/178 generic notices in default state. Composer has 12/14, active call 6/6, Web 5/6. Static label matching understated the gap (A-035, A-079 to A-084).
- Settings, Apps, Log and Call settings topology/depth diverge from the guide; live SDK root captures are required before firmware-specific restructuring (A-039 to A-046).
- Contacts can be added, but a fourth contact cannot be reached by arrow navigation because dynamic rows use a static three-entry navigation length (A-096, A-103).
- Several inbox/conversation rows all route to one Alex thread and fixed recipient. SMS segmentation and T9/multitap remain under-tested (A-054 to A-056, A-097).
- Call log values and duration screens are hard-coded rather than derived from call state (A-050, A-086).
- Player display says 01:30, internal auto-stop uses 180 seconds, progress is static, one-track next/previous wraps silently, and visual volume has no audio effect (A-108 to A-111).

## Physical and visual findings

- Owner evidence shows a compact, tapering C2-01. Web is a tall/slender slab with a large lower body. LCD/body ratio, deck spacing, D-pad, call/end keys and keypad geometry are materially different (A-071 to A-074).
- Owner keypad is dense, shallow and shaped with exact white secondary legends. Web uses large regular rectangles and approximated `1`, `0`, `*`, `#` marks (A-027, A-075).
- Owner standby is dark with a pale-blue full-width softkey band; web default is a bright blue gradient with black bars (A-057, A-076).
- Icon assignment is semantically unsafe: one fallback on 122 rows. Create message still uses text glyphs despite verified SDK ID 0570. The complete asset family is now available for an explicit `(page,row)->asset` manifest (A-036, A-064 to A-066, A-106).
- Current web correctly uses fallback fonts and makes no genuine-font claim. Five real S40 TTF families were recovered, but public redistribution must be reviewed before embedding (A-107).
- Status state has only default, Dial-dim and dial/incall mode. Bluetooth shown in owner standby and alarm/profile/lock/message/audio/data families are absent; call dim timer is absent (A-078, A-088).

## Evidence-backed passes

- Frozen public Pages bytes match audited local `index.html` exactly; extracted JavaScript passes syntax check and the live screenshot was inspected.
- All 83 declared route rows execute without exceptions; all enabled rows reach declared destinations (A-070).
- Four mobile/tablet viewports at 390×844 and larger fit structurally with no measured overflow (A-069).
- Core behavior passes: four Home shortcuts open real destinations; Go to Home works; lock/unlock works; Calendar note create/view, To-do create/save, Notes create/save, Alarm valid/invalid handling, Bluetooth toggle, Theme apply, Draft open/END resave, message Send and Calculator 2+3=5 all passed (A-104).
- Exact five Web row assets match SDK IDs 0590, 0581, 1093, 0578 and 0586. Themes names/sizes/dates and Calculator operator geometry are based on emulator captures.
- Profile activation, dynamic Drafts count and fictional public demo data pass their scoped tests (A-053 partial, A-094).
- Orange custom guide content is intentionally omitted per scope (A-045).
- Asset archive is hash/integrity checked; icon manifest count and known IDs were visually checked. IDs 0487 and 0639 are equivalent globe variants, not pixel-identical files (A-106 correction).

## Fix order

The detailed sequence is in `FIX-SEQUENCE.md`:

1. Active-call controls, blank softkey gating, empty-state guard, escaping/state migration, responsive fit.
2. Remove or implement Options overclaims; unify dynamic state and navigation; per-thread messaging; replace placeholders with truthful screens.
3. Rebuild owner-evidence silhouette/standby/keypad; create explicit icon manifest; add sourced status families and scroll/label parity.
4. Accessibility, keyboard, pressed/long-press behavior, Help, stale demo dates and regression reruns.

## Evidence and artifact index

- Full register: `AUDIT-REGISTER.md` (A-001 through A-111).
- `page-inventory.txt`, `runtime-page-snapshot.json`, `static-page-map.json`.
- `key-transition-matrix.json`, `route-replay-matrix.json`, `softkey-icon-runtime-matrix.json`.
- `options-dispatch-inventory.json`, `options-runtime-replay.json`.
- `responsive-geometry.json`, `functional-flow-smoke.json`.
- Visual sheets: `c2-owner-video-refinement-side-by-side.jpg`, `messaging-menu-side-by-side.jpg`, `composer-evidence-check.jpg`, `calculator-refined-side-by-side.jpg`, `themes-side-by-side.jpg`, `web-menu-exact-assets-side-by-side.jpg`, `incall-audit-side-by-side.jpg`.
- Reproducibility: `docs/S40-SDK-REBUILD-RECIPE.md`; SDK asset archive and manifest under dev assets.

## Audit limits

- Physical evidence did not cover every screen or every long-press sequence.
- The SDK drops/queues keys and requires 4-6 second verified input pacing; some firmware topology is still uncaptured.
- Runtime Options replay used clean default state. State-specific actions were called unimplemented only when the default exposed action produced a generic notice; fixtures still need to test non-empty cases before final behavior changes.
- Pixel parity is claimed only for named same-screen evidence, never for uncaptured fallback pages.
