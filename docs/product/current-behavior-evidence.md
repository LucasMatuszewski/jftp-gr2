# jFTP current-functionality evidence and consistency audit

Date: 2026-10-16. Application revision examined:
`dbdc47608d031c287debaa9ba4f7d94665842239`.
Companion to [the current-functionality PRD](../PRD.md).

This document records provenance and limitations, not product requirements or
an implementation/testing plan. Two delegated `gpt-6-luna` reviews inspected
bounded original definitions, actions, dialogs and callers for gaps in the saved
documentation. They did not build, run tests, start Swing or contact services.
The primary review reused the existing architecture, RepoMap, Repomix and graph
guides and checked their provenance rather than loading complete packs.

## How to interpret the baseline

- **Executed** means the particular historical observation recorded below; no
  new application execution was performed for this PRD.
- **Source** means a reachable implementation was inspected. Server effects,
  filesystem results and complete UI interaction are not thereby demonstrated.
- **Limitation** records current behavior without approving it as a future
  requirement. **Unknown** records an outcome not established as met.
- Unhandled failures can bypass normal completion paths. Descriptions of refresh,
  cleanup and status reset are conditional on the inspected return/error paths.

## Consistency and freshness audit

| Material | Check and result | Consequence |
| --- | --- | --- |
| [Architecture evidence](../design/jftp-architecture-2026-10-15.evidence.json) | All 21 recorded source hashes and 11 artifact hashes match. | Existing diagrams retain their recorded scope and source correspondence. |
| Application source and build descriptor | `git diff efa2596e7a0522ba0cc9d2439b7702e30a0b5524 HEAD -- src/main src/tests pom.xml` is empty at the examined revision. | No application change has invalidated the reviewed architecture source since its documented revision. |
| [Repomix provenance](../RepoMix/provenance.json) | 465 of 466 captured source-file hashes match; README is the only mismatch. | Selected application implementation/resources still match; the packed README is historical. |
| [RepoMap guide](../repo-maps/README.md) | Overview omits declarations; complete index covers captured declarations, not bodies. | Navigation only; neither report proves product behavior. |
| [Graph guide](../code-graph/README.md) | Saved graph records an older HEAD and has known missing/rejected edges. | No graph traversal was attempted or freshness guard bypassed. |
| [Architecture scope](../design/jftp-architecture-2026-10-15.md) | ZIP, remote editing and most dialogs are explicitly omitted. Luna checked those gaps and found no contradiction in the reviewed core architecture claims. | PRD coverage extends beyond the diagram scope through the evidence cards below. |
| [README](../../README.md) | Its unconditional encrypted-favorites claim exceeds the save implementation. | The maintained README now states the encryption fallback; historical platform/security claims remain qualified by the PRD. |
| Former PRD | Previously described only the minimal Windows startup exercise. | It is replaced in the same file; historical startup links are pinned to the former Git revision. |

Original generated snapshots were not changed or regenerated. This documentation
task leaves analyzed application inputs unchanged, so it does not require a new
application-context snapshot. The [snapshot catalogue](../context-snapshots/README.md)
continues to describe immutable historical products, not a graph for current HEAD.

## Evidence cards

Paths and line anchors below refer to original files at the examined application
revision. The [machine-readable source fingerprint](current-behavior-source-state.json)
records SHA-256 hashes for the cited source files. Ranges identify the inspected
scope; short code fragments identify the relevant operation, not a proposed design.

### E01

**Historical desktop startup; AC-01.** [Startup verification](../minimal-startup.md)
records a visible Windows frame and a later responsive process. Native focus/input
attempts failed; a terminal screenshot was rejected as application evidence.
Favorites interaction, normal Exit/restart and full desktop QA remain incomplete.
This supports window startup only, not the remaining user flows.

### E02

**Sessions; AC-02–04, F01 and main UI.** [JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L134)
L134–153 creates the menu/toolbar/tab layout and adds/selects `new FTPSession(this)`;
L188–194 closes/removes the selected session. [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L77)
L77–147 contains per-instance connection/navigation/filter state; L289–313 places
local/remote panes in a horizontal split, the log above and status below. Separate
fields support session separation but are not proof of concurrent-server isolation.

### E03

