Hashcracker.py
==============

Python 3 program for dictionary attacks on password hashes

Written by Dan Boxall, aka "apex123". Many thanks to purplex for testing the program and helping to clean the code, and to 2laXt3rmn8r for testing the program and compiling the wordlist.

GENERAL USAGE NOTES
===================
- This version of Hashcracker can only be used with Python 3. I will be writing a version for python 2 later.
- Hashcracker supports dictionary attacks for hash types md5, sha1, sha224, sha256, sha384 and sha512.
- When first started, Hashcracker will prompt you to enter a hash. It will automatically detect what type of hash is entered (unless the hash is not one of the above mentioned hashtypes).
- Hashcracker will then prompt you to enter the name of the wordlist you would like to use. If the wordlist is not in the same directory as Hashcracker, please make sure to include the full path to the wordlist. A wordlist with over 660000 words has been compiled by 2laXt3rmn8r, and is included with this program.

SUGGESTIONS
===========
If you have any problems with Hashcracker, or would like to see anything added, please contact me at dboxall123@gmail.com.
I will be adding a GUI soon.
