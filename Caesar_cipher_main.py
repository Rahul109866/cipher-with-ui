print('\033c')
#clears the screen for output


class Cipher():
    
     
    def __init__(self):
        
        print(f"Welcome to the CCA's cipher machine.\n".center(160))
        
        
    def encrypt(self):
        
        print("Begin Encryption.....\n")
        
        text = input("Please enter your message: ")    
        rotation = int(input("Enter the rotation for your Caesar's cipher: "))
        
        self.message = text
        self.rotation = rotation
        
        def chrToUni(string): 
            """Converts the string into list of unicode equivalent
            
            Keyword arguments:
            string -- input string
            list: list of unicode converted elements
            """
            
            # str1 = string.replace(" ", "")
            
            str1 = [*string]
            return list(map(ord, str1))
            # unpack the strings into a list of charecters
            
        
        uniEncryptList = chrToUni(self.message)
        
        def rotate(num, degree=self.rotation):
            return num + degree
        
        def cyclicUnicode(num):
            """makes the unicode cycle between 97 and 122
            
            Keyword arguments:
            num -- unicode number representation of a lowercase charecter
            Return: int -> cycled unicode charecter if out of bounds
            """
            
            if num > 122:
                return (num % 122) + 96
            else:
                return num % 122
            
        def uniToChar(num):
            return chr(num)
            
        cycledUnicode = list(map(cyclicUnicode, list(map(rotate, uniEncryptList))))
        
        cipherText = list(map(uniToChar,cycledUnicode ))
        
        print("\nEncryption Completed.")
        print("\nThe encrypted text is:")
        return "".join(cipherText)
    
    
    def decrypt(self):
        
        print("Decryption Commenced...")
        
        spaghetti = input("Please Enter the encrypted message: ")
        cipher_key = int(input("Enter the cipher key: "))
        
        self.spaghetti = spaghetti
        self.cipher_key = cipher_key
        
        def chrToUni(string): 
            """Converts the string into list of unicode equivalent
            
            Keyword arguments:
            string -- input string
            list: list of unicode converted elements
            """
            
            str1 = string.replace(" ", "")
            str1 = [*str1]
            return list(map(ord, str1))
        
        uniDecryptList = chrToUni(self.spaghetti)
        
        
        
        def unRotate(num,degree=self.cipher_key):
            return num - degree
        
        def decyclicUnicode(num):
            """makes the unicode cycle between 97 and 122
            
            Keyword arguments:
            num -- unicode number representation of a lowercase charecter
            Return: int -> cycled unicode charecter if out of bounds
            """
            
            if num > 96:
                return num
            else:
                return 122 + (num - 96) # measure of how far away from 97('a') is num and then add it to 122('z') to wrap around
        
        
        # return list(map(decyclicUnicode,list(map(unRotate, uniDecryptList))))
        
        decycledUnicodeList = list(map(decyclicUnicode,list(map(unRotate, uniDecryptList))))
        decryptedList = list(map(chr, decycledUnicodeList))
        return "".join(decryptedList)
        
        
if __name__ == '__main__': 

    c = Cipher()

    # print(c.encrypt())
    print(c.decrypt())
              