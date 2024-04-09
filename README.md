# Kryptuś

## How it works?
Kryptuś is a Python-based encryption and decryption tool that uses a specific key to encrypt and decrypt text files.
The tool also supports compression of the encrypted text to save storage space.

## How to use it?
Upon its first usage, the program will create a configuration file.
This configuration file contains the following fields:

```ini
[DEFAULT]
key = An 11 character long key used for both encryption and decryption processes.
file-location = The location of the file containing the text you wish to encrypt.
encrypted-file-location = The location where you want to store your encrypted text.
decrypted-file-location = The location where you want to store your decrypted text.
use-compression = Set this to TRUE if you want to compress the encrypted text, and FALSE if not.
```
The configuration file must use the same values for the key and compression when encrypting and decrypting the same text.

Alternatively, you can bypass the configuration file and set everything directly in the program, from the key to the file locations. The only exception is the **use-compression** option, which must be set in the configuration file.