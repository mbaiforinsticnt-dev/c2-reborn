# C2 Reborn - start here

## Recover a release

1. Read README.md and 1-HANDOVER.md. Their release facts are a dated snapshot.
2. Read current main and its index.html blob. Separately fetch the Pages index with a unique `?cb=` query and hash those served bytes.
3. Download the release ZIP pinned to its archive commit, not a moving main URL. Compare bytes or a recorded checksum.
4. Extract index.html, NOTES.md, BEHAVIOUR-RULES.md and number-rule-check.py. Never add real contacts to a release bundle.
5. v6.313 archive commit: `0b8d2496e0897e7da20c96c4d74576df65bd9148`; path `archive/1-c2-reborn-v6.313-candidate.zip`; expected HTML git blob `047c380665053b0cf0823888c134cd53a876f356`. ZIP SHA256 `5ce87161946801fe8fa14264c0c48ca0114ab283b7fc3c770582bdf651defd14`; HTML SHA256 `5e7eb18874bed44996ea7b8ee8c9938f8701531dac7914b3fd064296c35c0b45` (3,739,345 bytes).

## Replacement regression sweep

Requires Python 3 and google-chrome with headless support. Save the code below as sweep.py, then run:

```sh
mkdir -p /tmp/h
python3 sweep.py index.html sweep-output.txt
```

The test clock is fixed at 7 October 2026, 01:12 BST (epoch 1791331920000) for repeatable computed times. For v6.313 the baseline is 409 content lines and MD5 prefix `a798bba3`, with zero JS errors or exceptions. It checks 204 page entries, screen text, Options, softkeys and Down x4 / OK routing. It does not replace form-sequence tests or differential emulator testing. The old q126-q130 scripts and MD5 baselines are not recoverable from the release ZIPs checked so far.

The replacement code is banked here so it does not depend on a temporary folder:

```python
import sys,subprocess,hashlib,re
f=sys.argv[1]
x=open(f).read();x=x.replace('<head>', '<head><script>const RealDate=Date;class FixedDate extends RealDate{constructor(...a){super(...(a.length?a:[1791331920000]))}static now(){return 1791331920000}};window.Date=FixedDate;</script>', 1);j=x.rfind('</body>')
t="""<script>window.__err=[];addEventListener('error',function(e){__err.push(String(e.message))});
setTimeout(function(){var out=[];try{press('RSK')}catch(e){}
var pages=[];try{Object.keys(route).forEach(function(k){pages.push(k);(route[k]||[]).forEach(function(p){if(pages.indexOf(p)<0)pages.push(p)})});Object.keys(opts).forEach(function(k){if(pages.indexOf(k)<0)pages.push(k)})}catch(e){out.push('ERRP '+e)}
pages.forEach(function(p){try{go(p);sel=0;draw();var s=document.querySelector('#screen');var txt=s?s.innerText.replace(/\\s+/g,' ').slice(0,300):'';var o='';try{o=JSON.stringify(currentOptions())}catch(e){o='ERR'}
var sm=['sl','sm','sr'].map(function(i){var e=document.getElementById(i);return e?e.innerText:''}).join('/');
out.push(p+' | '+page+' | '+txt+' | '+o+' | '+sm);
for(var i=0;i<4;i++){press('DOWN')}press('OK');out.push('  >ok '+page+' '+(document.querySelector('#screen')||{innerText:''}).innerText.replace(/\\s+/g,' ').slice(0,120));
}catch(e){out.push(p+' EXC '+e)}});
var pre=document.createElement('pre');pre.id='out';pre.textContent=out.join('\\n')+'\\nERRORS '+__err.join(';');document.body.appendChild(pre)},3500)</script>"""
open('/tmp/h/sw_tmp.html','w').write(x[:j]+t+x[j:])
r=subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--virtual-time-budget=20000','--dump-dom','file:///tmp/h/sw_tmp.html'],capture_output=True,text=True,timeout=100).stdout
m=re.search(r'<pre id="out">(.*?)</pre>',r,re.S)
o=m.group(1) if m else 'NOOUT'
open(sys.argv[2],'w').write(o)
print(len(o.splitlines()),'lines',hashlib.md5(o.encode()).hexdigest()[:8],o.split('ERRORS')[-1][:200])

```

## Ship one change

1. Check Actions. If Pages is queued or running, wait. Check whether the intended change already landed before writing.
2. Start from verified current HTML. Make one bounded change, bump the version, update notes and rules, and run the sweep plus tests for the changed behavior. Review intentional differences; a matching MD5 is not parity proof.
3. ZIP index.html, NOTES.md, BEHAVIOUR-RULES.md and number-rule-check.py. Bank it in archive/ in an undoable commit. State any extra evidence included. Do not include handset media or private contacts.
4. Download the ZIP pinned to that archive commit and byte-compare with the local ZIP.
5. Run `.github/workflows/4-publish-index.yml` in Actions with zip_path (actual ZIP path), member (`index.html`), new_blob (git hash-object of the new HTML), base_blob (CURRENT root blob) and a clear message.
6. The workflow aborts if base_blob changed. It makes one index commit and requests a Pages build. Workflow success or raw GitHub match is not a served-byte check.
7. Wait for Pages completion. Fetch the Pages URL with a fresh `?cb=` and require its git blob to equal new_blob.
8. Drive the served page and inspect screenshots of changed screens. Record archive commit, publish commit, served blob, rollback blob, test counts, what changed and what is not done.
9. Update README and handover after verification. Documentation commits can also trigger Pages; avoid overlapping them with a release.

## Rollback

Revert the verified publish commit in one commit, or use a guarded restoration of index.html to the recorded prior blob. Recheck current state first, wait for deployment, then verify served bytes and the affected screen. `2-restore-index.yml` only handles a historical mistaken upload; do not use it for a new release.

## Working scripts

Temporary upload/publish helpers are conveniences, not the durable procedure. The guarded workflow is in `.github/workflows/4-publish-index.yml`; the replacement sweep is banked above; the number-rule checker is in current release ZIPs. Rebuild missing helpers from these recipes rather than trusting old temporary paths. Edit existing docs in place; uploads can gain numeric prefixes and need readback.

## Protected work

Do not touch ground-up/ during root-build work. Do not prune archive evidence or backups until the owner chooses the exact removals. Do not rewrite Git history.

## v6.313 scope

See README.md and 1-HANDOVER.md for scoped tests, deliberate individual-event rule, exact-icon gap, legacy history limit and unverified behavior. Archive includes the replacement sweep/helper, focused tests/results and demo-only preview. The sweep is not full differential certification. Do not reuse scratch-dependent historical scripts without inspecting their prerequisites.


The 409-content-line sweep has no final newline, so wc -l reports 408. This is a formatting count, not a lost test. The v6.313 sweep is byte-identical to v6.312. The earlier v6.312 change from v6.311 baseline 6b71d572 was Add to blacklist / Add to whitelist in contact Options. Enforcement has 13 focused tests separate from the sweep; filter pages have 14.

Rollback is the previous live release, v6.312 blob `abcc45c4d9547799481da3a60e353a80a90fb061`, not unpublished v6.311. Filter settings/pools/contact actions and expiry are implemented and settled rules now govern incoming demo calls. Active blacklist rejects listed numbers until expiry; whitelist permits listed numbers only. Both active with a number in both lists pauses simulation rather than guessing precedence. Blocked/pending results do not invent call-log events. Actual live whitelist-reject and filters-Off allow screens verified; other enforcement paths have focused local tests only. Unknown-caller meaning and black/white overlap remain open. No recording code, Merge unimplemented, no full-parity or audit-ready claim.
