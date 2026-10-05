# C2 Reborn - HANDOVER (not for upload to the site)

Last updated: 5 Oct 2026, 21:30 BST. Keep this file current after every publish (one commit, no change to index.html).
Repo: https://github.com/mbaiforinsticnt-dev/c2-reborn  |  Live: https://mbaiforinsticnt-dev.github.io/c2-reborn/index.html (about 6 min lag)
Owner: Moti Berger (Europe/London).

## 1. Publish state (check this first, then verify live)
- Live now: v6.238. Blob fa492e1d9d37a14ac8414849ddd329816f993d99, publish HEAD ba1d992199b486d6725cdddd00e59b1e18de910a, archive commit acb8d26c00df2333050c8be5e17306f31ebe6bcb.
- Banked but NOT live: v6.240 (archive commit 5e9c94520e23780010ee0f81252ef76a16f110bc, archive/1-c2-reborn-v6.240.zip, byte-verified). Expected live blob 50609164bc6749462197fe6529a22e1939ec3e98. Contents: Find on map removed from Names > Options; plain search in Conversations (word-start names, start-of-number digits). It carries v6.239 (archive commit 98d8f2952244c1418178dd14bea3476fb2a509cc), whose publish run was cancelled.
- Why not live: GitHub Actions incident on 5 Oct evening. Guarded publish runs 37364074742 (v6.239) and 37365890134 (v6.240) sat queued 15 min and were cancelled. Retry stage 2 (workflow 4-publish-index.yml only; the archive step is already done) once https://www.githubstatus.com shows Actions healthy. Inputs: zip path archive/1-c2-reborn-v6.240.zip, file index.html, new blob 50609164bc6749462197fe6529a22e1939ec3e98, base blob fa492e1d9d37a14ac8414849ddd329816f993d99.
- Rollback for v6.240 = v6.238 blob fa492e1d... . Earlier blobs: v6.237 5462207161c8da389dabe52df65a2c84256a1514, v6.236 29c88c29dc74f62b587b7e83dcd62f8ea012cbcb, v6.235 9d29ed9046525931232300027d2229b6c3405144, v6.234 3eca64b8da02bab6ad57ed9f2a5dca61b67bb97b.

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

## 5. Open items
- Publish v6.240 when GitHub Actions recovers (section 1).
- Moti emulator frames needed: Messaging root, call-log View screen, Call duration screen.
- Compose screen vs his handset video (17:41): handset has no Preview or Search in Options, centre key Send, Exit editor last. Our build keeps Preview and Search (emulator side). Waiting for his word before any removal.
- Remaining SMS attachment items (Wallpapers insert flow, Image thumbnail, Details, "Save message?" on MMS close, Remove submenu).
- Fonts: reload persistence and Wide/Bold overflow check.
- Centre-key situations list; snooze test; rules 1/3/4/6/9/12/13/18/21 audits; Options restyle for the other themes; contact-page Call options.
- Crawl (a8, Black/Nokia theme): about 42 screens checked on v6.238, 0 uneven lists. Restart it on every new build; never drive the shared Chrome while it runs.
- The SDK emulator could not be run locally (launcher exits after Preferences, "Connection Terminated"; RMI registry starts but no phone window). Verification is against Moti's frames and videos.

## 6. How to resume
1. Read this file, BEHAVIOUR-RULES.md and NOTES.md (latest archive zip). 2. Check live state (HEAD, blob). 3. If v6.240 is still not live and Actions is healthy, run stage 2. 4. Re-run the r-tests on any new build. 5. Tell Moti only significant changes (was / becomes) and what is not done.
