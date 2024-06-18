[app]
# (mandatory) Title of your application
title = Meu Projeto

# (mandatory) Package name
package.name = meuprojeto

# (mandatory) Package domain (needed for android/ios packaging)
package.domain = com.alx.master

# (mandatory) Source code where the main.py live
source.dir = .

# (optional) Application versioning (version code)
version = 0.1

# (optional) Application versioning (version name)
version.regex = (__version__ = ['"])([^'"]+)(['"])
version.filename = %(source.dir)s/main.py

# (optional) Application icon
icon.filename = %(source.dir)s/icon.png

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Separate folders by commas (e.g. deps, libs)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application presplash
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) Permissions
android.permissions = INTERNET

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Python for android
# Specify the python-for-android branch to use, defaults to master
# you can also set the full repository like git+https://github.com/kivy/python-for-android.git
# (if you know what you are doing)
android.python = 3.7.2

# (str) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 21

# (str) Android NDK version to use
# android.ndk = 19c

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = /opt/android-ndk

# (str) Android entry point
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'android'
# android.apptheme = android.Theme'

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (list) List of Java classes to add to the build.
# android.add_javaclasses = com.google.firebase.FirebaseApp,com.google.firebase.FirebaseOptions

# (list) List of Java jars to add to the libs so that pyjnius can access it (.jar files must contain .py files in the archive root or they will be ignored)
# android.add_jars = foo.jar,bar.jar:baz.jar

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# packagename tools)
# android.add_aars = foo.aar:bar.aar

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# packagename tools)
# android.gradle_dependencies = foo:bar

# (list) add a signature to the Android application
# default is empty and should be overwrite by adding something like this
# new_meta_data = key.store=key.keystore,key.alias=myalias

# (list) Change the signing entrypoint
# use it only if you understand what you are changing, per default, it's set to kivy entrypoint
# signing.entrypoint = my.signing.entrypoint

# (str) OUYA Console category. Should be one of GAME or APP
# if you leave this blank, OUYA support will be disabled
# android.ouya.category = GAME

# (bool) If True, then the android app will be started with black
# borders on non fullscreen mode, best for testing graphic issues
# android.new_skd = False

# (str) Keystore location (if using a full signing key)
# android.keystore = /path/to/keystore

# (str) Keystore password (if using a full signing key)
# android.keystore_password = my_password

# (str) Key alias (if using a full signing key)
# android.key_alias = my_alias

# (str) Key alias password (if using a full signing key)
# android.key_alias_password = my_alias_password
