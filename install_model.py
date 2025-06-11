import argostranslate.package
import argostranslate.translate

print("available models check kiye ja rahe hain...")
available_packages = argostranslate.package.get_available_packages()

print("english to urdu model dhoonda ja raha hai...")
package_to_install = next(
    pkg for pkg in available_packages
    if pkg.from_code == "en" and pkg.to_code == "ur"
)

print("model download ho raha hai...")
download_path = package_to_install.download()
print("model download ho gaya:", download_path)

print("model install kiya ja raha hai...")
argostranslate.package.install_from_path(download_path)

print("✅ model successfully install ho gaya")
