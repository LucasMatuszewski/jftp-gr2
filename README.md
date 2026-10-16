JFTP - The Universal FTP Client
===============================

Course updates
--------------

Use these pull requests and branches as course checkpoints:

| Update | Pull request | Branch | What changed |
| --- | --- | --- | --- |
| Documentation baseline and modernization plan | [PR #2](https://github.com/LucasMatuszewski/jftp-gr2/pull/2) | [codex/modernization-roadmap](https://github.com/LucasMatuszewski/jftp-gr2/tree/codex/modernization-roadmap) | Current-functionality PRD, retrospective architectural decisions, and a proposed staged modernization roadmap. |
| Sygnity visual refresh | [PR #1](https://github.com/LucasMatuszewski/jftp-gr2/pull/1) | [codex/sygnity-ui-refresh](https://github.com/LucasMatuszewski/jftp-gr2/tree/codex/sygnity-ui-refresh) | Sygnity branding, light surfaces, cyan accents, spacing and flatter borders, with existing workflows preserved as the acceptance requirement. |

For the documentation checkpoint, start with the [current-functionality PRD](docs/PRD.md), [architecture baseline](docs/ADR/000-main-architecture.md), [proposed modernization ADR](docs/ADR/008-modernization-roadmap.md), and [technology/UI research](docs/research/jftp-modernization-2026-10-16.md). The roadmap proposes Java/build/test upgrades, separation of application logic, and a qualified FTP-library replacement. Swing and existing saved-data formats remain the initial constraints; a UI-library replacement is not decided.

The documentation already landed on master: [product baseline](https://github.com/LucasMatuszewski/jftp-gr2/commit/b5e7657bac97ae567533d74ae487e5ae713379c8), [architecture baseline](https://github.com/LucasMatuszewski/jftp-gr2/commit/469ecd58fe268dc759c91905c25ddcabf8782c8d), [certificate-description correction](https://github.com/LucasMatuszewski/jftp-gr2/commit/284ab9fa6a54bf060e2f006baea724d3db5cf845), [modernization proposal](https://github.com/LucasMatuszewski/jftp-gr2/commit/8cec56fe7083ba71784528f8988c3f9ae234f8e8). This PR adds the course navigation above; it does not implement the proposed modernization.

For visual before/after screenshots and verification details, see the [visual-refresh report on its branch](https://github.com/LucasMatuszewski/jftp-gr2/blob/codex/sygnity-ui-refresh/docs/sygnity-ui-refresh.md). Each PR records its own scope and verification; a proposal or an open PR is not evidence that a change is merged.

Introduction
------------

JFTP is a graphical FTP (File Transfer Protocol) client software for 
transferring files from one computer to another over TCP/IP networks such as 
Internet.

JFTP can connect to any system that has a valid Internet address and an FTP 
server program, allowing you to transfer files between a wide variety of 
systems, including Windows, Mac OS X, Linux, UNIX and IBM i(AS/400) systems.

JFTP integrates the most widely used and widely accepted security mechanism, 
SSL (Secured Sockets Layer), to securely transfer your business critical and 
sensitive data.

JFTP is written entirely in Java(tm), meaning, it can run on a wide variety of 
platforms such as Windows, Mac OS X, Linux, Solaris, HP-UX, OS/2, UNIX or any 
other platform with a compatible JVM (Java Virtual Machine). 

Features
--------

###"The Universal FTP Client"

A "true" Universal FTP Client. JFTP can be installed and run on a wide variety 
of platforms such as:

* Windows 
* Mac OS X
* Linux
* Solaris
* HP-UX
* OS/2
* Other UNIX flavors
* Any other platform with a compatible Java Runtime Environment

###Security

JFTP integrates the most widely used and widely accepted security mechanism, 
SSL (Secured Sockets Layer), to securely transfer your business critical and 
sensitive data.

* Support for SSL 3.0 and TLS 1.0, 1.1 and 1.2
* Supports several cryptographic algorithms such as RSA, AES, RC4, DES, Triple 
  DES, Diffie-Hellman and DSA
* Support for both Explicit and Implicit SSL connections
* Option of using SSL if it is supported by the FTP server

###File Filters

File filters give you the ability to decide what all files may be listed, 
uploaded, downloaded or deleted with in JFTP. You can set up either inclusion 
or exclusion filters on local and/or remote files based on a variety of 
criteria such as:

* File name pattern using regular expressions
* Modification date of the files
* Attributes of the files (if a file is hidden or not)

Using file filters, uploading all the files in your site that were modified on 
a specific date is as easy as a click of a mouse. No more need to spend time 
in picking up individual files in several directories of your web site.

###Transfers

* Download files and/or directories. Directories will be processed recursively
* Download As option to download a single file or directory (and its contents) 
  as a different name
* Download and Unzip option to automatically unzip downloaded zip files
* Upload files and/or directories. Directories will be processed recursively
* Upload As option to upload a single file or directory (and its contents) as 
  a different name
* Zip and Upload option to zip one or more files and/or directories and upload 
  the resulting zip file
* Filtered transfers

###Simultaneous FTP Sessions

JFTP allows you to work with multiple FTP sites simultaneously. Each session 
will create a new Tab making it easy to switch between sessions.

###Connect Quickly and Easily

Well thought-out design allows you to connect to your FTP site quickly and 
easily. You can configure both simple and advanced connection parameters, all 
through one easy-to-use connection dialog.

###Advanced Connection Options

JFTP allows you to specify various advanced connection parameters such as:

* Whether to use plain FTP connection or secured FTP connection
* Ability to provide an "Account" name for login. Most FTP servers just use 
  user name and password for login, but, some require account name to be 
  specified for login.
* Option of encrypting just the command channel to securely transmit the 
  password over the network
* Specify initial local and remote working directories to set, upon a 
  successful login
* Support for both passive (default) and active data transfers
* Allows you to execute raw FTP commands (standard or custom) soon after log in

###Proxy/Firewall

JFTP gives you the ability to connect through proxy servers and firewalls.

* Supports SOCKS proxy (both version 4 and version 5)
* Automatic detection of SOCKS version
* Supports SOCKS authentication

###Certificate Manager

JFTP comes with a built-in certificate manager to manage all your trusted 
certificates. Certificates are used to establish secured FTP connections. With 
JFTP's certificate manger, you can -

* Import certificates in to your trusted certificates database
* View details of a certificate
* Delete certificates from your trusted certificates database

###Manage your Favorite FTP Sites

JFTP allows you to store the connection parameters for the FTP sites that you 
frequently work with. With JFTP, connecting to your favorite FTP site is just 
one click away! Favorite definitions use encryption when it is available; the
current save implementation also includes an unencrypted fallback.

###Remote File Tasks

* Browse through the file system of your FTP site
* Open/Edit remote files directly using associated applications, modify them 
  and save them back to the FTP server 
* Print remote files using associated applications 
* Filter files based on their name pattern and/or modification date
* Create new directories
* Create new files
* Move/Rename files and directories
* Delete files and directories
* View or change permissions of a file or a directory
* Change the permissions of a directory and all of its children
* Execute standard or custom FTP commands
* Sort directory listing by name, type, size or last modified date

###Local File Tasks

* Browse through the file system of your PC and computers on your network
* Open/Edit local files using associated applications 
* Print local files using associated applications 
* Filter files based on their name pattern, modification date and/or attributes
* Create new directories
* Create new files
* Move/Rename files and directories
* Delete files and directories
* View attributes of a file or directory
* Sort directory listing by name, type, size or last modified date

###Auto-Detection of Transfer Type

JFTP automatically detects the transfer type (ASCII or Binary) to use for a 
specific file based on its extension. This feature is very useful when you are 
transferring hundreds or thousands of files of different types, in which case 
manually setting the transfer type is impossible.

###Internationalization and Localization

Support for Internationalization and Localization. This means JFTP supports 
multiple languages and Locale specific data such as dates and numbers. You can 
install as many language packs as you wish and use the language of your 
choice. The current version of JFTP bundles the following language packs:

* English
* Chinese (Traditional) 
* German 

Product requirements baseline
-----------------------------

See the [current-functionality PRD](docs/PRD.md) for existing user flows, stories,
acceptance criteria and limitations. Its [evidence and consistency audit](docs/product/current-behavior-evidence.md)
distinguishes historical execution, source-confirmed behavior and unverified
outcomes. Historical platform and security claims above are not current support
certification. Future change PRDs can reference the stable story and criterion IDs.

Architecture documentation
--------------------------

See the [source-checked architecture diagrams](docs/design/jftp-architecture-2026-10-15.md)
for components, startup, connection, transfers and persistence, including scope
and verification limits.

See the [retrospective ADR baseline](docs/ADR/000-main-architecture.md) for eight
records covering the current technology, interfaces, data, consequences and
verification boundaries. Accepted baseline status records the existing system;
it does not recommend retaining every choice during modernization. Future
decisions update the affected record and its dated history, with earlier text
preserved in Git.

The [proposed modernization roadmap](docs/ADR/008-modernization-roadmap.md) and
[research report](docs/research/jftp-modernization-2026-10-16.md) compare current
technology alternatives and map intentional fixes to PRD criteria. These are
proposals for discussion, not implemented or accepted replacement decisions.

Development repository and branches
-----------------------------------

The development repository is [LucasMatuszewski/jftp-gr2](https://github.com/LucasMatuszewski/jftp-gr2).
Local `master` tracks `origin/master` and contains the application development
and exercise changes. `Upstream` preserves the original project at commit
`14e62ceba4e371c2a0b955604b10f065f46f4f7d`; keep development commits on `master`.
The `upstream` remote points to [sai-pullabhotla/jftp](https://github.com/sai-pullabhotla/jftp).
The preserved `Upstream` branch is also published to `origin`.

Codex dependency security hook
------------------------------

See the [Maven dependency security gate](.codex/hooks/README.md) for POM change
review, activation through `/hooks`, verification and coverage limits.
