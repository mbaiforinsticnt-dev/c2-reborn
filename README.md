# C2 Reborn

A browser reconstruction of Nokia C2-01 / Series 40 screen layouts and key behavior. It is a prototype, not Nokia firmware or a working cellular stack.

[Open the live phone](https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html).

## Current release

Snapshot checked 7 October 2026: **v6.305**.

- Root `index.html` blob: `76edbe198c98d3532ba93e33dd4aa5ef5d35aa45`.
- Publish commit: `633fbd9b1ae42ec601c1e4a930f18e4642ba9097`.
- Archive commit: `a9d5cf718170e24df4f73539833883671a6e10e5`.
- Release bundle: `archive/1-c2-reborn-v6.305.zip`.
- Previous release, v6.304: blob `5eac383e93befac644e4274ba0331231f7df80bf`.

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

The replacement sweep covers 204 page entries, screen text, Options, softkey labels and a Down x4 / OK probe. With the test clock fixed at 7 October 2026, 01:12 BST, the v6.305 baseline is 409 output lines, MD5 prefix `36b87ba9`, with no JavaScript errors or exceptions. It is not the lost q126/q127/q129/q130 behavior suite and does not cover key sequences inside forms.

## Assets and data

Use firmware icons or sources the owner chose or made. The 16 symbol-picker emoji are Twemoji: Copyright Twitter, Inc. and other contributors, CC-BY 4.0. See the release notes for credit and origin details.

Only made-up names and numbers belong in source, tests, notes and archives. Do not retain handset photos or videos in the repository.

Older navigation inventories and release notes remain in Git history and the archive bundles; they are not current parity certificates.
