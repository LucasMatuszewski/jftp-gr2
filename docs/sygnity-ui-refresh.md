# Sygnity appearance refresh

2026-10-16. Scope: [PRD AC-90–93](PRD.md#13-agreed-sygnity-appearance-refresh-2026-10-16). This is a small presentation change to the existing Swing desktop, using the supplied Sygnity assets. No dependency, protocol, persistence format, action handler, localized string or button icon was changed.

## Design and implementation

| Area | Change and reason |
| --- | --- |
| Top toolbar | White surface, a 2 px cyan bottom rule, and 8 px vertical / 12 px horizontal insets give the dense action strip some space. All 20 original buttons retain their order, icon assignments, tooltips and listeners. Enabled-state logic is unchanged. |
| Logo | The original `assets/logo.svg` is rendered faithfully to a transparent 480 × 144 PNG under the existing Maven resource root. Swing paints it at 120 × 36 logical pixels, preserving the 10:3 aspect ratio and extra resolution for display scaling. Flexible space pushes it to the right; its accessible name is “Sygnity”, and it adds no keyboard stop or action. |
| Surfaces and typography | White lists, fields and menu surfaces; `#F9F9F9` panels; `#F1F1F1` headers; `#3A3A3A` text. Standard controls use the logical SansSerif font at 13 px, regular weight. Montserrat is absent from the supplied font assets, so there is no runtime font download or new font dependency. Existing log styling remains in place. |
| Accent colors | The supplied `#00AEEF` cyan marks the toolbar, progress fill and selected-tab highlight. The supplied `#1E73BE` blue supports focus/title accents. Selection uses a derived pale cyan `#DDF3FD` with graphite text, avoiding white text on bright cyan. Derived gray `#DDE2E5` separates surfaces. |
| Tables | Header labels are explicitly opaque so the chosen background actually paints. Headers use the table-header font and a thin bottom/right divider with 6 × 8 px padding. Sorting icons and cell-rendering data remain unchanged. The existing font-based row-height calculation is unchanged. |
| Status bar | Etched and lowered bevels become thin separators and small padded cells. Status text, progress values, speed, elapsed time and security indicators use their existing update methods. |
| Look and feel | `SygnityStyle.install()` sets developer defaults before `JFTP` constructs its content. The saved look-and-feel class remains selected by the existing bootstrap; no appearance setting is rewritten. Metal gradients are flattened where they would obscure the selected surface colors. Native themes may paint some controls differently. |

Production edits are limited to the new `SygnityStyle`, one installation call in `JFTP`, toolbar presentation, header rendering and status-bar borders. The packaged PNG uses the already configured resource root; the Maven descriptor is unchanged by this task. Existing CRLF files retain CRLF.

## Screenshot review

These are native X11 window captures of the real Swing application under WSLg, not mockups or browser renderings. Main comparison captures both have a 1100 × 760 client area. Synthetic file timestamps differ between the isolated before/after profiles. Pane dividers were adjusted with native dragging for the comparison; their production layout code is unchanged. Captures contain the client area rather than operating-system title-bar decorations.

| State | Evidence |
| --- | --- |
| Before | [before.png](screens/sygnity-refresh/before.png) |
| After | [after.png](screens/sygnity-refresh/after.png) |
| Pale cyan file selection | [selection.png](screens/sygnity-refresh/selection.png) |
| Two sessions | [two-sessions.png](screens/sygnity-refresh/two-sessions.png) |
| Narrow 900 × 700 client area | [narrow.png](screens/sygnity-refresh/narrow.png) |
| Connection form / validation | [connect.png](screens/sygnity-refresh/connect.png), [connection-validation.png](screens/sygnity-refresh/connection-validation.png) |
| Preferences / About | [preferences.png](screens/sygnity-refresh/preferences.png), [about.png](screens/sygnity-refresh/about.png) |
| Standalone restart | [restarted.png](screens/sygnity-refresh/restarted.png) |
| Real empty local folder | [local-folder.png](screens/sygnity-refresh/local-folder.png) |
| Missing external CSV viewer | [external-viewer-unavailable.png](screens/sygnity-refresh/external-viewer-unavailable.png) |

Visual assessment: the logo is clear and fits beside all original actions at both tested widths. White space in the header, regular-weight labels and quieter table/status borders reduce the heavy gray framing. Pale cyan selection retains dark readable filenames, and disabled toolbar icons remain distinguishable. At 900 px, file columns retain their existing horizontal scrolling rather than wrapping or hiding controls. The original small bitmap icons and native Swing control shapes still give the app a legacy character; replacing them would exceed the requested styling scope. Brand color is concentrated in the header and interaction states rather than filling the working panes.

## Automated verification

The temporary Linux toolchain is OpenJDK 21.0.12.1 and the existing Maven 3.9.12 distribution. Existing dependencies were copied to `/tmp/jftp-ui-runtime/maven-cache`; none were upgraded. `-Pwindows` explicitly selects the existing compiler exclusion of `OSXAdapterOld.java`, whose historical Apple APIs are absent from this JDK. This is a session command choice, not a build change or Windows runtime test.

Exact setup for the commands used:

```bash
source /tmp/jftp-ui-runtime/env.sh
MVN=/mnt/c/Users/BiuroEdukey/.m2/wrapper/dists/apache-maven-3.9.12/59fe215c0ad6947fea90184bf7add084544567b927287592651fda3782e0e798/bin/mvn
```

The original source was first run with the new presentation tests. An incorrect expected JavaHelp listener name in the characterization fixture was corrected before production edits. The corrected Red command was:

```bash
bash "$MVN" -B -ntp -o -s /tmp/jftp-ui-runtime/settings.xml -Dmaven.repo.local=/tmp/jftp-ui-runtime/maven-cache -Pwindows -DargLine=-Djava.awt.headless=true compiler:testCompile surefire:test
```

Result: **29 executed, exactly 2 expected assertion failures, zero errors/skips**: the toolbar lacked its Sygnity wordmark and the logo resource was absent. All 26 existing behavior tests and the original-action characterization passed. Offline plugin-prefix lookup also emitted warnings for uncached, unused release/deploy plugins; these were not behavioral failures.

After implementation, compilation and tests were separate checks:

```bash
bash "$MVN" -B -ntp -o -s /tmp/jftp-ui-runtime/settings.xml -Dmaven.repo.local=/tmp/jftp-ui-runtime/maven-cache -Pwindows compile
bash "$MVN" -B -ntp -o -s /tmp/jftp-ui-runtime/settings.xml -Dmaven.repo.local=/tmp/jftp-ui-runtime/maven-cache -Pwindows -DargLine=-Djava.awt.headless=true test
```

Both returned **BUILD SUCCESS**. **29 tests executed, zero failures/errors/skips**. The three new tests cover original action ordering and icons/tooltips remaining present, logo placement without button overlap or an added keyboard stop, and packaged logo aspect ratio/transparency. No mocks were created. Existing obsolete Java 8 target, deprecated API and unchecked-operation notices remain; no new compilation warning was introduced.

## Real desktop QA and limits

Startup used `StateProbe prepare-desktop` with matching new `user.home` and `jftp.qa.home` paths, followed by the real `JFTPApplication`. Profiles `/tmp/jftp-ui-runtime/before-profile` and `/tmp/jftp-ui-runtime/after-profile` contain only synthetic files, English defaults and disabled update checking. No external FTP service, real credentials, favorites or personal certificate store was accessed.

The native QA driver launches the actual `JFTPApplication` and observes its public controls on the EDT. It uses `java.awt.Robot` mouse/key input and XTest input via `xdotool`; it never calls `doClick`, substitutes action results or adds a production test path. Screenshots use X11 `XGetImage` on the actual returned window ID. Root-window screenshots do not work in this WSLg session. The QA helper's initial incorrect tooltip lookup was corrected from observed control metadata; it was not an application error.

Verified visually and with actual state changes: startup; toolbar disabled/enabled state after selection; pale cyan file selection; opening a local folder with Enter and returning with the existing parent button; creating a second session and closing it through the existing menu mnemonic; Connect dialog, native Tab moving focus from Host Name to User Name, empty-host validation, error dismissal and Cancel; Preferences open/Cancel; About open/Close; native splitter dragging and narrow-window layout; normal Exit through the FTP menu and standalone restart from persisted synthetic settings. Required screenshots were inspected directly by the orchestrator; Luna supplied only a read-only source inventory.

Opening the synthetic `image.csv` through the existing Open action reported `java.io.IOException: Failed to show URI:file:/tmp/jftp-ui-runtime/after-profile/synthetic-files/image.csv` because this environment has no associated CSV viewer. The application's error dialog and stack trace were inspected and the error dismissed normally. The style layer does not touch desktop file-opening code; external viewer launch remains unverified here. FTP/FTPS transfer behavior and packaged-distribution startup were outside this presentation change and were not tested.

Windows interop attempts returned `UtilAcceptVsock: accept4 failed 110`, so the verified desktop environment is Linux Swing/Metal under WSLg. The Windows native look and feel and alternate display scales remain unverified. The selected LAF and icon asset resolution are preserved by source, but native platform painting should be reviewed on Windows before claiming cross-platform visual parity.

The standalone restart command (no QA driver or test classes) was:

```bash
source /tmp/jftp-ui-runtime/env.sh
java -Duser.home=/tmp/jftp-ui-runtime/after-profile -cp 'target/classes:/tmp/jftp-ui-runtime/maven-cache/com/myjavaworld/ftpapi/3.0.0/ftpapi-3.0.0.jar:/tmp/jftp-ui-runtime/maven-cache/javax/help/javahelp/2.0.05/javahelp-2.0.05.jar' com.myjavaworld.jftp.JFTPApplication
```

It restored the synthetic initial directory and window size, displayed the logo, and produced no startup-log output. The application is left running for review in task-owned tmux session `jftp-ui-review` (owner: this Codex task), using only the synthetic profile. Finished build/snapshot sessions and the baseline application session were closed.

Local logs, QA helper sources and tool environment are saved under ignored `target/verification/sygnity-refresh/`; screenshots use the repository's existing ignored `docs/screens/` convention. The initial implementation was verified before publication. The subsequent user instruction authorizes a focused commit, push and pull request; unrelated working-tree changes are excluded.

## Source navigation snapshot

[Sygnity UI snapshot](context-snapshots/sygnity-ui-90f300211437/README.md) contains new RepoMap, full and compressed Repomix profiles, and a code-only graph from a single frozen source manifest. The original snapshot's file hashes were verified unchanged. This records source navigation, not additional runtime coverage.
