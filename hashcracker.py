#!/usr/bin/env python3
import hashlib, sys, time
from itertools import product

# Ensures that python 3 is being used, otherwise the program will crash later on
if int(sys.version[0]) != 3:
    print("Sorry, Hashcracker requires Python 3. The latest version can be downloaded from http://www.python.org/download/releases/3.3.4/")
    sys.exit()
    

def get_algorithm( type ):
    # Dynamically creates the right function and returns it
    # using python closure, it is only used to build types_dict
    def algorithm( string ):
        h = type()
        h.update(string.encode('utf-8'))
        return h.hexdigest()
    return algorithm


TYPES_DICT = { 32 : get_algorithm( hashlib.md5 ),
               40 : get_algorithm( hashlib.sha1 ),
               56 : get_algorithm( hashlib.sha224 ),
               64 : get_algorithm( hashlib.sha256 ),
               96 : get_algorithm( hashlib.sha384 ),
               128 : get_algorithm( hashlib.sha512 ) }



class Control( object ):
    """ Main class """
    
    def __init__( self ):
        self.decrypt_method = None
        self.decrypted_hash = None
        self.user_file = None
    
    
    def main( self ):
        # Calls the get_hash method
        self.user_hash = self.get_hash()
        
        while self.decrypted_hash == None: # While no match has been found...
            self.crack_method = self.get_crack_method()
            
            if self.crack_method == 'd':
                self.wordlist = self.gen_wordlist() # get the wordlist...
                self.decrypted_hash = self.dict_attack()
            elif self.crack_method == 'b':
                self.decrypted_hash = self.brute_force()
                
            
            if self.decrypted_hash != None: # if hash_check returns a match carry out the 2 lines below and end the program
                self.elapsed = (time.time() - self.start) # This is the time taken to find a match.
                print('Hash cracked in '+str(self.elapsed)+' seconds. The correct word is: '+self.decrypted_hash)
                sys.exit()
            else:
                self.retry('no matches found')

            
    def get_hash(self):
        # Prompts for a hash
        while True:
            hash_input = input('Please enter the hash: ')
            
            # Checks if hash_input is a valid hash, returns the hash type,
            # and breaks out of the loop.
            # If hash is not valid, calls the retry method.
            
            if hash_input.isalnum(): # Ensures that the hash only contains alpha-numeric characters
                length = len(hash_input)
                
                if TYPES_DICT.get( length, None ):
                    self.hashtype = TYPES_DICT[length]
                    return hash_input

                else:
                    self.retry('invalid hash')
            
            else:
                self.retry('invalid hash')
                    
                    
    def gen_wordlist(self):
        # Prompts for a wordlist. If wordlist is not in the same directory as the program,
        # please enter the full path to the wordlist file.
        
        while self.user_file == None:
            self.filename = input('Please enter the name of the wordlist: ')
            
            # If file exists, the self.user_file variable is set to the wordlist and the loop ends.
            try:
                self.user_file = open(self.filename, 'r', encoding='utf-8')
            
            # If the file does not exist, calls the retry method.
            except FileNotFoundError:
                self.retry('no file named '+self.filename)
        
        # Reads file and returns a list.
        words = self.user_file.read()
        self.user_file.close()
        return words.split()
         
    
    def get_crack_method(self):
        while True:
            crack_method = input("Please enter 'b' for brute-force or 'd' for dictionary attack: ")
            if crack_method.lower() == 'b':
                return crack_method
            elif crack_method.lower() == 'd':
                return crack_method
            else:
                self.retry('invalid option')
            
    
    def dict_attack(self):
        # This method loops through the wordlist, converting each word to the hash type
        # and comparing the value to the hash entered by the user.
        # If/When the loop finds a match, the word is returned and the loop ends.
        # Also initializes the timer.
        self.start = time.time()
        print('Checking...\n\n')
        for word in self.wordlist:
            test = self.hashtype(word)
            if test == self.user_hash:
                return word
                
                
    def brute_force(self):
        # the brute force method. user enters required character set, min length and max length. 
        # the words are generated using itertools.product()
        charset = input('Please enter required character set: ')
        minlen = int(input('Please enter minimum length: '))
        maxlen = int(input('Please enter maximum length: '))
        
        print('Checking...(this could take a while)\n\n')
        self.start = time.time()
        for i in range(minlen, maxlen+1):
            for p in product(charset, repeat=i):
                word = ''.join(p)
                if self.hashtype(word) == self.user_hash:
                    return word
                
                
    def retry(self, failure_type):
        # This method asks if another try is required. The method is used for invalid hash,
        # invalid wordlist and if the selected wordlist does not find a match.
        # The failure_type argument is a string.
        print('Sorry, '+failure_type+'. Would you like to try again? (y/n)')
        while True:
            # If 'y' is selected, the loop ends and returns back to whichever method it was called from.
            # If 'n' is selected, the program ends.
            # If anything else is selected, the code returns to the beginning of the loop.
            choice = input()
            if choice.lower() == 'y':
                return
            elif choice.lower() == 'n':
                print('Thanks for using, goodbye.')
                sys.exit()
            else:
                print('Invalid option. Please press y or n.')

                    
                    
if __name__ == "__main__":
    run_it = Control()
    run_it.main()
