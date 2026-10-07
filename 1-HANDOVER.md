# C2 Reborn - handover

Snapshot: 7 October 2026. Read START-HERE.md and the latest archived BEHAVIOUR-RULES.md before changing anything.

## Release state

Live phone: https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html

- v6.306 root blob: `e314ebcfded0ddf997baab0ed322e6a33ca8da2b`.
- Publish commit: `ba2c3cf3ca2b6d8493298b82a128f38475f667da`.
- Archive commit: `e9db6c069f8627e8e37a3e48530eb0ab1be2c31d`.
- Bundle: `archive/2-c2-reborn-v6.306.zip`, containing index.html, NOTES.md, BEHAVIOUR-RULES.md and number-rule-check.py.
- One-step index rollback target: v6.305 blob `76edbe198c98d3532ba93e33dd4aa5ef5d35aa45`.
- Replacement sweep (fixed clock: 7 October 2026, 01:12 BST): 204 page entries, 409 lines, MD5 prefix `4f4a6cb6`, no errors or exceptions. v6.306 differs from the v6.305 sweep baseline 36b87ba9 because call-list text/layout changed.
- Old q126/q127/q129/q130 scripts were lost and were not banked in the release ZIPs. Their old MD5s are void. The replacement is narrower, not equivalent behavior coverage.

Verify current repository and Pages bytes before relying on this snapshot. Raw GitHub is not the served Pages build.

## Evidence and change boundaries

- Additions and repairs can ship. Feature removals need the owner's approval.
- Layout uses handset footage. On a disagreement the emulator wins; report the disagreement before changing the build.
- For every outside audit lead, check emulator or handset footage and report a verdict before editing HTML. Never contact Tab.
- C2-only additions stay and are identified as such, rather than described as Nokia parity.
- Icons come from firmware or sources the owner chose or made. No new drawn icons, Unicode stand-ins or video crops. Disclose the origin. Existing owner-approved exceptions are recorded in the release rules.
- Seed names and numbers must be made-up. Do not put real contacts into code, tests or archives; do not retain handset photos or videos.
- Every question about a screen needs its numbered screenshot. For unanswered choices, make a stated assumption rather than silently claiming evidence.
- No Google/Drive build delivery. Keep release notes, tests and rules in the repository bundles.
- One atomic publish, served-byte verification and a one-step rollback. Never commit another publish while Pages is deploying.

## Current rules and changes

BEHAVIOUR-RULES.md in the v6.306 ZIP is the complete rule record. It includes rules 21-39; next unused number is 40. In particular:

- One shared number-to-name lookup. Select / Select all / Deselect wording, except established message read/unread wording.
- Calling-phase controls deliberately differ from the handset. Do not remove C2-only features just because the emulator lacks them.
- Names includes groups in alphabetic order; group rows have their own view/details and member flows. Selected groups share marking controls and Delete selected confirmation with contacts.
- Add to group is available from contacts, conversations and call-log lists; unsaved numbers do not invent a contact.
- Name display defaults to First name first and uses the shared lookup. Groups are not reordered.
- List icons share a 32px box; visible art is no larger than 27px.
- Symbol picker uses Twemoji for 16 emoji. Star switches symbol/emoji pages; Hebrew is named עברית and uses the shekel sign.
- Calendar selected/today boxes use one fixed size, independent of the digit width. The apparent extra box on 14 was a screenshot misread, not a confirmed defect.

## Not done

- Private PDFs recovered. Their remaining audit leads require evidence-backed verdicts before changes; PDFs and handset images are not public release members.
- Full differential key-by-key parity audit and form-sequence regression coverage remain incomplete.
- Popup rule conflict: missed-call alert Options exists in the current build, while the general popup rule says no Options. Preserve it until the evidence and intended exception are resolved.
- Inbox "where saved" behavior remains unresolved.
- Historical open items still need checking, not blind implementation: call-log View/Call duration evidence, remaining MMS attachment flows, fonts persistence/overflow, other-theme Options and search highlighting/ranking.
- SDK reinstalled with Wine 11.18 and Java 6u37; Home/menu/Log rendering and some mouse navigation verified. Reliable centre-key input, populated missed log and full key-by-key sequences remain unverified.
- Further tidy removals paused until private preservation is byte-verified. ground-up/ is protected by its separate audit.

## Repository housekeeping facts

- `2-restore-index.yml` is a narrowly guarded historical v6.148 restore. It uses fixed blob IDs, NOT 2-index.html. It is not a generic rollback button.
- `tidy-archive.yml` moves root ZIPs into archive/ without changing their bytes. It has no deletion-list input.
- Icon viewer commit: `407b92091684164ac8cade46b9e8c5823aa810a2`; viewer was regenerated from the emoji pool.
- Do not delete and re-upload a documentation file merely to replace it. Use its editor to keep one undoable commit and its exact filename. Browser uploads may add numeric prefixes when names collide.

## Scoped v6.306 audit evidence

- Four full two-line call rows; repeated events retain individual times. Combined list is newest-first. This deliberately differs from Nokia aggregation.
- 13 targeted empty/delete/Back/persistence tests pass. Repeated callers/fifth-row checked in all four lists. Three viewport sizes and eight existing themes visually checked.
- Delete Yes removes the selected event only; Cancel retains it. Reload preserves timestamps, legacy counts and histories over 100 records; demo reseeding never replaces a shortened history.
- Current HTML SHA256: `1154035992378116f504cae172ce335f103598bc40d15aa861f08bde64be206a` (3,715,906 bytes).
- Exact upright solid-blue phone glyph from the handset remains missing. Firmware glyph 1179 retained unchanged. No drawing/recolour/video crop.
- Legacy aggregate histories retain their stored count, but unavailable individual times cannot be reconstructed. No cellular incoming-call pipeline is certified.
- The repaired number-rule probe reports zero leaks on 13 surfaces, but the in-call positive name assertion is absent; it is not full name-lookup certification.
- This is a fixed audit snapshot, not full differential parity certification. No third-party audit has been sent. Ground-up untouched; no private evidence included.
