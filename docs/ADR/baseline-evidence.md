# ADR baseline evidence and verification ledger

Date: 2026-10-16. Application source revision:
`b5e7657bac97ae567533d74ae487e5ae713379c8`.
Entry point: [ADR-000](000-main-architecture.md).

This is supporting evidence, not a ninth architectural decision. The eight ADRs
record the existing system; their dates identify documentation, not the dates
when the original authors made their choices. Original rationale/alternatives
are unknown except where the startup record documents a later minimal repair.

## Reused context and freshness

- [Source-checked architecture](../design/jftp-architecture-2026-10-15.md) and
  [its manifest](../design/jftp-architecture-2026-10-15.evidence.json): all 21
  source hashes and 11 artifact hashes match this task's source state.
- [PRD evidence](../product/current-behavior-evidence.md) and
  [source state](../product/current-behavior-source-state.json): all 43 cited
  source fingerprints match. Existing claims retain their evidence limits.
- [RepoMap guide](../repo-maps/README.md) and selected overview declarations
  supply navigation. They do not provide complete bodies or resolved dispatch.
- [Full-code Repomix guide](../RepoMix/README.md): 465/466 captured file hashes
  match, with README the historical difference. The full pack is selected text
  implementation context, not dependencies or runtime proof. Its compressed
  counterpart is not used to establish behavior.
- [Graph guide](../code-graph/README.md): older HEAD and known omitted/rejected
  edges prevent treating it as a current call graph. No guard was bypassed and
  no historical graph was relabeled or regenerated.
- `git diff --quiet b5e7657 -- src/main src/test pom.xml` confirms no application,
  test or build-descriptor changes. The actual test root is `src/test/java`.
  The earlier product ledger's `src/tests` diff path did not cover that actual
  test tree; this task checks the correct path and preserves the earlier record.
- The [snapshot policy](../context-snapshots/README.md) requires no new context
  snapshot for unchanged application inputs. Original generated products remain
  byte-preserved.

Two read-only Luna reviews supplied bounded source checks for additional build,
packaging, models, store/security and monitor facts, then reviewed the drafts.
No application build, tests, Swing launch, FTP service or updater request was
executed. Browser rendering of diagrams is documentation validation only.

## Source evidence cards

The [machine-readable manifest](baseline-evidence.json) records source hashes,
diagram provenance and documentation-check results. The following ranges are
original-source scope, not implementation instructions. No secret/key/password
values or personal profile contents were read or reproduced.

