# Activity performed as part of Public Key Cryptography Basics Room

- **Pre-requiste** :
1. Start the Room specific machine for the activities.

- **Task 5** :
1. Navigate to provided location and check out the file which is present in location.
2. To display the fingerprint use command: "ssh-keygen -l -f <File_location>".

- **Task 7** :
1. This task crucially deals with decryptionusing the gpg.
2. Use the command provided to temporarily import the necessary key to decrypt. command: "gpg --no-default-keyring --keyring ./temp-keyring.gpg --import <my_private.key>"
Explination: 
gpg
Invokes the GNU Privacy Guard (GPG), a tool for secure encryption and decryption using public-key cryptography.
--no-default-keyring
Tells GPG not to use the default keyring (~/.gnupg/pubring.kbx and secring.gpg or equivalent). This ensures you don’t affect or interact with your main stored keys.
--keyring ./temp-keyring.gpg
Specifies a custom keyring file (here, temp-keyring.gpg) where GPG should import or look for keys.
This becomes the new active keyring just for this command and others with the same flags.
--import <my_private.key>
Tells GPG to import the contents of my_private.key (usually an ASCII-armored or binary OpenPGP private key) into the specified keyring.
3. Use the command to decrypt the message and obtain the message. command: "gpg --no-default-keyring --keyring ./temp-keyring.gpg --decrypt L<encrypted_file.gpg>"
Explination:
gpg
Calls the GPG tool to perform operations—in this case, decryption.
--no-default-keyring
Again disables use of the system’s default keyring, ensuring you are working only with the custom one.
--keyring ./temp-keyring.gpg
Uses the same temporary keyring where the private key was imported.
This keyring contains the private key required to decrypt the message.
--decrypt <encrypted_file.gpg>
Tells GPG to decrypt the file encrypted_file.gpg.
If it was encrypted with the matching public key, GPG uses the imported private key to reverse the encryption and recover the original content.


