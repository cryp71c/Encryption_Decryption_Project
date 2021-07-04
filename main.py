import random
import numpy as np
class EDAlgorithm:
    def __init__(self, keyValues, string_to_encrypt):
        self.keyValues = keyValues
        self.string_to_encrypt = string_to_encrypt
        global encryp_char_List 
        encryp_char_List = []
        global char_unecryptlst
        char_unecryptlst = []
        global unecryptlst
        unecryptlst = []
        global full_string
        full_string = ""

    def encrypt(self):
        for i in self.string_to_encrypt:
            x = ord(i)
            encryp_char_List.append(x * np.sum(self.keyValues))
  
    def decrypt(self):
        for items in encryp_char_List:
            l = np.sum(self.keyValues)
            char_unecryptlst.append(int(items/l))
        for letter in char_unecryptlst:
            letter = chr(letter)
            unecryptlst.append(letter)
        full_string = "".join(unecryptlst)
        print(full_string)

def main():
    usr_input_str = input("Please enter a string to encrypt: ")
    config_setup = EDAlgorithm([random.randint(0,1000000) for _ in usr_input_str], usr_input_str)
    config_setup.encrypt()
    print(encryp_char_List)
    config_setup.decrypt()

main()