| ID | Original source and range | Supporting observation / safe identifying fragment | Used by |
| --- | --- | --- | --- |
| B01 | [pom.xml](../../pom.xml#L3), L3–10, L64–109 | One JAR artifact, ftpapi 3.0.0, JavaHelp 2.0.05, JUnit 3.8.1 test scope, five resource roots, release 8. | 000, 001, 006, 007 |
| B02 | [Build plugins/profile](../../pom.xml#L110), L110–208 | Main-Class JFTPApplication, lib classpath prefix, configured assembly/package phase, narrow Windows exclusion. | 006 |
| B03 | [Binary assembly](../../src/main/assembly/binary.xml#L5), L5–43 | Application JAR at archive root, dependencies in lib, filtered scripts at root. | 006 |
| B04 | [Windows launcher](../../src/main/scripts/jftp.bat#L1), [shell launcher](../../src/main/scripts/jftp.sh#L1) | Both templates target an application JAR inside lib, differing from the descriptor's root placement. | 006 |
| B05 | [Bootstrap](../../src/main/java/com/myjavaworld/jftp/JFTPApplication.java#L28), L28–67 | Locale/look and feel precede frame construction, visibility and first session. | 000, 001, 002 |
| B06 | [Frame/session/state](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L65), L65–153, L188–194, L512–568 | Static data-home/preference capture, tab creation/removal and preference object streams. | 000, 002, 004 |
| B07 | [Session](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L70), L70–180, L224–327 | Mutable UI/client/filter state, progress, monitor and close lifetime. | 000, 002, 005 |
| B08 | [Connection and transfer](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L593), L593–942 | Reflection, distinct initialization errors, serial selected operations and recursion. | 002, 003 |
| B09 | [Custom worker](../../src/main/java/com/myjavaworld/gui/SwingWorker.java#L123), L123–148 | Normal construct return precedes invokeLater completion, unchecked escape can bypass it. | 002 |
| B10 | [Connection model](../../src/main/java/com/myjavaworld/jftp/RemoteHost.java#L33), L33–225; [Favorite](../../src/main/java/com/myjavaworld/jftp/Favorite.java#L25), L25–53 | Serializable settings and named Favorite subtype with case-insensitive name equality. | 000, 003, 004 |
| B11 | [Preference model](../../src/main/java/com/myjavaworld/jftp/JFTPPreferences.java#L38), L38–129 and accessors through L457 | Serializable aggregate with UI/connection/transfer/proxy/security data and password arrays. | 004 |
| B12 | [Favorite manager](../../src/main/java/com/myjavaworld/jftp/FavoritesManager.java#L64), L64–85, L112–137, L170–186 | Legacy-list rewrite, sealed-object save or plain-list fallback. Embedded key value deliberately omitted. | 004 |
| B13 | [Favorite dialog](../../src/main/java/com/myjavaworld/jftp/FavoritesDlg.java#L232), L232–250, L325–341 | Save errors are handled before close/connection continues. | 004 |
| B14 | [JKS manager](../../src/main/java/com/myjavaworld/jftp/ssl/KeyStoreManager.java#L36), L36–132, L150–192, L240–250, L303–321 | Static caches, missing-store creation, immediate persistence and alias replacement. | 004 |
| B15 | [SSL context](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPSSLContext.java#L37), L37–44; [key manager](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPKeyManager.java#L41), L41–48; [trust manager](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPTrustManager.java#L57), L57–99 | Context delegates key/trust decisions, warning acceptance caches a chain without store import. | 003, 004 |
| B16 | [Monitor](../../src/main/java/com/myjavaworld/util/FileChangeMonitor.java#L34), L34–97; [temp-copy flow](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L1540), L1540–1601 | One-second timestamp-increase sampling, mapping, delete-on-exit registration and close/stop behavior. | 002, 005 |
| B17 | [JavaHelp adapter](../../src/main/java/com/myjavaworld/jftp/JFTPHelp2.java#L40), L40–70; [resource loader](../../src/main/java/com/myjavaworld/util/ResourceLoader.java#L29) | Packaged locale-specific help and resource-bundle/image boundary. | 001, 006 |
| B18 | [Test fixture](../../src/test/java/com/myjavaworld/jftp/BehaviorTestCase.java#L1), [persistence fixture](../../src/test/java/com/myjavaworld/jftp/PersistenceTestCase.java#L1), [StateProbe](../../src/test/java/com/myjavaworld/jftp/StateProbe.java#L1) | Synthetic profile isolation and later-process persistence probing. | 007 |
| B19 | [Configuration suite](../../src/test/java/com/myjavaworld/jftp/ConnectionConfigurationTest.java#L1), [filter suite](../../src/test/java/com/myjavaworld/jftp/LocalFilteringTest.java#L1), [favorites suite](../../src/test/java/com/myjavaworld/jftp/FavoritesPersistenceTest.java#L1), [preferences suite](../../src/test/java/com/myjavaworld/jftp/PreferencesPersistenceTest.java#L1) | Four suites, 5+7+7+7 historically executed cases. | 007 |
| B20 | [AutoUpdater](../../src/main/java/com/myjavaworld/jftp/AutoUpdater.java#L33), L33–90; [Check Now](../../src/main/java/com/myjavaworld/jftp/SoftwareUpdatePrefsPanel.java#L48), L48–78; [window opening](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L155), L155–163 | Automatic initial delay, independent manual check, fixed public HTTP properties URL, string version ordering, missing-result silence and five-minute exception retry. Endpoint not contacted. | 000, 001 |

Previously checked action/dialog ranges for file operations, ZIP, Desktop,
commands, sorting and filters remain in the linked PRD evidence cards E03–18.
The ADR manifest includes those cited application hashes as reused source scope.

## Technology documentation audit

Context7 IDs below were returned by resolution and then queried; none are guessed.
Queries were scoped separately to lifecycle, compiler release, Swing dispatch,
serialization, JSSE, Desktop, resource encoding, test discovery and legacy testing.

| Verified ID or official fallback | Source and scope |
| --- | --- |
| `/websites/maven_apache` | [Maven lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html), general phases. |
| `/apache/maven-compiler-plugin` | [Release contract](https://maven.apache.org/plugins/maven-compiler-plugin/examples/set-compiler-release.html), current docs do not change pinned project version. |
| `/websites/maven_apache_surefire_maven-surefire-plugin` | [Surefire test goal/discovery](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html), actual historical runner from logs. |
| `/websites/oracle_en_java_javase_21_api` | [Swing threading](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/package-summary.html), [Desktop](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Desktop.html), [SSLContext](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/javax/net/ssl/SSLContext.html), [PropertyResourceBundle](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/PropertyResourceBundle.html). |
| `/websites/oracle_javase_8_api` | [ObjectInputStream](https://docs.oracle.com/javase/8/docs/api/java/io/ObjectInputStream.html), legacy API reference. |
| `/junit-team/junit4` | [Legacy TestCase article](https://github.com/junit-team/junit4/blob/main/doc/testinfected/testing.htm), supplemental documentation only, not a change from JUnit 3.8.1. |
| ftpapi official fallback | [Version 3.0.0 vendor artifacts](https://www.jmethods.com/ftpapi/download.html). Two Context7 names returned unrelated matches; none used. Vendor API HTML could not be retrieved. |
| JavaHelp official fallback | [Official project](https://javaee.github.io/javahelp/) and [archived source](https://github.com/javaee/javahelp). No Context7 match; project dependency version comes from POM. |

Current Java resource documentation specifies UTF-8 with fallback behavior for
PropertyResourceBundle input streams, unlike historical Java 8 conventions.
This does not establish that existing localized UI strings are correct on every
runtime. Resource bytes were not transcoded or rewritten.

## Historical execution, not a new run

[Startup verification](../minimal-startup.md) records compilation, 26 tests and
limited visible startup separately, with incomplete native/manual QA. Existing
ignored `target/verification/commit-tests.log` L24–41 and `final-tests.log` L36–53
show Surefire 3.2.5, JUnit3Provider and the 26/0/0/0 final counts. These logs do
not pin the plugin in the POM or prove protocol/native/manual behavior.

## Documentation validation scope

All ADR files follow their main/granular template, contain decisions, consequences,
review triggers, change history, test scenarios and scoped technical acceptance
criteria. Implementation snippets are excluded. Source matching, local links,
PRD coverage, standalone/fenced diagram equality, real Mermaid parsing, local
rendering and visual review are recorded in the manifest after validation.
Parser/render success is not application runtime or architectural correctness.

### Recorded results, 2026-10-16

- Eight ADR records, 17 decision IDs and 35 technical acceptance criteria passed
  template/identifier checks. All 21 PRD stories have area coverage, and all 12
  PRD flows are identified in sequence coverage.
- 135 local links and 33 source-line anchors resolve in the checked scope.
  All 65 combined cited source hashes match. The preserved architecture and PRD
  source/artifact checks also pass, with README the sole historical Repomix mismatch.
- All 26 final Mermaid sources parse with Mermaid 12.2.0. Mermaid CLI 12.0.0
  rendered all 26 to SVG, all 26 SVGs parse as XML, and all 26 fenced blocks match
  their standalone sources. All 16 sequence sources were checked for raw semicolons.
- Seven final PNG contact sheets were inspected, covering all 26 rendered views.
  A browser geometry check found no label outside an SVG viewport. Wide flowcharts
  and long notes were adjusted before final review.
- The selected overview SVG and all standalone Mermaid sources are tracked under
  `docs/ADR/diagrams/`. Other SVGs, previews, profiles and logs remain under ignored
  `target/adr-validation/`. Diagram sources/selected SVG use explicit LF attributes.
- Target host is GitHub/GFM; its deployed Mermaid version was not pinned or
  discovered. Local parser/render results do not certify every older plugin.

Exact document-check commands used temporary helpers:

- `npm.cmd exec --yes --package=@mermaid-js/mermaid-cli@12.0.0 --package=mermaid@12.2.0 --package=jsdom@26.0.0 -- node target/adr-validation/validate.cjs --reuse-rendered`
- `npm.cmd exec --yes --package=@mermaid-js/mermaid-cli@12.0.0 --package=mermaid@12.2.0 --package=jsdom@26.0.0 -- node target/adr-validation/preview.cjs`
- `git diff --cached --check` for the explicitly staged documentation.

The helpers are removed after use. Reused SVGs were accepted only when the input
hash matched already-rendered sources; changed diagrams were rerendered. A
temporary realpath compatibility preload was scoped to rendering processes, not
installed in the application or global environment. The tool dependency tree
emitted a `whatwg-encoding@3.1.1` deprecation notice; no application dependency was
added or changed. No Maven/application test command, desktop launch, real FTP or
updater call was made, and no new runtime acceptance status is asserted.
