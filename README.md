# C2 Reborn

A browser reconstruction of Nokia C2-01 / Series 40 screen layouts and key behavior. It is a prototype, not Nokia firmware or a working cellular stack.

[Open the live phone](https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html).

## Current release

Snapshot checked 7 October 2026: **v6.313**.

- Root `index.html` blob: `047c380665053b0cf0823888c134cd53a876f356` (3,739,345 bytes).
- Publish commit: `6c660a57df6a7370d7d971e1ee777341c9a70b8f`.
- Archive commit: `0b8d2496e0897e7da20c96c4d74576df65bd9148`.
- Release bundle: `archive/1-c2-reborn-v6.313-candidate.zip`.
- Previous release (rollback), v6.312: blob `abcc45c4d9547799481da3a60e353a80a90fb061`.

These are a dated snapshot, not an automatic claim about the latest deployment. Check the HTML version label and served bytes before using them.

## Where to start

- `START-HERE.md`: recover a release, run the replacement regression sweep, publish and verify.
- `1-HANDOVER.md`: current decisions, evidence limits and unfinished work.
- Latest release ZIP: `index.html`, `NOTES.md`, `BEHAVIOUR-RULES.md`, `number-rule-check.py`.
- `ICON-CATALOGUE.md`: historical firmware icon mapping.
- `icon-pool/1-pool.json`: icon pool; `icon-pool/1-index.html`: viewer; `icon-pool/1-sync.py`: sync helper.
- `fonts/`: Nokia Sans source bundle.
- `archive/`: release and historical evidence bundles. Do not prune without approval.
- `ground-up/`: separate frozen reconstruction under an hourly audit. Do not change or remove it as part of root-build work.

## Verification standard

Real emulator or handset evidence is required for each parity claim. Navigation reachability and a clean JavaScript run do not prove phone behavior. Outside audits supply leads, not authority to change the build. Check each lead against the emulator or handset footage and report the verdict before editing.

The replacement sweep covers page entries, screen text, Options, softkey labels and a Down x4 / OK probe. With the test clock fixed at 7 October 2026, 01:12 BST, the v6.313 output is 409 content lines, MD5 prefix `a798bba3`, with no JavaScript errors or exceptions. It differs from the v6.311 baseline only by the two added contact Options. It is not the lost q126/q127/q129/q130 behavior suite and does not cover key sequences inside forms.

## Assets and data

Use firmware icons or sources the owner chose or made. The 16 symbol-picker emoji are Twemoji: Copyright Twitter, Inc. and other contributors, CC-BY 4.0. See the release notes for credit and origin details.

Only made-up names and numbers belong in source, tests, notes and archives. Do not retain handset photos or videos in the repository.

Older navigation inventories and release notes remain in Git history and the archive bundles; they are not current parity certificates.

## Scoped v6.313 additions and limits

- New Call filtering row in Call settings (14th row, additive; existing 13 rows untouched): blacklist numbers pool with Options > Remove behind a review prompt, Reject numbers in blacklist Off / On / On until expiry with a validated future Year/Month/Day/Hour/Minute editor that expires back to Off even after reload, whitelist mode On/Off, whitelist numbers pool, and contact Options Add to blacklist / Add to whitelist. Duplicates are blocked.
- Incoming demo filtering is now enforced: active blacklist blocks listed numbers; Off allows; Timed stops at expiry. Whitelist allows listed numbers only, including blocking all when empty. If both active lists contain a number, simulation pauses pending the overlap decision. Blocked/pending results invent no call-log events. Live empty-whitelist rejection and filters-Off allow screens inspected; other combinations have focused local tests only.
- These are owner-requested custom additions demonstrated on a different handset; they are not Nokia parity claims. Demo data and localStorage only: no real calls, no account contact mutations, no real handset numbers.
- Reject unknown callers is a pending note, not a toggle, until the owner defines "unknown" (withheld vs unsaved). The blacklist/whitelist overlap rule is also undecided.
- Auto call recording is deliberately absent (owner deferred it). Merge contact remains an honest Not implemented.
- 73 scoped checks pass on this exact file (13 enforcement, 14 filter, 12 core, 10 actions, 5 storage, 19 font). Served bytes verified against blob `047c380665053b0cf0823888c134cd53a876f356` after publish; changed screens visually inspected live.
- Carries v6.308-v6.311 work: individual call events with exact timestamps, event-specific snooze/reminder, incoming-call simulation, Phone/SIM Copy/Move (owner-confirmed), red-key group exit repair, unified font routes with Small enabled.
- Exact upright solid-blue phone glyph from the handset remains missing. Firmware glyph 1179 retained unchanged. No drawing/recolour/video crop.
- This is a fixed snapshot, not full differential parity certification. No third-party audit has been sent. Ground-up untouched; no private evidence included.
