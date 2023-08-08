print('\033c')
# clears the screen for output


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

            str = string.strip().lower()
            str1 = [*str]
            return list(map(ord, str1))
            # unpack the strings into a list of charecters

        uniEncryptList = chrToUni(self.message)
        print(uniEncryptList)

        def rotate(num, degree=self.rotation):
            if num != 32:
                return num + degree  # to account for whitespaces
            else:
                return num

        def cyclicUnicode(num):
            """makes the unicode cycle between 97 and 122

            Keyword arguments:
            num -- unicode number representation of a lowercase charecter
            Return: int -> cycled unicode charecter if out of bounds
            """

            if num > 122:
                return (num % 122) + 96

            elif num == 32:  # preserve whitespace position
                return num

            else:
                return num % 122

        # shift and make them within alphabet range
        cycledUnicode = list(
            map(cyclicUnicode, list(map(rotate, uniEncryptList))))
        print(cycledUnicode)

        # convert unicode back to charecter
        cipherText = list(map(chr, cycledUnicode))

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

            str1 = string
            str1 = [*str1]
            return list(map(ord, str1))

        uniDecryptList = chrToUni(self.spaghetti)

        def unRotate(num, degree=self.cipher_key):
            if num != 32:
                return num - degree
            else:
                return num    # preserve whitespace position

        def decyclicUnicode(num):
            """makes the unicode cycle between 97 and 122

            Keyword arguments:
            num -- unicode number representation of a lowercase charecter
            Return: int -> cycled unicode charecter if out of bounds
            """

            if num > 96 or num == 32:
                return num

            else:  # if the charecter was wrapped around in the original code
                # measure of how far away from 97('a') is num and then add it to 122('z') to wrap around
                return 122 + (num - 96)

        decycledUnicodeList = list(
            map(decyclicUnicode, list(map(unRotate, uniDecryptList))))

        decryptedList = list(map(chr, decycledUnicodeList))

        print("The original message is: ")
        # make it presentable with capitalization and with a fullstop
        return f'\n{"".join(decryptedList).capitalize()}. '


if __name__ == '__main__':

    c = Cipher()

    choice = int(input("Do you want to encrypt or decrypt?: "))

    if choice != 0:
        print(c.encrypt())
    else:
        print(c.decrypt())
