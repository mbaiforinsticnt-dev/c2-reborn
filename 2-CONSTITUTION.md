# C2 Reborn - working constitution

Written 15 Sep 2026 after the v4.4 recovery, deep audit and fix phase. Read this before starting any C2 Reborn work.

## Survival rules
1. Nothing lives only in scratch. Commit as you go; source, assets, recipes and project-operating docs go to the repo (mbaiforinsticnt-dev/c2-reborn, dev branch). Owner-facing reports may also go to Drive. If it isn't banked remotely, it doesn't exist.
2. Verify the artefact, not the API result. After any publish/deploy/upload, download the live bytes and compare SHA. GitHub Pages lags minutes; the GitHub web editor silently adds a trailing newline; multi-file browser uploads get numeric filename prefixes (contents stay exact).
3. Freeze before auditing or third-party review. Publish a named snapshot, verify its bytes and version label, and audit that. Never audit a moving target.
4. The public URL only changes as a deliberate deploy, after tests pass. Moti gets the link plus what changed, every time.

## Evidence rules
5. Pixel-truth beats "looks fine." Evidence order is Moti's real C2-01 photos/video first, S40 emulator second, official guide third. Compare against exact evidence, not memory of what a Nokia looked like.
6. The emulator is the reference for LCD content: S40 SDK under Wine, recipe in docs/S40-SDK-REBUILD-RECIPE.md. Asset IDs are 0-based (0570 = Create message; Web badges 0578/0581/0586/0590/1093). The full carved asset tree (1,433 icons, wallpapers, 5 real TTFs, animations) is in assets/s40-sdk with a manifest.
7. Known SDK quirks are not bugs to fix blindly: frozen media elapsed counter, no in-call duration timer, ~2min idle LCD dim, no camera device, PC keyboard letters don't enter composer.
8. When two audits disagree, replay the claim against the actual build before adopting it. ChatGPT's v4.1 audit hallucinated a version string; half its findings were already fixed.

## Code rules learned the hard way
9. One getItems(page) source of truth: rendering, selection limits, OK actions and Options must all read the same array. Static screens[] alongside live data caused the unreachable-fourth-contact class of bugs.
10. Never fake behavior: no "X selected" notices, no Select on disabled rows, no labels that lie (Loudsp. hung up). Unimplemented means a plain "Not implemented in this prototype" with Back only.
11. Escape all mutable text into innerHTML. Version saved state (schema v2+) with deep migration - old localStorage contaminates new builds.
12. Scale the whole handset uniformly (transform scale on one fixed reference size). Never flex the shell while the LCD stays fixed.
13. No OS-dependent emoji in UI chrome (call/end buttons are inline SVG).
14. Multitap engine is verified good - don't touch it. T9 needed candidate cycling wired to keys before focus navigation eats them.

## Relationship rules (Moti)
15. Moti has previously said "Always go ahead without me" and "Yes you publish" for C2 Reborn (15 Sep; source message IDs are indexed). Treat this line as a pointer, not authority: before publishing or any other representation, verify the original owner-channel messages and check for later restrictions. Still send what changed + link each deploy.
16. Milestones roughly every 30s on long jobs, digit-emoji progress on his latest message, 💯 at done. Own mistakes early and plainly. No optimism narration.
17. He checks live URLs himself - report follow-through, not claims.
18. All accounts on the catcat identity; no Google SSO on new third-party accounts; credentials via vault link only, never in chat; modchele20@gmail.com is destination-only, never sign in.

## Release and scope guardrails
19. Keep branch roles explicit: `dev` banks tested milestones; `main` is the Pages source. Do not treat a numerically prefixed browser-upload copy (`1-index.html`, `2-index.html`) as the branch entry point. Replace the real root `index.html`, then verify that root file and the deployed Pages bytes separately.
20. A green draw smoke is necessary but not sufficient. For each fix cluster, run focused behavior replay, JS syntax check, the 89-page draw smoke, responsive bounds where relevant, and pixel inspection for visual changes.
21. Demo data is fictional and public-safe. Describe the web build as a prototype, never full parity; web is the product and APK is only a safety artifact. Orange custom items stay out, and Go to/Home shortcuts must open real destinations.
22. Every public publish/deploy has a mandatory ChatGPT-audit handoff. After verifying the deployed bytes, add both that version's exact deployed `index.html` as a `.txt` file and a source ZIP to the dedicated Drive folder `ChatGPT audits` (`1qkwgC47sZlSPg5pGtgmNzMm_NcRfxRyQ`). The parent folder stays anyone-with-link reader. `Audit responses` (`10O3kQ7z0EC8AHSXVHzbuQ-SwarJ0ndwr`) is the only anyone-with-link writer area, for ChatGPT's response documents. Verify folder contents and permissions after every handoff. No publish is complete without this step.
23. Push every WIP commit to remote `dev` immediately, including work not yet verified or ready for `main`; label unverified state in the commit message/report. Local commits are not a safety net. If CLI credentials are unavailable, use the authenticated GitHub web UI and verify the remote commit before continuing substantial work.
24. Every completed audit/reconciliation cycle automatically ends with the next fresh audit candidate: advance its visible version label, run the required regression for its changes, and place a fresh `LATEST` source `.txt` plus ZIP and truthful README in `ChatGPT audits` without waiting to be asked. The README must distinguish an audit candidate from a deployed public checkpoint. Report the folder/files each cycle.
25. APK packaging is again an active deliverable so Moti can test on his phone. The web remains the product and source of truth; APK is an installable test artifact built from a named verified web candidate. Every APK report must state the embedded web version/SHA, package/version identifiers, signing type, installability check and file hash; do not imply APK parity beyond the embedded build.
