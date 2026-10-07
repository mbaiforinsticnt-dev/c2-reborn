# C2 Reborn

A browser reconstruction of Nokia C2-01 / Series 40 screen layouts and key behavior. It is a prototype, not Nokia firmware or a working cellular stack.

[Open the live phone](https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html).

## Current release

Snapshot checked 7 October 2026: **v6.306**.

- Root `index.html` blob: `e314ebcfded0ddf997baab0ed322e6a33ca8da2b`.
- Publish commit: `ba2c3cf3ca2b6d8493298b82a128f38475f667da`.
- Archive commit: `e9db6c069f8627e8e37a3e48530eb0ab1be2c31d`.
- Release bundle: `archive/2-c2-reborn-v6.306.zip`.
- Previous release, v6.305: blob `76edbe198c98d3532ba93e33dd4aa5ef5d35aa45`.

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

The replacement sweep covers 204 page entries, screen text, Options, softkey labels and a Down x4 / OK probe. With the test clock fixed at 7 October 2026, 01:12 BST, the v6.306 baseline is 409 output lines, MD5 prefix `4f4a6cb6`, with no JavaScript errors or exceptions. It is not the lost q126/q127/q129/q130 behavior suite and does not cover key sequences inside forms.

## Assets and data

Use firmware icons or sources the owner chose or made. The 16 symbol-picker emoji are Twemoji: Copyright Twitter, Inc. and other contributors, CC-BY 4.0. See the release notes for credit and origin details.

Only made-up names and numbers belong in source, tests, notes and archives. Do not retain handset photos or videos in the repository.

Older navigation inventories and release notes remain in Git history and the archive bundles; they are not current parity certificates.

## Scoped v6.306 audit evidence

- Four full two-line call rows; repeated events retain individual times. Combined list is newest-first. This deliberately differs from Nokia aggregation.
- 13 targeted empty/delete/Back/persistence tests pass. Repeated callers/fifth-row checked in all four lists. Three viewport sizes and eight existing themes visually checked.
- Delete Yes removes the selected event only; Cancel retains it. Reload preserves timestamps, legacy counts and histories over 100 records; demo reseeding never replaces a shortened history.
- Current HTML SHA256: `1154035992378116f504cae172ce335f103598bc40d15aa861f08bde64be206a` (3,715,906 bytes).
- Exact upright solid-blue phone glyph from the handset remains missing. Firmware glyph 1179 retained unchanged. No drawing/recolour/video crop.
- Legacy aggregate histories retain their stored count, but unavailable individual times cannot be reconstructed. No cellular incoming-call pipeline is certified.
- The repaired number-rule probe reports zero leaks on 13 surfaces, but the in-call positive name assertion is absent; it is not full name-lookup certification.
- This is a fixed audit snapshot, not full differential parity certification. No third-party audit has been sent. Ground-up untouched; no private evidence included.
