# C2 Reborn - handover

Snapshot: 7 October 2026. Read START-HERE.md and the latest archived BEHAVIOUR-RULES.md before changing anything.

## Release state

Live phone: https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html

- v6.305 root blob: `76edbe198c98d3532ba93e33dd4aa5ef5d35aa45`.
- Publish commit: `633fbd9b1ae42ec601c1e4a930f18e4642ba9097`.
- Archive commit: `a9d5cf718170e24df4f73539833883671a6e10e5`.
- Bundle: `archive/1-c2-reborn-v6.305.zip`, containing index.html, NOTES.md, BEHAVIOUR-RULES.md and number-rule-check.py.
- One-step index rollback target: v6.304 blob `5eac383e93befac644e4274ba0331231f7df80bf`.
- Replacement sweep (fixed clock: 7 October 2026, 01:12 BST): 204 page entries, 409 lines, MD5 prefix `36b87ba9`, no errors or exceptions. v6.303, v6.304 and v6.305 produced the same sweep output.
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

BEHAVIOUR-RULES.md in the v6.305 ZIP is the complete rule record. It includes rules 21-39; next unused number is 40. In particular:

- One shared number-to-name lookup. Select / Select all / Deselect wording, except established message read/unread wording.
- Calling-phase controls deliberately differ from the handset. Do not remove C2-only features just because the emulator lacks them.
- Names includes groups in alphabetic order; group rows have their own view/details and member flows. Selected groups share marking controls and Delete selected confirmation with contacts.
- Add to group is available from contacts, conversations and call-log lists; unsaved numbers do not invent a contact.
- Name display defaults to First name first and uses the shared lookup. Groups are not reordered.
- List icons share a 32px box; visible art is no larger than 27px.
- Symbol picker uses Twemoji for 16 emoji. Star switches symbol/emoji pages; Hebrew is named עברית and uses the shekel sign.
- Calendar selected/today boxes use one fixed size, independent of the digit width. The apparent extra box on 14 was a screenshot misread, not a confirmed defect.

## Not done

- PDF and outside-audit lead verdicts: files need to be recovered or re-sent. No HTML change based on these leads is authorized by a verdict yet.
- Full differential key-by-key parity audit and form-sequence regression coverage remain incomplete.
- Popup rule conflict: missed-call alert Options exists in the current build, while the general popup rule says no Options. Preserve it until the evidence and intended exception are resolved.
- Inbox "where saved" behavior remains unresolved.
- Historical open items still need checking, not blind implementation: call-log View/Call duration evidence, remaining MMS attachment flows, fonts persistence/overflow, other-theme Options and search highlighting/ranking.
- Local SDK launch was unsuccessful after Preferences. Do not describe fresh emulator probes as completed unless evidence actually exists.
- Tidy removals await the owner's choice. ground-up/ is protected by its separate audit.

## Repository housekeeping facts

- `2-restore-index.yml` is a narrowly guarded historical v6.148 restore. It uses fixed blob IDs, NOT 2-index.html. It is not a generic rollback button.
- `tidy-archive.yml` moves root ZIPs into archive/ without changing their bytes. It has no deletion-list input.
- Icon viewer commit: `407b92091684164ac8cade46b9e8c5823aa810a2`; viewer was regenerated from the emoji pool.
- Do not delete and re-upload a documentation file merely to replace it. Use its editor to keep one undoable commit and its exact filename. Browser uploads may add numeric prefixes when names collide.