**Connection; AC-05–10, AC-83–85.** [ConnectionDlg](../../src/main/java/com/myjavaworld/jftp/ConnectionDlg.java#L114)
L114–127 and L641–713 approve only after validation, reject blank required fields
and ports outside 0–65535, and return no approved definition on Cancel. Implicit
port validation applies only when that security mode is selected. L303–327 and
L607–639 expose security/directory/advanced settings.
[RemoteHost](../../src/main/java/com/myjavaworld/jftp/RemoteHost.java#L33) L33–209
holds those settings; that is not successful FTPS negotiation.
[FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L593)
L593–704 configures the client, connects/logs in, runs commands and requests a
listing. The active-connection path calls `disconnect()` without waiting before
starting its new attempt. Inner connect/login failures clear the client; outer
configuration/command/listing failures do not share that cleanup. The
[architecture connection view](../design/jftp-architecture-2026-10-15.md#3-connect-authenticate-and-list)
explains the distinction. The separate
[disconnect path](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L1495)
L1495–1530 requests closure and clears session state on its handled paths;
reconnect at L701–704 resubmits the existing site definition.

### E04

**Browse/sort/filter wiring; AC-11–14.**
[FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L338)
L338–430 implements local/remote navigation and filtered listing; L101–116 and
L258–282 keep separate filters. [LocalPane](../../src/main/java/com/myjavaworld/jftp/LocalPane.java#L115)
L115–130, L295–311 and [RemotePane](../../src/main/java/com/myjavaworld/jftp/RemotePane.java#L107)
L107–120, L284–300 sort when data is set and toggle the first four column sorts.
Remote double-click navigation/open dispatch is at RemotePane L164–173, L233–245.

### E05

**Historical automated behavior; AC-15–17, AC-49–51, AC-55, AC-57, AC-74–75.**
[Startup verification](../minimal-startup.md#tests-and-behavioral-baseline) records
26 executed tests: five connection-configuration, seven local-filtering, seven
favorites-persistence and seven preferences-persistence cases. They use synthetic
local state, including later-process persistence checks, and report no failures,
errors or skips in the recorded final runs. Controlled mutations were detected
and reverted. These are historical results, not newly executed checks or FTP E2E.

Local filtering includes case/date boundaries and navigable directories.
Favorites include old-list handling and damaged-file errors. Preferences include
reloading configured values and damaged-file fallback. No claim is made that the
tests establish Save/Cancel GUI behavior or transfer correctness.

### E06

**Standard transfer paths; AC-18–20, AC-24–26.**
[FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L707)
L707–942 iterates selections, recursively visits filtered children and requests a
destination listing after normal/handled returns. File failures can be caught
inside the per-file operation, allowing another item to proceed. Directory/list
failure paths differ between upload and download; refresh is not proof of success.
L812–832 calls `client.download`; L884–921 calls `client.upload`. Their dependency
semantics for an existing destination were not reviewed here. No destination-byte,
overwrite/resume, rollback or real-server success evidence supports AC-26/GAP-01.

### E07

**Progress, abort and messages; AC-21–23, AC-64, AC-67–68.**
[JFTPToolBar](../../src/main/java/com/myjavaworld/jftp/JFTPToolBar.java#L291)
L291–308 enables Abort when connected, not only during a transfer.
[AbortAction](../../src/main/java/com/myjavaworld/jftp/actions/AbortAction.java#L53)
L53–75 sets the flag and separately requests protocol abort.
[FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L236)
L236–247 calculates average speed from transferred bytes/elapsed seconds;
L549–565 consumes progress/abort callbacks. [StatusBar](../../src/main/java/com/myjavaworld/jftp/StatusBar.java#L61)
L61–95 displays progress, speed and time. [StatusWindow](../../src/main/java/com/myjavaworld/jftp/StatusWindow.java#L52)
L52–99 exposes message categories and clears its bounded document at the limit.
Neither abort nor message display establishes immediate stopping, rollback or a
durable audit trail.

### E08

**Transfer modes; AC-27–29.**
[FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L224)
L224–234 selects extension mapping or fallback when Auto Detect is on; transfer
methods call this selection. [TransferModeMenu](../../src/main/java/com/myjavaworld/jftp/TransferModeMenu.java#L59)
L59–123 exposes Auto Detect, ASCII and Binary. [TransferModesPrefsPanel](../../src/main/java/com/myjavaworld/jftp/TransferModesPrefsPanel.java#L82)
L82–100 saves mappings/default. [JFTPPreferences](../../src/main/java/com/myjavaworld/jftp/JFTPPreferences.java#L99)
L99–129 defines initial binary fallback and text-extension mappings.

### E09

**Variants; AC-30–33, AC-69.** [DownloadAsAction](../../src/main/java/com/myjavaworld/jftp/actions/DownloadAsAction.java#L52)
L52–87 and [UploadAsAction](../../src/main/java/com/myjavaworld/jftp/actions/UploadAsAction.java#L52)
L52–87 require connection/selection and a name before submitting work.
[ZipAndUploadAction](../../src/main/java/com/myjavaworld/jftp/actions/ZipAndUploadAction.java#L59)
L59–126 packages filtered selection, attempts upload and offers archive deletion.
[DownloadAndUnzipAction](../../src/main/java/com/myjavaworld/jftp/actions/DownloadAndUnzipAction.java#L58)
L58–117 checks ZIP extension and dialog approval, attempts download and then
requests extraction with optional archive deletion. The download method handles
errors without returning a success result; extraction is attempted afterward
without confirming download success. These actions expose handled errors/refresh paths;
their wiring does not prove successful content delivery or extraction.

### E10

**Create/rename/delete; AC-34–39, AC-70–71, AC-76.** [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L973)
L973–1072 and L1206–1418 implement remote/local creation, rename and confirmed,
filtered recursive deletion. Local deletion ignores individual deletion return
values. [RenameLocalFileDlg](../../src/main/java/com/myjavaworld/jftp/RenameLocalFileDlg.java#L112)
L112–168 and [RenameRemoteFileDlg](../../src/main/java/com/myjavaworld/jftp/RenameRemoteFileDlg.java#L107)
L107–163 accept nonblank source/destination text without basename-only validation.
[RenameLocalFileAction](../../src/main/java/com/myjavaworld/jftp/actions/RenameLocalFileAction.java#L57)
L57–71 and [RenameRemoteFileAction](../../src/main/java/com/myjavaworld/jftp/actions/RenameRemoteFileAction.java#L56)
L56–70 forward that text. Paths can be attempted; successful cross-directory moves
were not demonstrated and no separate Move action was established in this scope.

### E11

**Properties/permissions; AC-40–42.** [LocalFilePropertiesDlg](../../src/main/java/com/myjavaworld/jftp/LocalFilePropertiesDlg.java#L156)
L156–330 displays information without a local permissions editor.
[RemoteFilePropertiesDlg](../../src/main/java/com/myjavaworld/jftp/RemoteFilePropertiesDlg.java#L214)
L214–253, L519–560 builds permission selections and a recursive choice.
[JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L325) L325–344 sends approved
changes to [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L1074)
L1074–1158, which issues server-specific `SITE CHMOD` requests with optional
filtered recursion. Properties do not call the separate rename/update method.

### E12

**Desktop integration/edit-back; AC-43–46, AC-78–81.**
[OpenLocalFileAction](../../src/main/java/com/myjavaworld/jftp/actions/OpenLocalFileAction.java#L52)
L52–73, [EditLocalFileAction](../../src/main/java/com/myjavaworld/jftp/actions/EditLocalFileAction.java#L52)
L52–68 and [PrintLocalFileAction](../../src/main/java/com/myjavaworld/jftp/actions/PrintLocalFileAction.java#L52)
L52–68 request desktop operations. [OpenRemoteFileAction](../../src/main/java/com/myjavaworld/jftp/actions/OpenRemoteFileAction.java#L54)
L54–95, [EditRemoteFileAction](../../src/main/java/com/myjavaworld/jftp/actions/EditRemoteFileAction.java#L54)
L54–90 and [PrintRemoteFileAction](../../src/main/java/com/myjavaworld/jftp/actions/PrintRemoteFileAction.java#L54)
L54–91 first obtain a temporary copy. [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L153)
L153–180 handles monitored-file change/upload approval;
[L1558–1585](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L1558) registers the
temporary copy. Desktop requests are conditional on desktop integration being
supported; unsupported integration can result in no desktop operation. This is explicit approval wiring, not demonstrated editor
compatibility, synchronization or conflict resolution.

### E13

**Favorites; AC-47–52, AC-72, AC-86–87.** [FavoritesDlg](../../src/main/java/com/myjavaworld/jftp/FavoritesDlg.java#L90)
L90–108, L163–250 and L335–340 wires Add/Edit/Delete/Connect, rejects duplicates
and attempts save on close/before connection. The
[save handler](../../src/main/java/com/myjavaworld/jftp/FavoritesDlg.java#L335)
catches/reports failure, allowing closing or connection to continue.
[FavoritesManager](../../src/main/java/com/myjavaworld/jftp/FavoritesManager.java#L64)
L64–85 and L112–137 accepts old lists and saves an encrypted object when possible
but includes a plain-list fallback. This contradicts unconditional encrypted
storage, not the architecture's already-qualified persistence description.

### E14

**Preferences/locale; AC-53–56 and F09.**
[PreferencesDlg](../../src/main/java/com/myjavaworld/jftp/PreferencesDlg.java#L61)
L61–110, L207–233 and L288–335 exposes category navigation and Save/Cancel paths.
[LocalePrefsPanel](../../src/main/java/com/myjavaworld/jftp/LocalePrefsPanel.java#L69)
L69–100 stores locale selection. [JFTPApplication](../../src/main/java/com/myjavaworld/jftp/JFTPApplication.java#L39)
L39–55 applies `Locale.setDefault(JFTP.prefs.getLocale())` before constructing the
window. This confirms startup application, correcting an initial incomplete
review that inspected the preferences panel alone. Immediate UI rebuilding is
not established. [ProxyPrefsPanel](../../src/main/java/com/myjavaworld/jftp/ProxyPrefsPanel.java#L209)
L209–235 exposes enabled/host/port/user/password settings; end-to-end proxy
compatibility is unverified. UI settings currently save appearance; commented
controls are not treated as available features.

### E15

**Certificates/trust; AC-58–61, AC-73.**
[CertificateManagerDlg](../../src/main/java/com/myjavaworld/jftp/ssl/CertificateManagerDlg.java#L198)
L198–355 wires selected-store X.509 import, details and confirmed deletion, with
handled errors. [JFTPTrustManager](../../src/main/java/com/myjavaworld/jftp/ssl/JFTPTrustManager.java#L76)
L76–99 checks trust/date/host failures, accepts a chain for that manager instance
on Yes, and rejects other choices. [SecurityWarningDlg](../../src/main/java/com/myjavaworld/jftp/ssl/SecurityWarningDlg.java#L104)
L104–123 offers inspection/decision. No unconditional secure-connection or permanent
trust-store modification guarantee follows from these paths.

### E16

**Commands; AC-62–63.** [ExecuteCommandDlg](../../src/main/java/com/myjavaworld/jftp/ExecuteCommandDlg.java#L69)
L69–127 tokenizes nonblank lines and rejects blank input.
[JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L294) L294–308 requires a
connected session. [FTPSession](../../src/main/java/com/myjavaworld/jftp/FTPSession.java#L1450)
L1450–1492 silently skips the prefixes listed in AC-63 after uppercase conversion
using the current default locale, then submits others in order. The line is not
trimmed before prefix matching: longer names with these starts are also skipped,
while leading whitespace bypasses that match. "Custom commands" does not mean all
entered commands are forwarded. Configured post-login commands are a separate
path described by E03.

### E17

**Help/update entrypoints; AC-65–66, AC-82, AC-88.**
[HelpMenu](../../src/main/java/com/myjavaworld/jftp/HelpMenu.java#L53) L53–115 wires
Contents, Tips, FAQ, Support, Feedback and platform-appropriate About.
[JFTP](../../src/main/java/com/myjavaworld/jftp/JFTP.java#L155) L155–163 checks the
saved update preference at window opening. [AutoUpdater](../../src/main/java/com/myjavaworld/jftp/AutoUpdater.java#L31)
L31–91 attempts the historical update endpoint; [SoftwareUpdatePrefsPanel](../../src/main/java/com/myjavaworld/jftp/SoftwareUpdatePrefsPanel.java#L61)
L61–80 exposes the preference and Check Now. No endpoint was contacted and no
help launch or update-service availability was verified.

### E18

**Drag and drop; AC-77.**
[DnDTransferHandler](../../src/main/java/com/myjavaworld/jftp/DnDTransferHandler.java#L49)
L49–74 and L89–99 invokes the standard upload/download actions. The panes attach
the handler at [LocalPane L413–419](../../src/main/java/com/myjavaworld/jftp/LocalPane.java#L413)
and [RemotePane L381–388](../../src/main/java/com/myjavaworld/jftp/RemotePane.java#L381).
This dispatch uses the current destination, not a new target directory inferred
from the drop position. No native drag/drop interaction was performed.

## Documentation verification

Required scope is document structure, identifier/reference consistency, source
correspondence, diagram syntax and a focused diff. No application build, test or
startup is required for this documentation-only change. Historical execution
commands/results remain in the linked startup record rather than being reported
as new results. Future product decisions should use the stable US/AC/GAP IDs;
future evidence should update status without silently rewriting historical proof.

Documentation QA passed on 2026-10-16:

- 21 stories, 88 uniquely identified criteria and 12 flows; every criterion is
  referenced by a story and every criterion's evidence ID exists.
- 93 local links, including 70 source-line anchors, and three pinned historical
  Git links resolve within the checked scope.
- All 43 cited source fingerprints match. The 21 architecture-source and 11
  architecture-artifact fingerprints still match; the Repomix comparison remains
  465/466, with README the sole expected historical mismatch.
- The PRD's single flowchart parses with Mermaid 12.2.0 and references all flows.
  This is syntax validation, not a claim of rendered-layout inspection.

The exact parser/structure command was:

```powershell
npm.cmd exec --yes --package=mermaid@12.2.0 --package=jsdom@26.0.0 -- node target/prd-validation/validate.cjs
```

The one-off validator was kept under ignored `target/` and removed after use;
its result remains an ignored local artifact. The initial temporary-tool install
emitted an upstream `whatwg-encoding@3.1.1` deprecation notice from the jsdom
dependency tree; no application/project dependency was added or changed.
`git diff --cached --check` is the final whitespace check before committing the
explicit documentation paths. No application build, tests or manual QA were
rerun for this documentation-only change.
