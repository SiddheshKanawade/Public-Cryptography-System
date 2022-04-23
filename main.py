import newtonRaphson
import helper
import encryption
import decryption


newtonRaphsonObj = newtonRaphson.newtonRaphsonClass
helperObj = helper.Helper
encryptionObj = encryption.Encryption
decryptionObj = decryption.Decryption

# Driver program to test above

class main:

    def __init__(self, cipher, list, string):
        self.cipher = cipher
        self.list = list
        self.string = string

inputText = str(input("Type message\n"))

main.list=[]
for i in range(len(inputText)):
  main.list.append(ord(inputText[i]))

# print(main.list)
# print("\n")

print("\nProgram output: \n")
# encryption
main.cipher = encryptionObj.encrption(main.list)
print("Encrption output: \n")
print(main.cipher)





# decryption
main.string = decryptionObj.decryption(main.cipher)
print("\nDecrypted message:\n" + main.string)
print("\n")


