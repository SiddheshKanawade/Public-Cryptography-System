import newtonRaphson
import helper
import encryption
import decryption
import keyGeneration
import newtonRaphson


newtonRaphsonObj = newtonRaphson.newtonRaphsonClass
helperObj = helper.Helper
encryptionObj = encryption.Encryption
decryptionObj = decryption.Decryption
keyGenerationObj = keyGeneration.KeyGeneration

# Driver program to test above

class main:

    def __init__(self, cipher, list, string):
        self.cipher = cipher
        self.list = list
        self.string = string

inputText = input()

# Key Generation
Sa, Pa, n = keyGenerationObj.Key_Generation(17, 13, 7)
x0 = 1
addition = newtonRaphsonObj.newtonRaphson_KeyGeneration(x0, Sa)

main.list=[]
for i in range(len(inputText)):
    main.list.append(ord(inputText[i]))

# encryption
main.cipher = encryptionObj.encrption(main.list, addition)
print("Encrption output: \n")
print(main.cipher)


# decryption
value = newtonRaphsonObj.newtonRaphson_KeyGeneration(x0, Sa)
decryptionOutput = decryptionObj.decryption(main.cipher, value)
main.string = decryptionOutput[0]
asciiList = decryptionOutput[1]
print("\nDecrypted message:\n" + main.string)
print("\n")

outputString = main.cipher

listfinal = []

for i in range(len(outputString)):
    listfinal.append([inputText[i], outputString[i], asciiList[i]])


