# C2 Reborn - HANDOVER (not for upload to the site)

Last updated: 5 Oct 2026, 22:40 BST. Keep this file current after every publish (one commit, no change to index.html).
Repo: https://github.com/mbaiforinsticnt-dev/c2-reborn  |  Live: https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html (about 6 min lag)
Owner: Moti Berger (Europe/London).

## 1. Publish state (check this first, then verify live)
- Live now: v6.243 (published 6 Oct 00:36). Blob ff3fd3e7a4c5e0b4726f7b9fede4f57e688164f9, 3,628,589 bytes, publish HEAD a0ee6e06146c73623ca7fd36b080002469d4d597, archive commit ee4d527f9d69757c5966d4f65e34b7164eef21b0 (archive/1-c2-reborn-v6.243.zip, byte-verified), run https://github.com/mbaiforinsticnt-dev/c2-reborn/actions/runs/37389313396 (success). Rollback: v6.242 blob 72ca00c07b3c8c21f3892fceb8d74edd5d713ff9 (v6.241 blob 8c2d7b8732a4a8dfb16ed6ec1225f6f97dc3dae2). v6.241 = Use detail Numbers list first; v6.242/243 = icon-row text sits in the upper part of large rows, scroll thumb one item tall.
- Rollback: v6.238 blob fa492e1d9d37a14ac8414849ddd329816f993d99. Earlier: v6.237 5462207161c8da389dabe52df65a2c84256a1514, v6.236 29c88c29dc74f62b587b7e83dcd62f8ea012cbcb, v6.235 9d29ed9046525931232300027d2229b6c3405144.
- If a publish run sits queued 15 min it is cancelled by GitHub; re-run the workflow stage only (the archive step is already done).

## 2. How a build is shipped (do not skip steps)
1. Make the change in a working copy of index.html (one atomic change, bump the banner "C2 Reborn v6.NNN").
2. Run the behaviour tests (r-tests q126, q127, q129, q130: output md5 prefixes 6e4e3a44 6647fb8b 34f22f99 d8d9a646 must not change) plus a test for the change.
3. Zip the bundle (index.html, NOTES.md, BEHAVIOUR-RULES.md, screenshots, tests). Upload as archive/1-c2-reborn-vX.zip in one commit. Download the raw file pinned to that commit and byte-compare with the local zip.
4. Run the guarded workflow 4-publish-index.yml: zip name, file index.html, new blob, base blob. It aborts if the live base blob is not the one given. Scope: Nokia builds into c2-reborn only.
5. Verify the live blob (git hash-object of the raw file at main HEAD = expected). Record: live link, publish HEAD, blob, bytes, run URL, archive commit, rollback blob, test counts, short change list, blunt "not done".
6. Update this file.
- Authority: additions and repairs ship under Moti's standing grant (one atomic commit, live byte check, one-step rollback). Removals only on Moti's explicit word or handset footage.

