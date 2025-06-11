import argostranslate.translate

langs = argostranslate.translate.get_installed_languages()
for lang in langs:
    print(f"{lang.name} - {lang.code}")
