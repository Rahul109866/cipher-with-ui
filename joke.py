print('\033c')
#clears the screen for output


class Cipher():
    
    keyset = 'abcdefghijklmnopqrstuvwxyz'
    
    def __init__(self, message, rotation):
        
        self.message = message
        self.rotation = rotation
        
    def encrypt(self):
        
        def chrToUni(string): 
            """Converts the string into list of unicode equivalent
            
            Keyword arguments:
            string -- input string
            list: list of unicode converted elements
            """
            
            strList = [*string]
            return [ord(x) for x in strList]
        
        
        
        
        
        
        
        
        
        