## 3. Evidence rules
- The video Moti sends of the SDK emulator is an AnyDesk screen recording of the SDK emulator. Primary evidence; the emulator wins over the handset on disagreements (Moti 13:13, 12:55). Handset footage otherwise outranks other sources. Inside the screen, the emulator wins.
- Tab's reports are unverified leads: reproduce first. Never contact Tab.
- C2-only features stay even if the SDK emulator lacks them (rule 11), e.g. View conversations. The emulator is not a C2.
- Icons: original firmware files or sources Moti chose or made. Never drawn by us, never Unicode glyphs, no video crops. Disclose crop / made / firmware. Postal-address open envelope (ICONDSPOSTAL, #53) is Moti's own ChatGPT original: keep (20:47). Keypad symbols stay as is, no stand-ins (Moti 20:44: "up to the hardware makers").
- Keypad, brand and page text use Nokia Sans Wide. In-screen fonts stay the firmware S40 set unless the user picks another in Display > Fonts.
- Do not attach index.txt builds. Image attachments are fine. Never use Google or Drive. Keep notes, test sheet and rules in the repo's non-site folder.
- Report only significant changes, as a short numbered list (was / becomes). Short answers. Milestone line with real counts about every 30 min while working.
- Never contact third parties for him; send zips as .txt copies if a channel refuses zips.

## 4. Moti's rulings this session (5 Oct, BST)
Full wording is in BEHAVIOUR-RULES.md and MOTI-RULES-5Oct.txt inside each archive zip. Summary:
- Centre key = the most common action on the screen; the hardware OK key follows the label. Truncated received message: Open. Fully shown received: Reply. Sent: Send.
- Holding Up/Down more than 0.8 s auto-scrolls at 4 steps/s.
- Equal row height per page; row size follows the emulator/handset for that page; never resize a page to fill blank space (16:19). Only Display settings is normalised (4 x 57).
- Names: dark rounded highlight, Options panel grey translucent (Black theme only so far). Small extra gap between title and first row.
- Names > Options: Search, Call >, Send message >, View conversations, Add new >, Edit >, Delete contact, Marking options >. Find on map REMOVED (Moti 20:30). Call > = Voice call, Video call (Video shows "Video call not available. Calling with voice.", then calls). The submenu appears only from Options; the green key and the centre key do a direct voice call.
- Call-log lists (All calls, Missed, Received, Dialled): centre key = Call. Options follow the emulator frame (17:38): Call duration, Send message >, View, Edit number, Delete, then View conversations (C2-only), Call >. Save and Add to contact only when the number is not a saved contact. Call duration screen and View/contact details: Moti will send emulator frames; Call duration screen parked ("we will expand on that later"). The Details page I built in v6.237 is no longer reachable.
- Conversations: Options > Local search; typing on the list opens a search bar. Own index of conversation names and numbers (unsaved numbers included), never the contacts index. Plain search: word-start for names (Alex or Morgan, not "lex"), start-of-number for digits. Half-name/half-number matching = "enhanced", shelved. Match highlight and ranking: NOT built, waiting for Moti.
- Options menus: Black theme restyle done; other themes pending.
- Create message: 4 rows x 34 px, icon 22, text 24 px (handset photo). Messaging root rows 56 px is a fit, not a measurement.
- Display > Fonts setting exists (user-chosen; default firmware).

## 4b. Row and menu categories from Moti's handset photos (6 Oct 00:21-00:39) - rules to follow
These are Moti's own handset photos and words. Emulator wins where it disagrees. Do not restyle pages until he says so; log and audit first.
1. Icon rows (large rows): the label sits in the UPPER part of the row, not centred (Contacts menu photo, 00:21). Emulator Memory card / Display settings frames agree. Done in v6.243 for rows taller than 15% of the screen. Small-row pages (7 per page) keep the label centred with the icon (Create message, Media menu photos).
2. Row-size categories (rows per page): 4 = largest (Messaging root, Names with number, Contacts menu, Contacts Settings; counter shown). 6 = Names with Contacts view "Name list" (ours already 6). 7 = Media menu, Create message (4 rows then empty tail), Messaging options menus such as Sent Items (New message, Inbox view, Folder details, Message log, SIM messages, Memory status). More categories to come from Moti.
3. Floating type 1.0 = full-width popup list over the page, 7 rows, slightly smaller rows than plain 7-row (Gallery > Options: Downloads >, Mem. card options >, Details, Type of view, Sort >, Add folder, Memory status; softkeys Select/Back).
4. Floating type 2.0 = small submenu popup over the dimmed parent, anchored beside the highlighted parent row, dark background, white highlight on first row (Gallery > Mem. card options > Set password / Rename mem. card / Format memory card). 2.0 popups nest sideways: Gallery > Options > Sort > By name / By date / By format / By size > second 2.0 popup Ascending / Descending, stacked beside the previous one with the parent dimmed.
5. Softkeys seen on handset: Contacts menu Select/Back (ours Options/Select/Back), Messaging root Options/Select/Back, Media menu Options/Open/Exit, Names (Name list) Options/Details/Exit, Create message Select/Back. Handset is secondary: the Contacts menu difference is a possible removal and needs Moti's word.
6. Scroll thumb is one item tall and moves with the selected item (handset Contacts, emulator Display settings). Done in v6.242.
7. Audit of ours (v6.243, rows visible per page from row height): about 4 rows: log, settings, gallery, messaging, message folders; about 5: Contacts menu, Media menu and about 60 other pages (handset says Contacts menu = 4, Media menu = 7: MISMATCH, not fixed); about 6-7: Create message, profiles, message settings. Pages with 3 or more handset photos still missing for most categories.

8. Moti 00:42 naming (verbatim): 4 rows = main. 6 rows = Names (name only). 7 rows = generally Options (7.1.0), none floating. 7 floating rows (7.2.0): since floating, they only reach slightly below the regular ceiling. He will soon specify which pages belong to which category. Wait for his page assignments; do not restyle until then.
9. Moti 00:42: floating type 2 = smallest size (the small submenu popup).
10. Moti 00:43 standing rule: every question to him comes with a screenshot of the page in question; he replies on it.
## 5. Open items
- Moti emulator frames needed: Messaging root, call-log View screen, Call duration screen.
- Compose screen vs his handset video (17:41): handset has no Preview or Search in Options, centre key Send, Exit editor last. Our build keeps Preview and Search (emulator side). Waiting for his word before any removal.
- Remaining SMS attachment items (Wallpapers insert flow, Image thumbnail, Details, "Save message?" on MMS close, Remove submenu).
- Fonts: reload persistence and Wide/Bold overflow check.
- Centre-key situations list; snooze test; rules 1/3/4/6/9/12/13/18/21 audits; Options restyle for the other themes; contact-page Call options.
- Crawl (a8, Black/Nokia theme): about 42 screens checked on v6.238, 0 uneven lists. Restart it on every new build; never drive the shared Chrome while it runs.
- The SDK emulator could not be run locally (launcher exits after Preferences, "Connection Terminated"; RMI registry starts but no phone window). Verification is against Moti's frames and videos.

## 6. How to resume
1. Read this file, BEHAVIOUR-RULES.md and NOTES.md (latest archive zip). 2. Check live state (HEAD, blob). 3. If v6.241 is still not live and Actions is healthy, run stage 2. 4. Re-run the r-tests on any new build. 5. Tell Moti only significant changes (was / becomes) and what is not done.
