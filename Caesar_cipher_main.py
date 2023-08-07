print('\033c')
#clears the screen for output


class Cipher():
    
    # keyset = 'abcdefghijklmnopqrstuvwxyz' 
    
    def __init__(self, message, rotation):
        
        print("Welcome to the CCA's cipher machine.")
        
        self.message = message
        self.rotation = rotation
        if rotation > 25:
            print("Please enter a number less than 26 to avoid redundancy.")
            
        
    def encrypt(self):
        
        print("Begin Encryption.....")
        
        def chrToUni(string): 
            """Converts the string into list of unicode equivalent
            
            Keyword arguments:
            string -- input string
            list: list of unicode converted elements
            """
            
            strList = [*string] # unpack the strings into a list of charecters
            return [ord(x) for x in strList]
        
        uniList = chrToUni(self.message)
        
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
            
        cycledUnicode = list(map(cyclicUnicode, list(map(rotate, uniList))))
        
        cipherText = list(map(uniToChar,cycledUnicode ))
        
        print("Encryption Completed.")
        print("The encrypted text is:")
        return "".join(cipherText)
    
    
    
    
    
c = Cipher('ragul', 29)
print(c.encrypt())
    
    

        
        
        
        
        
        
        
        
        
        
        