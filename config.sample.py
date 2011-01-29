
#Copy this file to config.py, then amend the settings below according to
#your system configuration.

aapt_path = "/path/to/android-sdk-linux_86/platforms/android-4/tools/aapt"
sdk_path = "/path/to/android-sdk-linux_86"
ndk_path = "/path/to/android-ndk-r5"

#You probably don't need to change this...
javacc_path = "/usr/share/java"

repo_url = "http://f-droid.org/repo"
repo_name = "FDroid"
repo_icon = "fdroid-icon.png"
repo_description = """
The official FDroid repository. Applications in this repository are official
binaries built by the original application developers.
"""

#The key (from the keystore defined below) to be used for signing the
#repository itself. Can be none for an unsigned repository.
repo_keyalias = None

#If you're building a signed repository, you need the public key here. You
#can get the public key in the correct format by using 'getsig -f x.jar" where
#x.jar is any jar you have signed with it.
repo_pubkey = 'not set'

#The keystore to use for release keys when building. This needs to be
#somewhere safe and secure, and backed up!
keystore = "/home/me/somewhere/my.keystore"

#The password for the keystore.
keystorepass = "foo"

#The password for keys - the same is used for each auto-generated key.
keypass = "foo2"

#The distinguished name used for all keys.
keydname = "CN=Birdman, OU=Cell, O=Alcatraz, L=Alcatraz, S=California, C=US"

#Use this to override the auto-generated key aliases with specific ones
#for particular applications. Normally, just leave it empty.
keyaliases = {}
keyaliases['com.example.app'] = 'example'


