[app]

# (str) Title of your application
title = Calculadora de Moedas

# (str) Package name
package.name = calcugator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let Kivy find KV inside main)
source.include_exts = py,kv

# (str) Application versioning (method 1)
version = 0.1.0

# (list) Application requirements
# Kivy 2.2.x é estável no Android; KivyMD 1.1.1 é compatível
requirements = python3,kivy==2.2.1,kivymd==1.1.1,num2words

# (str) Supported orientation (one of: landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Use AndroidX
android.enable_androidx = True

# (int) android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (str) Permissions
android.permissions = INTERNET

# (bool) Accept Android SDK licenses automatically (recomendado para CI)
android.accept_sdk_license = True

# (str) Application entry point is main.py por padrão
# entrypoint = main.py

# (str) Icon of the application (opcional)
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application (opcional)
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
# (str) Command to run the application
disable_android_logcat = 0
log_level = 2
warn_on_root = 1 