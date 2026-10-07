# C2 Reborn - handover

Snapshot: 7 October 2026. Read START-HERE.md and the latest archived BEHAVIOUR-RULES.md before changing anything.

## Release state

Live phone: https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html

- v6.312 root blob: `abcc45c4d9547799481da3a60e353a80a90fb061`.
- Publish commit: `1df51fc15cb07bdda7984ca3f6445977162f7af9`.
- Archive commit: `3cc5e77da3bc099fef8764e83e528f3c8db76bd8`.
- Bundle: `archive/1-c2-reborn-v6.312-candidate.zip`, containing index.html, NOTES.md, BEHAVIOUR-RULES.md and number-rule-check.py.
- One-step index rollback target: v6.307 blob `c8946a2130890089c0c3021a216d952ae6057a7d`.
- Replacement sweep (fixed clock: 7 October 2026, 01:12 BST): 204 page entries, 409 lines, MD5 prefix `a798bba3`, no errors or exceptions. v6.312 differs from v6.311 baseline 6b71d572 only by the two new contact Options; no final newline means wc -l prints 408 for 409 content lines.
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

BEHAVIOUR-RULES.md in the v6.312 ZIP is the complete rule record. It includes rules 21-39; next unused number is 40. In particular:

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

## Historical v6.306 audit evidence (retained, not current-file hashes)

- Four full two-line call rows; repeated events retain individual times. Combined list is newest-first. This deliberately differs from Nokia aggregation.
- 13 targeted empty/delete/Back/persistence tests pass. Repeated callers/fifth-row checked in all four lists. Three viewport sizes and eight existing themes visually checked.
- Delete Yes removes the selected event only; Cancel retains it. Reload preserves timestamps, legacy counts and histories over 100 records; demo reseeding never replaces a shortened history.
- Current HTML SHA256: `1154035992378116f504cae172ce335f103598bc40d15aa861f08bde64be206a` (3,715,906 bytes).
- Exact upright solid-blue phone glyph from the handset remains missing. Firmware glyph 1179 retained unchanged. No drawing/recolour/video crop.
- Legacy aggregate histories retain their stored count, but unavailable individual times cannot be reconstructed. No cellular incoming-call pipeline is certified.
- The repaired number-rule probe reports zero leaks on 13 surfaces, but the in-call positive name assertion is absent; it is not full name-lookup certification.
- This is a fixed audit snapshot, not full differential parity certification. No third-party audit has been sent. Ground-up untouched; no private evidence included.


## Scoped v6.312 evidence and open work

- Current HTML SHA256 `fc795f096508a8eb786d152d7ebec5e79bba9d084f2bd5472fb6d3995c408592`, 3,737,641 bytes. ZIP SHA256 `57acf91d46831c4f26342f8a5bdcf5568322548a15d3bc91b4963c1399e17d51`, 4,667,614 bytes, 81 members. Archive-pinned download byte-matched and served Pages blob matched. Publish run 37595240914 succeeded.
- 60 focused checks: filter14/core12/actions10/storage5/font19. Sweep 409 content lines/no JS errors; no full form or differential certification.
- Call filtering is a deliberate custom addition shown on another phone: Off/On/On-until-expiry with validated future date/time, reload-safe expiry, blacklist/whitelist pools with Options > Remove, contact Add to blacklist/Add to whitelist. Demo data only. IMPORTANT: these settings are not yet wired into incoming-call simulation. Incoming-call enforcement remains open and must be tested.
- Reject unknown callers is a pending note until the owner defines unknown (withheld, unsaved or both). Black/white overlap rule awaits his answer. Merge contact remains Not implemented pending its open question; auto recording was expressly deferred. Exploratory answer-machine/calendar/extra-number tour does not establish implementation scope.
- Live font verification: Contacts Settings selects Small; General Font size Contacts reflects the same saved value. Small18/Normal22/Large26px Names screens inspected after navigation/reload. Six-row layout preserved.
- Live group-red verification: Names > Business opens Business; one red End-call click without active call goes to home. Before/after screenshots inspected.
- Carries event-specific missed-call snooze/calendar reminder, incoming demo call state preservation, Phone/SIM Copy/Move, font and red repairs. No real calls or connected contacts change.
- Backups and batched verified cleanup are separate from development. Keep current/rollback on GitHub. No per-build full MEGA gate; no removals authorized by this update. Ground-up untouched.
- Full differential audit, exact upright blue glyph and other unresolved audit leads remain. No third-party audit send, no audit-ready closeout.
