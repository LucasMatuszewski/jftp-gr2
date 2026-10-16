# jFTP modernization research and source audit — 2026-10-16

**Purpose:** evidence and alternatives for [proposed ADR-008](../ADR/008-modernization-roadmap.md).

**Application source examined:** `469ecd58fe268dc759c91905c25ddcabf8782c8d`. **Status:** research only, no implementation or modern-runtime qualification.

Three explicitly scoped Luna inventories supplied source facts. The primary agent chose recommendations and requested precision/reachability checks. Luna did not choose the architecture. No application build/test/startup, new JDK installation, application dependency installation, FTP connection or updater request occurred. Public documentation and artifact **metadata** were fetched. Temporary documentation-only Mermaid tooling is separate from the application build.

## 1. Review outcome for the PRD

The existing user stories remain the functional preservation boundary. A new Java target, build toolchain, internal port or test framework does not inherently require new business features. The baseline also records observable limitations, so intentional fixes must not be hidden under “same functionality.”

The source audit found genuine documentation errors, corrected as PRD version 1.1:

| Correction | What source establishes | Document consequence |
| --- | --- | --- |
| Active certificate manager | Only the server tab is added; client tab/builder are commented out. Both active construction paths open this same dialog. Client JKS configuration/use remains present. | Correct F10, UI description and AC-58; do not promise an active client-certificate management screen. |
| Warning certificate details | The warning opens an installable detail dialog; Install requests persistent server-store import. Warning Yes only caches acceptance for that trust-manager instance. Install is not rolled back by later No. | Clarify AC-61, add AC-89 for an existing omitted path, preserve all other identifiers. |
| Server validation description | The default X509 manager is initialized, but server validation does not delegate to its checkServerTrusted. It uses local leaf-validity, CN and stored-alias tests. | Correct ADR-003/004 facts; do not describe current validation as standard PKIX. |

These corrections add no function or code. Tests were not rerun and source-only criteria were not promoted to Executed.

## 2. Source inventory and evidence boundaries

### 2.1 Protocol and replacement surface — Luna protocol inventory

A production import scan found **29 files** directly importing the legacy FTP API: 22 core/UI files and seven actions. A prior draft count of 26 was corrected before use. Imports are a coupling indicator, not a whole-program call graph.

