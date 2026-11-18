# IntegrityVoice for Android — Complete Corresponding Source

This repository contains the **complete corresponding source code** for the
**IntegrityVoice** app distributed on Google Play
(package `com.getintegrityvoice.softphone`), published by
**Nctsupport, LLC** (Belmont, NC, USA) in compliance with the GNU General
Public License.

**Contact:** support@nctsupport.com · https://getintegrityvoice.com

## What this app is

IntegrityVoice is the Android softphone for the IntegrityVoice business phone
service. It is a branded build of **Linphone for Android**, developed by
**Belledonne Communications** (https://www.linphone.org), preconfigured for
the IntegrityVoice PBX (`pbx.getintegrityvoice.com`).

## Licensing

- The app source in this repository is licensed under the
  **GNU General Public License v3.0** — see `LICENSE.txt`.
- The Linphone SDK (`org.linphone:linphone-sdk-android`) the app is built
  against is dual-licensed by Belledonne Communications under
  **GPLv3 / AGPLv3** or a commercial license. The AGPLv3 text is included as
  `LICENSE-AGPL-3.0.txt`. The SDK's own source code is published by
  Belledonne Communications at https://gitlab.linphone.org/BC/public/linphone-sdk
- All original copyright and license notices from upstream are preserved
  intact throughout this tree. Upstream's own README is kept unchanged as
  `README-UPSTREAM.md`.

If you received the IntegrityVoice app from Google Play and would like this
source in another form, write to **support@nctsupport.com** and we will
provide it.

## Provenance — exactly what this tree is

- Base: `BelledonneCommunications/linphone-android`, commit
  `8847693` ("Updated gradle to 9.8.2"), app version `6.3.0-alpha`
  (versionCode 602010) at the time of branding.
- Branding: applied by `brand/apply_brand.py` (included in this repository)
  plus the brand assets committed in the tree. The script's bench paths are
  specific to our build machine; the edits it makes are the complete set of
  functional changes: our package name, app name, colors, icons/splash,
  default domain `pbx.getintegrityvoice.com`, and removal of upstream's
  `app/google-services.json` (we ship no Firebase configuration in this
  build).
- The working tree published here is byte-for-byte the tree that produced
  the distributed build, minus build outputs (`app/build/`, `build/`) and
  the empty `keystore.properties` template values (the file itself is
  included, with blank fields).

## The Linphone SDK, as we build it

The SDK is **not** vendored into this tree. It is consumed as a Maven
artifact from Belledonne's repository (`https://download.linphone.org/maven_repository`),
selected by `settings.gradle.kts` and pinned by version range in
`gradle/libs.versions.toml` (`org.linphone:linphone-sdk-android`, `5.6.+`).
The build that produced the current distributed APK resolved that range to
**`5.6.0-alpha.212+89c46b14e5`**. The corresponding SDK source is the
`linphone-sdk` project at https://gitlab.linphone.org/BC/public/linphone-sdk
Before any future release build, the version range will be replaced with the
exact resolved version so the build is fully reproducible.

## Building

Standard Linphone Android build: `./gradlew assembleRelease` with the
Android SDK/NDK versions named in `docker-files/` and `gradle.properties`
(`LinphoneSdkBuildDir` may stay empty to use Belledonne's published SDK
artifact, as our build does). Release signing uses a `keystore.properties`
file that is intentionally blank here.
