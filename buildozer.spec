[app]

# (str) Title of your application
title = JARVIS Hindi Assistant

# (str) Package name
package.name = jarvis

# (str) Package domain (needed for android/ios packaging)
package.domain = com.jarvis.assistant

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,yaml

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyjnius,pyyaml,speechrecognition,pyttsx3

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = RECORD_AUDIO,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) The archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The X509 certificate subject to use for creating the keystore
# android.keystore_name = jarvis.keystore

# (str) The name of the keystore to create.
# android.keystore_name = jarvis.keystore

# (str) The password for the keystore
# android.keystore_passwd = jarvis

# (str) The alias for the keystore
# android.keystore_alias = jarvis

# (str) The password for the keystore alias
# android.keystore_alias_passwd = jarvis

# (str) The format of the keystore
# android.keystore_format = PKCS12

# (str) The format of the keystore
# android.keystore_format = PKCS12

# (int) if set, create an APK that targets API level set. For example, if set to 27,
# the APK will target API 27, and will not run on devices with API < 27.
# android.target_api = 27

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values is available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

# (str) The command invoked on completion of the APK. The pattern is a format string
# as expected by the str.format() method. The following values are available for use:
# - {appclass} is the app class name
# - {package} is the package name
# - {build} is the build number
# - {arch} is the architecture
# android.apk_cmd = {appclass} -m {package}.{appclass} {args}

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin
