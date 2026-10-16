# Minimal Windows startup verification

2026-10-15, working copy based on `cdc95025ac74098f129bfd9cdcd613fa6348c8d0`.
Scope: [historical startup PRD](https://github.com/LucasMatuszewski/jftp-gr2/blob/dd05dd443efd3151e0d0085eca7e356566ad0bda/docs/PRD.md). **Compilation and all 26 behavior tests pass. The real
desktop window starts. Full native/manual desktop QA is still incomplete.**

## Minimal change

Production Java and resource bytes are unchanged. `pom.xml` changes only:

- jMethods dependency repository from HTTP to HTTPS: Maven 3.9.12 blocks its old
  HTTP URL (`maven-default-http-blocker`).
- Compiler Plugin 2.4 / source-target 1.5 to Compiler Plugin 3.13.0 / `release 8`:
  Microsoft JDK 21.0.10 rejects source/target 5. The Java 8 target limits the
  bootstrap change without a runtime/API modernization.
- An OS-activated Windows profile excludes only `OSXAdapterOld.java`. Compilation
  otherwise fails because `com.apple.eawt.ApplicationAdapter/ApplicationEvent`
  are absent. The active reflective adapter remains; it is outside Windows flow.

JUnit stays at 3.8.1, ftpapi at 3.0.0, JavaHelp at 2.0.05. No serialization,
protocol, application logic, localization or UI redesign was introduced.

## Tests and behavioral baseline

| Suite | Cases | Observations covered |
| --- | ---: | --- |
| ConnectionConfigurationTest | 5 | Defaults, null/whitespace handling, invalid/custom ports, command order, FTPS serialization |
| LocalFilteringTest | 7 | Actual files, inclusion/exclusion, case, date boundaries, hidden attribute, navigable directories |
| FavoritesPersistenceTest | 7 | First use, order/content, edit/remove/clear, older serialized lists, damaged files, another JVM |
| PreferencesPersistenceTest | 7 | First use, transfer/connection/UI/certificate/proxy data, replacement, damaged-file fallback, another JVM |

Tests were written before the build repair and first run through an external
POM against unchanged application sources. They use public inputs/results,
real synthetic files, unique temporary homes and no mocks. Persistence tests
refuse to use another initialized profile. Child-JVM probes check disk state
rather than a process-local cache. They do not establish FTP transfer correctness.

Controlled behavioral mutations were then checked on the unchanged source:
fallback port 22 (1 failure), inverted file acceptance (7 failures), dropped
favorite addition (2 failures), discarded saved preference values (5 failures).
Each run had **zero setup errors**. Every mutation was reverted byte-for-byte in
`finally`; the complete original-source suite subsequently passes. Build or
environment failures are not counted as a behavioral TDD Red.

An early `CodexSandboxOffline` execution could not use Windows shell folders:
`Cannot invoke "sun.awt.shell.Win32ShellFolder2.getChildByPath(String)" because
"desktop" is null`. After continuation the executor used `AzureAD\BiuroEdukey`;
the same tests passed without an application workaround. That observation does
not establish which host setting changed between turns.

## Reproduce build and tests

Use JDK 21 and Maven 3.9.12. This checkout does not have a Maven wrapper.

```powershell
$env:JAVA_HOME = 'C:\Program Files\Microsoft\jdk-21.0.10.7-hotspot'
mvn -B -ntp compile
mvn -B -ntp '-DargLine=-Djava.awt.headless=true' test
```

In this session `mvn` was absent from PATH. The actual executable was:

```text
C:\Users\BiuroEdukey\.m2\wrapper\dists\apache-maven-3.9.12\59fe215c0ad6947fea90184bf7add084544567b927287592651fda3782e0e798\bin\mvn.cmd
```

Both commands also used the following session-only arguments (no global Maven
settings changed):

```text
-s C:\Users\BiuroEdukey\AppData\Local\Temp\jftp-gr2-maven-settings.xml
-Dmaven.repo.local=C:\Users\BiuroEdukey\AppData\Local\Temp\jftp-gr2-maven
```

The temporary settings route dependency downloads through the session proxy.
Logs are local ignored artifacts: `target/verification/compile.log`,
`final-tests.log`, `mutation-*.log`, plus `target/surefire-reports/`.
Compilation, test execution and GUI startup are separate results. JDK warnings
about the obsolete Java 8 target and existing deprecated/unchecked legacy code
remain visible; this exercise does not clean up those APIs or raise the target.

## Safe desktop launch

Run in a normal interactive Windows session. After `test-compile`, use the two
runtime JARs from the session cache above (or their locations in your Maven
repository). Preparation creates synthetic files, disables update checking and
does not connect to FTP services:

```powershell
$cache = 'C:\Users\BiuroEdukey\AppData\Local\Temp\jftp-gr2-maven'
$cp = "target\classes;target\test-classes;$cache\com\myjavaworld\ftpapi\3.0.0\ftpapi-3.0.0.jar;$cache\javax\help\javahelp\2.0.05\javahelp-2.0.05.jar"
$profilePath = Join-Path (Get-Location) ('target\qa-profile-' + [guid]::NewGuid().ToString('N'))
& "$env:JAVA_HOME\bin\java.exe" "-Duser.home=$profilePath" "-Djftp.qa.home=$profilePath" -cp $cp com.myjavaworld.jftp.StateProbe prepare-desktop
if ($LASTEXITCODE -ne 0) { throw 'Profile preparation failed; do not launch' }
& "$env:JAVA_HOME\bin\java.exe" "-Duser.home=$profilePath" -cp $cp com.myjavaworld.jftp.JFTPApplication
```

The actual entry point was launched with this isolated state. A visible frame
showed `report.txt`, `image.csv` and `folder`, and the standalone process reported
`Responding=True`. Startup logs had no application exception. No external FTP
service, participant data or personal preference/certificate store was used.

## Desktop evidence and limits

Visible Swing-control automation exercised second-session creation, connection
validation/cancellation, invalid-regex feedback, filter apply/clear with actual
listing assertions, and preference cancellation/save with actual disk readback.
Screenshots are under ignored `docs/screens/`: `startup.png`, `two-sessions.png`,
`connect.png`, `connection-validation.png`, `filter-validation.png`,
`filter-input.png`, `filtered-files.png`, `preferences-cancel.png`,
`preferences-save.png`, `preferences-saved.png`.

This automation used public Swing controls (`doClick`, `setText`, tree selection)
in the **real application**, without mocks or production test paths. It is not a
native mouse/keyboard Manual QA pass. A later favorites-screen run stopped because
the QA helper incorrectly treated a numeric port field as a password field. Its
failed assertion and explicit `System.exit(1)` closed the test process; this was
not an observed application crash. The helper was not promoted to a regression
test. Favorites persistence is covered by the passing behavior suite.

The native-input diagnostic returned exactly:

```text
GetCursorPos = True
SetCursorPos(currentX,currentY) = False
GetLastError = 5 (Access is denied.)
TokenIsAppContainer = 1
TokenUIAccess = 0
TokenElevation = 0
```

Windows requires window-station write access and the input desktop for
[SetCursorPos](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setcursorpos).
The command's token is an AppContainer token despite its normal user name. This
supports an executor-isolation explanation; no ACL-level access check was made to
distinguish the exact denied window-station/desktop right. No sandbox, ACL,
desktop assignment or system configuration was changed to force input access.

[Codex Windows sandbox documentation](https://learn.chatgpt.com/docs/windows/windows-sandbox)
also states that MXC stops remaining child processes when a foreground command
exits. This can explain detached-process lifetime, but the active backend was not
independently identified here. The observed QA-helper exits are directly
explained by its own error handler.

**Remaining required validation:** native/human interaction including focus and
keyboard navigation, completing favorites add/edit/delete/cancel, About, normal
Exit, and standalone restart with persisted values. Packaged distribution launch,
FTP/FTPS transfers and non-Windows support remain unverified and outside the
agreed initial scope. No commit or push was made during the initial startup exercise.

## Commit preparation verification, 2026-10-15

The user explicitly authorized committing this build/test baseline with the native
Manual QA gap recorded, as an exception to the repository's pre-commit QA rule.
This exception permits recording the work; the outstanding runtime QA remains
incomplete.

Using the same JDK, Maven executable, settings and local repository listed above,
both offline checks passed:

```powershell
mvn -B -ntp -o -s <session-settings> '-Dmaven.repo.local=<session-cache>' compile
mvn -B -ntp -o -s <session-settings> '-Dmaven.repo.local=<session-cache>' '-DargLine=-Djava.awt.headless=true' test
```

Results: compilation `BUILD SUCCESS`; all 26 tests executed with zero failures,
errors or skips. Logs: `target/verification/commit-compile.log` and
`target/verification/commit-tests.log`. These are ignored local artifacts.
An isolated application process again reported `Responding=True` with title
`JFTP`. A native-input attempt returned `SetCursorPos=False`; bringing the window
to the foreground also failed. The attempted OS screenshot captured the terminal,
so it was rejected as application evidence. No native QA pass is claimed.
