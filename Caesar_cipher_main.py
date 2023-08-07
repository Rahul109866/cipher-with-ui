print('\033c')
#clears the screen for output


class Cipher():
    
    # keyset = 'abcdefghijklmnopqrstuvwxyz' 
    
    def __init__(self):
        
        print("Welcome to the CCA's cipher machine.\n")
        
        
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
            
            strList = [*string] # unpack the strings into a list of charecters
            return [ord(x) for x in strList]
        
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
            
            strList = [*string] # unpack the strings into a list of charecters
            return [ord(x) for x in strList]
        
        uniDecryptList = chrToUni(self.spaghetti)
        
        def unRotate(num, rotation):
            return num - rotation
        
        def uni
        
        
        
        

    

c = Cipher()

print(c.encrypt())
    
    

    
    

        
        
        
        
        
        
        
        
        
        
        