| Area | Current facts a replacement must account for | Primary original source |
| --- | --- | --- |
| Configuration | Host/port/user/password/account; passive; commands; initial directories; client/parser class names; four SSL modes and data-channel flag | [RemoteHost](../../src/main/java/com/myjavaworld/jftp/RemoteHost.java#L33), L33–229; [ConnectionDlg](../../src/main/java/com/myjavaworld/jftp/ConnectionDlg.java#L607), L607–713 |
| Reflection | Client and parser are created from persisted class-name strings; UI offers Default/AS400 clients and Unix/default/DOS parser choices | [JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L91), L91–101; [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L623), L623–641 |
| Connection | Account-capable login, configured command order, optional initial remote path and listing; inner/outer errors differ | [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L593), L593–699 |
| Transfers | Standard, As, ZIP and temporary-copy variants all reach the legacy client; fixed boolean/offset argument values do not establish their external semantics | [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L707), L707–971, L1558–1601 |
| Metadata and maintenance | Parser-created entries feed tables, sorting, ownership/link metadata, create/rename/delete and SITE CHMOD | [RemoteFilePropertiesDlg](../../src/main/java/com/myjavaworld/jftp/RemoteFilePropertiesDlg.java#L155), L155–253, L519–560; session L973–1278 |
| Filters | Relevant filters affect child enumeration for transfer/delete/recursive permission changes | [RemoteFileFilterDlg](../../src/main/java/com/myjavaworld/jftp/RemoteFileFilterDlg.java#L102), L102–138; session L795, L937, L1143, L1263 |
| Proxy | JVM-wide SOCKS properties and default Authenticator, not a per-client setProxy call | [JFTPUtil](../../src/main/java/com/myjavaworld/jftp/JFTPUtil.java#L70), L70–95; [ProxyPrefsPanel](../../src/main/java/com/myjavaworld/jftp/ProxyPrefsPanel.java#L255) |
| Commands/events | Post-login commands differ from interactive prefix skipping; HELP/STAT/SYST/NOOP and control/data events feed logs/progress | [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L518), L518–568, L1420–1493 |

The cached exact dependency scope contained a binary JAR and POM, not its source JAR. Public signatures were inspected with javap, not treated as implementation semantics. The current dependency/application POMs declare Apache 2.0; this is metadata, not a general legal conclusion. No key/password values were reproduced.

The source uses connection/list/transfer/file-operation/listener APIs, not just file bytes. A replacement must qualify active/passive connections, account login, optional/explicit/implicit FTPS, clear/encrypted data-channel choice, parser/profile mapping, SOCKS behavior, commands, filters and metadata.

Commons Net having an OS/400 parser does not establish equivalence to the old AS400 client. If an actual required server/profile cannot be qualified in an authorized lane, keep the old provider for it or agree a product-scope change. A simulated listing is not real AS/400 E2E proof.

### 2.2 Persistence/security — Luna full-reader/writer and caller inventory

Four production classes explicitly declare Serializable: JFTPPreferences, RemoteHost, Favorite and LocalFile. The inspected writers persist preferences/favorites, not LocalFile.

| Current contract | Migration/refactor implication | Primary original source |
| --- | --- | --- |
| RemoteHost is mutable; Favorite inherits it, has its own serialization identifier and name-only case-insensitive equality | Changing inheritance, class names, field types or identities can break saved forms or list semantics | [RemoteHost](../../src/main/java/com/myjavaworld/jftp/RemoteHost.java#L33), [Favorite](../../src/main/java/com/myjavaworld/jftp/Favorite.java#L25) |
| Manager accepts raw lists/base RemoteHost entries, while UI edits cast entries to Favorite | Manager persistence tests do not establish that every accepted list is UI-editable | [FavoritesManager](../../src/main/java/com/myjavaworld/jftp/FavoritesManager.java#L64), L64–155; [FavoritesDlg](../../src/main/java/com/myjavaworld/jftp/FavoritesDlg.java#L190), L190–205, L349–405 |
| Preference save directly overwrites an object stream; load returns defaults from finally on corrupt input, possibly leaving corrupt bytes | Atomic writes/recovery changes are separate behavior decisions | [JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L512), L512–568 |
| Favorites read can immediately rewrite a legacy list; AES uses a source-embedded key and can fall back to a raw list | No implicit schema/credential migration or unearned encrypted-storage guarantee | [FavoritesManager](../../src/main/java/com/myjavaworld/jftp/FavoritesManager.java#L64), L64–137, L170–186 |
| No per-reader object-input filter is present in the inspected readers | Filtering must qualify supported graphs, including inner sealed-object reading, rather than claiming a simple outer filter solves it | Same readers; [Java filtering contract](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/io/ObjectInputFilter.html) |
| JKS caches initialize once; preferences can later change paths/passwords without reloading them | Cache contents can be saved to newly configured paths; a lifecycle fix is observable | [KeyStoreManager](../../src/main/java/com/myjavaworld/jftp/ssl/KeyStoreManager.java#L36), L36–132, L170–224 |
| Add/delete mutates cache before disk save, with no rollback | Store write failure can leave memory/disk different | KeyStoreManager L91–132, L303–321 |
| Only server-manager tab is active; warning details expose Install | Correct existing docs, keep transient Yes distinct from durable Install | [CertificateManagerDlg](../../src/main/java/com/myjavaworld/jftp/ssl/CertificateManagerDlg.java#L368), L368–372; [SecurityWarningDlg](../../src/main/java/com/myjavaworld/jftp/ssl/SecurityWarningDlg.java#L104), L104–110; [CertificateDlg](../../src/main/java/com/myjavaworld/jftp/ssl/CertificateDlg.java#L64), L64–85, L115–135 |
| Server check uses leaf validity, exact CN comparison and a stored-certificate alias, with no default server-chain delegation | Standard chain/SAN/hostname validation changes require explicit policy and compatibility cases | [JFTPTrustManager](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPTrustManager.java#L57), L57–163 |

All active CertificateManagerDlg construction sites were checked: [JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L319) and [ManageCertificatesAction](../../src/main/java/com/myjavaworld/jftp/actions/ManageCertificatesAction.java#L51). No alternate client-tab activation path was found in this bounded all-caller search.

Preferences Cancel bypasses panel save, but Check Now is an immediate side effect. Save mutates the shared preference aggregate before disk writing. Favorite Close/Connect can continue after a reported save error. Current name/hash behavior also needs characterization before record/collection rewrites: Favorite's hashcode spelling does not override hashCode. These are evidence points, not automatic instructions to change behavior.

### 2.3 Java/UI/build — Luna repository-wide scan and focused bodies

A textual scan covered **182 production Java files** for applet/Apple/internal APIs, reflection, Thread stop/suspend/resume, finalizers/security-manager references and selected date/boxing uses. It is not an exhaustive compatibility proof.

- JFTPApplet and Apple integration remain. Windows excludes OSXAdapterOld only; active macOS integration uses reflective com.apple.eawt interfaces. Applet deployment is not part of the PRD desktop flows. Do not claim modern macOS/Linux support from Windows compilation.
- The scan found no sun/com.sun/jdk.internal references and no finalize/SecurityManager/Thread.stop/suspend/resume calls in that pattern scope. Deprecated Class.newInstance, boxed constructors, raw collections and SimpleDateFormat remain.
- **29 active custom-worker constructions** were identified: FTPSession 19, eight action classes one each, two properties dialogs one each. Commented code was excluded.
- Custom worker finished is queued only after normal construct return. Some GUIUtil/JOptionPane calls occur on worker/updater paths without a dispatch wrapper; no runtime thread-failure claim is made.
- FileChangeMonitor is a Swing Timer polling increasing last-modified values, not content hashes. Replacing it by WatchService is not automatically equivalent; overflow/coalescing/platform semantics would need their own checks.
- ZIP extraction resolves entry names beneath the target without a visible containment check. This is a source-based escape-risk finding, not an executed exploit.
- A blanket “empty ZIP files divide by zero” claim was withdrawn: stable empty input normally never enters the positive-read progress loop. Characterize unknown-size/concurrent modifications if changing progress code; no empty-file defect is established here.
- AutoUpdater returns after normal metadata processing, including blank/missing version. Only exceptions wait five minutes and retry; it is not a periodic successful-check loop.
- The application JAR is assembled at the distribution root while launcher templates target lib. This mismatch is source-confirmed, not a performed packaged-launch failure.

Primary sources: [SwingWorker](../../src/main/java/com/myjavaworld/gui/SwingWorker.java#L77), L77–148; [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L1320); [GUIUtil](../../src/main/java/com/myjavaworld/gui/GUIUtil.java#L95); [FileChangeMonitor](../../src/main/java/com/myjavaworld/util/FileChangeMonitor.java#L27), L27–97; [Zip](../../src/main/java/com/myjavaworld/zip/Zip.java#L219); [Unzip](../../src/main/java/com/myjavaworld/zip/Unzip.java#L134), L134–172; [AutoUpdater](../../src/main/java/com/myjavaworld/jftp/AutoUpdater.java#L56), L56–90; [POM](../../pom.xml#L83), [assembly](../../src/main/assembly/binary.xml#L20), [launcher](../../src/main/scripts/jftp.bat#L1).

## 3. Verified current release candidates

These are available stable candidates as of research, not “already compatible” or an instruction to use floating latest versions. Maven metadata may label a prerelease as release; stable versions were filtered explicitly.

| Item | Current/observed baseline | Verified stable candidate | Evidence |
| --- | --- | --- | --- |
| Runtime/language | release 8; limited historical JDK 21 run | Java 25 LTS; recommend Microsoft distribution, patched build/hash to lock at P1 | [Microsoft](https://learn.microsoft.com/en-us/java/openjdk/support), [LTS roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html) |
| Maven | Historical 3.9.12, no wrapper | 3.10.0 | [Downloads](https://maven.apache.org/download.cgi), [metadata](https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/maven-metadata.xml) |
| Wrapper plugin | Absent | 3.3.4 | [Metadata](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-wrapper-plugin/maven-metadata.xml) |
| Compiler | 3.13.0 | 3.16.0, not 4 beta | [Metadata](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/maven-metadata.xml) |
| Surefire / Failsafe | Unpinned; historical Surefire 3.2.5 | 3.6.0 / 3.6.0 | [Surefire](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/maven-metadata.xml), [Failsafe](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-failsafe-plugin/maven-metadata.xml) |
| Resources / JAR / Assembly | Existing roots; JAR 2.4, Assembly 2.3 | 3.5.0 / 3.5.1 / 3.8.0 | [Resources](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/maven-metadata.xml), [JAR](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/maven-metadata.xml), [Assembly](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-assembly-plugin/maven-metadata.xml) |
| JUnit | 3.8.1 | Jupiter/BOM 6.1.3 | [Metadata](https://repo.maven.apache.org/maven2/org/junit/junit-bom/maven-metadata.xml), [project](https://junit.org/) |
| FTP client | ftpapi 3.0.0 | Commons Net 3.13.0 candidate | [Release notes](https://commons.apache.org/proper/commons-net/changes.html), [metadata](https://repo.maven.apache.org/maven2/commons-net/commons-net/maven-metadata.xml) |
| Real local test server | No qualified server fixture | Apache FtpServer 1.2.1 candidate, test only | [Project](https://mina.apache.org/ftpserver-project/), [metadata](https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-core/maven-metadata.xml) |

Maven's publisher currently calls 3.10.0 stable and Maven 4.0.0-rc-7 preview. Compiler metadata exposes a 4.x beta, so selecting metadata's raw release field would not meet this proposal. Some Context7 “current JUnit” snippets still showed 5.13.4; current publisher/metadata and the upstream JUnit framework docs were used instead.

No source/dependency publishing task or new FTP deployment credential is selected. Review old SCM/deploy/release/wagon configuration before activation; changing it is not necessary to preserve the desktop user stories.

## 4. UI alternatives and recommendation

**Primary recommendation:** keep Swing through the first modernization phases. Separate application logic first. If a visual improvement is desired later, FlatLaf is the lowest-disruption experiment. If a full Java-based UI replacement is desired after that, JavaFX is the first prototype candidate. These are architectural judgments for this application, not measured speed/accessibility results.

| Option | Documented capability | Fit and potential benefit here | Cost / evidence gate | Recommendation |
| --- | --- | --- | --- | --- |
| Existing Swing | Part of [Java 25 desktop API](https://docs.oracle.com/en/java/javase/25/docs/api/java.desktop/javax/swing/package-summary.html) | Reuses current panes/dialogs, resources, Desktop integration and Java code | Existing coupling/EDT problems still need work; age does not prove replacement is necessary | Retain initially. |
| Swing + FlatLaf | [Swing look and feel, HiDPI and themes](https://www.formdev.com/flatlaf/) | Can modernize appearance without rebuilding the file-manager workflow | Still a visual change requiring focus, layout, custom-renderer, locale and screenshot QA | First optional appearance experiment, not phase one. |
| JavaFX | [Controls/CSS/properties](https://openjfx.io/), [Swing interoperability](https://openjfx.io/javadoc/26/javafx.swing/javafx/embed/swing/package-summary.html) | Stays in Java; view-state binding and styling offer a plausible long-term UI structure | Rewrite controls/dialogs/drag-drop/help integration; extra modules/platform artifacts; mixed UI has EDT and FX-thread boundaries | First full-replacement prototype, no adoption decision yet. |
| SWT/JFace | [Native toolkit](https://eclipse.dev/eclipse/swt/), [Display threading contract](https://help.eclipse.org/latest/topic/org.eclipse.platform.doc.isv/reference/api/org/eclipse/swt/widgets/Display.html) | Worth considering if native desktop integration/widget behavior is the actual driver | Different widget/resource lifecycle and platform-specific artifacts, substantial rewrite | Conditional shortlist, not a default upgrade. |
| Compose Desktop | [Swing interop](https://kotlinlang.org/docs/multiplatform/compose-desktop-swing-interoperability.html), [project](https://github.com/JetBrains/compose-multiplatform) | Declarative state-driven UI and Java-core reuse | Introduces Kotlin/build/rendering ecosystem; retaining Java logic does not retain Swing screens | Consider only with an explicit Kotlin/declarative-UI goal. |
| Tauri / Electron | [Tauri process model](https://v2.tauri.app/concept/process-model/), [Electron process model](https://www.electronjs.org/docs/latest/tutorial/process-model) | Relevant if web UI reuse is a strategic requirement | Web frontend plus IPC/sidecar or backend rewrite; Tauri uses system webviews, Electron bundles Chromium/Node | Lowest fit for current Java-only modernization; reassess only if the product direction changes. |

No exact future UI SDK version is selected. Resolve a supported JDK/toolkit pair and native package matrix at the prototype stage rather than pinning an untested version from a tutorial.

### Conditional UI roadmap

1. Extract view-independent commands, results and session state while Swing remains the production view.
2. Record representative Swing behavior and measurements on one controlled Windows environment and synthetic dataset.
3. Prototype the same tabbed two-pane browsing, sorting/filtering, transfer/progress/cancel, favorites, certificate Yes/No/View/Install and remote edit-back flows. Use actual local services, not a mocked UI-only demo.
4. Compare startup/first-listing time, working set, input responsiveness, keyboard/focus, drag/drop, scaling, localization and packaging. Report measured values; no benefit is assumed in advance.
5. Make a group decision using feature parity, measured benefit, maintenance cost and team constraints. Framework marketing or a screenshot alone is insufficient.
6. If approved, migrate one flow/workspace at a time with a rollback route. Mixed-toolkit interoperability is a transition mechanism, not proof of equivalent behavior or a desired permanent architecture.

## 5. Protocol alternatives

| Option | What is supported by evidence | Why / why not now |
| --- | --- | --- |
| Retain ftpapi behind a new port | Current API surface/profile strings and binary signatures are known; real behavior remains partly unverified | Recommended first extraction adapter: retain the existing provider/code path and profile identifiers while introducing an isolation boundary. Behavior compatibility still requires qualification. |
| Commons Net 3.13.0 | [FTP/FTPS API](https://commons.apache.org/proper/commons-net/apidocs/org/apache/commons/net/ftp/FTPSClient.html), parser family and current release | Best focused replacement candidate, subject to full used-surface qualification. |
| Commons VFS | [FTP/FTPS and other filesystem providers](https://commons.apache.org/proper/commons-vfs/filesystems.html) | Useful for a multi-filesystem product, but URI abstraction alone does not replace the current command/event/profile contract. Not selected. |

Do not copy defaults blindly. Commons Net's official FTPS documentation says hostname verification is not enabled by default; its exposed trust-manager controls require an explicit policy. Some retrieved generated examples contradicted each other about explicit/implicit mode and ports; those snippets were rejected in favor of official class docs/source. A current release does not itself establish secure configuration.

Keep ordinary FTP and the selected security/data-channel options where required. Do not implement an undisclosed cleartext retry after a certificate/TLS validation failure. Any opportunistic mode needs a reviewed downgrade policy and real-service cases.

## 6. Proposed behavior-impact register

These are **proposals**, not corrected descriptions of already-implemented behavior. The retrospective PRD retains its recorded limitations until a change is accepted. Approval of this research is not approval to implement every row.

| ID | Current observation | Proposed outcome for discussion | PRD impact / gate |
| --- | --- | --- | --- |
| B-00 | Launcher targets lib while application JAR is assembled at root | Runnable distribution with installed supported Java and original resources | Supports AC-01 without new product features; requires actual packaged/native proof. |
| B-01 | Reconnect can overlap disconnect; stale worker callbacks can outlive session state | Complete teardown before reconnect, current-generation delivery and owned cancellation | Intentionally changes AC-10 limitation and F01/F02 cleanup; preserve Abort/no-rollback distinction AC-22–25. |
| B-02 | Extraction target is formed from archive entry text without visible containment guard | Valid ZIP extraction preserved; reject traversal/absolute/drive/UNC/symlink/junction escape cases without writes outside the approved target | New malformed/malicious-input acceptance boundary for F05/US-11; source risk only, no exploit executed. |
| B-03 | Unzip can follow a handled failed download | Do not extract without a successful downloaded archive | Changes AC-33, requires an expected behavioral Red and accepted failure outcome. |
| B-04 | Server trust uses local CN/alias checks rather than default server-chain validation | Explicit standard chain/hostname checks and defined transient Yes versus durable Install handling | May change which warnings appear; map AC-60/61/89 and self-signed/SAN/expired/wrong-host cases before adopting. |
| B-05 | JKS cache can outlive path changes and diverge from disk after failed save | Define reload and failed-write/cache outcome without a silent format change | F09/F10 persistence/error behavior; separate from initial storage compatibility. |
| B-06 | Favorite/plain fallback, embedded-key sealing and raw preference credentials | Later explicit credential/storage design with backup, compatibility and rollback | AC-49–52/55/57; deferred by the initial-format constraint. Do not claim early encryption improvement. |
| B-07 | Interactive command prefix matching silently skips longer names and can be bypassed by leading whitespace | Evaluate parsed-command validation and actionable results separately | Changes AC-63, do not silently change it inside a client adapter migration. |
| B-08 | Updater has a fixed HTTP source, string version ordering and exception-only retries without explicit cancellation | Later explicit update-source/version/lifecycle policy while retaining entrypoints | F12/AC-66/88; no replacement endpoint selected or contacted, no automatic deletion of the feature. |
| B-09 | Local deletion can ignore an individual failure | Define reporting/partial-success behavior while preserving legitimate recursive/filter operations | Changes AC-39 and failure handling for US-13. Separate bug specification. |

Do not implement all rows together. Prioritize independently testable safety work after the necessary characterization and group agreement. Preserve successful use cases; do not assert success when both old/new implementations merely fail the same fixture.

## 7. Detailed stages and stopping rules

| Stage | Scope | Entry / exit evidence | Explicit exclusions |
| --- | --- | --- | --- |
| P0 | Reproduce current baseline; close critical FTP/FTPS/file/certificate/native coverage gaps with synthetic real fixtures | Actual discovered tests, real source/destination outcomes, native interaction and known defects recorded | No library/JDK/UI/storage rewrite. |
| P1 | Wrapper/build pins, JDK 25 qualification, then language target; B-00 as its own approved build fix | Separate compile/test/startup/package/native results, resources/old state preserved, warnings reviewed | No UI replacement, stored-format conversion, Maven 4 prerelease or unqualified profile removal. |
| P1b | Migrate existing tests to Jupiter separately | Same behavioral assertions and critical mutation sensitivity, valid synthetic child-JVM fixtures | No production rewrite to make the test fixture convenient. |
| P2 | Extract one core/port/adapter flow at a time | Green characterization, dependency boundary check, same current use-case outcomes | No speculative module/service split. Approved lifecycle fixes are separate commits with PRD disposition. |
| P3 | Commons Net qualification and profile-specific cutover | Real local-service/certificate/proxy/parser/content matrix; keep legacy for unqualified cases | No SFTP/cloud feature or fabricated AS/400 E2E evidence. |
| P4 | Optional UI evaluation/decision | Representative native prototypes, measured comparison and group choice | No selected replacement merely because a prototype renders. |
| P5 | Optional storage migration, runtime bundling, other platform lanes and update/help evolution | Separate decisions/specifications and platform/migration proof | Not a requirement to complete the initial Windows modernization. |

A small approved B-register fix can be scheduled earlier than P3 when its own tests/prerequisites exist. It must not be hidden in an otherwise behavior-preserving refactor.

After each major verified application step, assign one snapshot publisher and publish RepoMap/full Repomix/code graph as a new labeled set, with source-state checks and comparison to prior/original products. Do not overwrite initial snapshots or bypass exact-HEAD graph guards. This documentation research changes no analyzed application input and needs no new application snapshot.

## 8. Research limitations and discussion points

- Current framework/version documentation and release availability are not compatibility execution results.
- No new JDK, dependency, test framework, server, native package or UI prototype was installed/built/run here.
- Native QA prerequisites and real special-server/profile lanes remain to be established for implementation.
- Exact JDK patch/checksum is locked when P1 is implemented; do not use a floating vendor latest alias.
- Main questions for group review are the first bounded implementation stage, the B-register order/policy, and whether any optional UI benefit justifies a later prototype. No full UI rewrite, storage migration or implementation is approved by this report.

## 9. Documentation verification

The [machine-readable evidence](jftp-modernization-2026-10-16.evidence.json)
records the examined revision, source/document fingerprints, candidate versions,
resolved documentation IDs and check results. The reviewed baseline contains
21 user stories and 89 criteria, including the factual AC-89 correction. A
concurrent Sygnity appearance appendix in the working PRD belongs to a separate
task and was excluded from this task's commits and baseline fingerprint.
Independent application styling edits also began during finalization. Source
fingerprints in this report therefore identify the explicitly examined Git
revision, not a claim that the concurrent working tree remains identical.
Research source hashes use canonical Git-blob bytes. Older baseline manifests
retain their checkout-byte hashes, which can differ only through line endings;
their original working-tree match was completed before the concurrent edits.

All 32 ADR diagram sources parsed with Mermaid 12.2.0 and matched their fenced
blocks. Mermaid CLI 12.0.0 rendered six proposed views and the corrected
certificate sequence; all seven SVGs parsed as XML and were visually inspected
through two contact sheets. Browser geometry found no labels outside their
viewports. The other 25 baseline diagrams retain their previous fingerprints.
The selected proposed overview [SVG](../ADR/diagrams/008-01.svg) and standalone
Mermaid sources are tracked. Other previews/profiles/logs remain under ignored
target storage. GitHub/GFM is the intended renderer; its deployed Mermaid
version was not discovered or pinned.

The exact successful documentation-check commands used temporary helpers:

- `npm.cmd exec --yes --package=@mermaid-js/mermaid-cli@12.0.0 --package=mermaid@12.2.0 --package=jsdom@26.0.0 -- node target/modernization-validation/validate.cjs`
- `npm.cmd exec --yes --package=@mermaid-js/mermaid-cli@12.0.0 --package=mermaid@12.2.0 --package=jsdom@26.0.0 -- node target/modernization-validation/preview.cjs`
- `node target/modernization-validation/audit.cjs --baseline` and `node target/modernization-validation/audit.cjs`
- `git diff --quiet 469ecd58fe268dc759c91905c25ddcabf8782c8d -- src/main src/test pom.xml` for the tracked application inputs at verification time.
- `git diff --quiet 469ecd58fe268dc759c91905c25ddcabf8782c8d 284ab9f -- src/main src/test pom.xml` and Git-blob hashes for the pinned baseline after concurrent application edits began.
- `git diff --cached --check` before each explicit-path documentation commit.

The one-off helpers are removed after use. A Windows realpath compatibility
preload was limited to renderer child processes; Chrome used isolated profiles
and its normal sandbox. These are documentation checks. No application build,
tests, native Swing QA, new runtime/library qualification or service check was
performed by this task.
