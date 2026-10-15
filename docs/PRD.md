# Minimal Windows startup and behavior baseline

Agreed scope: the user's request of 2026-10-15. Baseline revision:
`cdc95025ac74098f129bfd9cdcd613fa6348c8d0`.

## Outcome and acceptance criteria

Run the existing desktop application on this Windows machine with the installed
Microsoft JDK 21. Make only evidenced build/startup repairs; preserve application
logic, resource encodings, preference/favorite formats and UI.

Before changing production behavior, characterize four existing capabilities:

1. Connection configuration: defaults, normalization, login commands and FTP/FTPS
   settings survive serialization without losing user-entered data.
2. Local filtering: inclusion/exclusion, case sensitivity, modification-date
   boundaries, hidden files and directory navigation use real synthetic files.
3. Favorites: first use, add, replace, remove, clear, legacy-format import and
   damaged-file errors preserve observable persistence behavior.
4. Preferences: first use, repeated save/reload, connection/transfer/UI settings
   and certificate paths survive persistence. Characterize damaged-file fallback
   separately from desired future recovery behavior.

Tests use public behavior, no private-field assertions or endpoint/database
mocks. All persisted data belongs to a unique synthetic profile. Establish a
passing characterization baseline and demonstrate that controlled behavioral
mutations are detected, reverting each mutation afterward. A build failure is
not a behavioral TDD Red. Any discovered runtime defect requiring a fix needs a
regression test that fails for that defect before the fix.

Verify compilation, test discovery/execution and visible Swing startup
separately. Exercise sessions, local filtering, connection cancellation,
favorites, preferences save/cancel, About, exit and restart. Save screenshots
under `docs/screens/` and inspect logs. Use only synthetic local files; disable
update checking in the QA profile before startup. Do not contact FTP services.

## Boundaries

No protocol changes, dependency modernization, UI redesign, external services,
personal state, deployment, commits or push. FTP/FTPS transfers, packaged launcher
repair and other operating systems are outside this initial startup exercise.
The existing architecture sketch is adequate for entry-point navigation; extend
it with persistence, resource/dependency boundaries and verified startup facts.

## Subsequent commit authorization

On 2026-10-15 the user requested granular local commits for the accumulated
repository changes and explicitly accepted committing the build/test baseline
with the native Manual QA gap documented in [minimal-startup.md](minimal-startup.md).
This supersedes the initial no-commit boundary for recording the work. Push was
not requested, and the outstanding runtime QA is still incomplete.
