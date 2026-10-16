# Comparison with original and previous step

The previous published step is `original-initial-context`, also the original baseline, so both comparisons use that immutable snapshot. Its complete archived-file SHA-256 list was verified unchanged before and after extraction.

## Source changes for this UI request

Added `SygnityStyle` (central palette, presentation defaults, logo painter) and `SygnityAppearanceTest` (three contracts). Changed only the presentation call in the JFTP constructor, toolbar border/insets and decorative trailing label, opaque padded table-header presentation, and status-bar borders. Added a transparent logo resource derived from `assets/logo.svg`; no build wiring or dependency changes were required. Existing action declarations, icon assignments, listeners, enabled-state logic, FTP behavior and serialized preference/favorite/certificate classes were not changed by this task.

The surrounding dirty tree contains pre-existing startup/build, documentation, skill and newline differences. The current source manifest captures their actual bytes; differences from the historical original must not all be attributed to this UI request. `docs/PRD.md`, the desktop ADR and the task report describe the separately agreed presentation scope.

## Extraction differences

The original mapper was the Python fallback; this step uses the verified native 0.3.0 mapper. Declaration counts, formatting and ranking differences are therefore not evidence of application changes. This complete index captures 1,642 definitions in 191 Java files. The overview omits 626 definitions by budget and must not be treated as exhaustive.

The original text pack included a wider tracked-text/resource/help corpus. The new packs deliberately select all Java sources/tests, the Maven descriptor and palette tokens; this scope difference explains absent help/properties files and changed byte/token counts. Both new profiles use the same selected source bytes; the full pack keeps implementation bodies while compressed extraction loses structure/body details. No token count is claimed to measure model accuracy or savings in this conversation.

The new raw graph adds the style/helper test declarations and their extracted relations. Three new explicit call sites were verified: `JFTP -> SygnityStyle.install`, `JFTPToolBar.prepareToolBar -> SygnityStyle.logo`, and `StatusBar.initComponents -> SygnityStyle.statusCellBorder`. Five inferred generic Icon target resolutions are unsupported; applet launch icon methods actually refer to `launch.gif`, and generic IndentIcon dispatch does not establish the new anonymous icon as a target. Four status-cell calls collapse to one graph edge. Old graph review labels were not copied. Graph counts and absent edges do not establish a complete call graph or dead code.

## Verification boundary

Compilation and all 29 tests passed; the corrected pre-production Red run had exactly the two expected missing-branding failures. Native Swing desktop QA and screenshots used real Robot/XTest input under WSLg, with synthetic state and no mocks. Windows native-LAF appearance is unverified. The unavailable external CSV viewer is a recorded environment limitation, not repaired in this styling step. See the linked runtime report for exact commands and evidence.
