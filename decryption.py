import helper

helperObj = helper.Helper

class Decryption:
    def decryption(cipher, value):
        func_list=[]
        s = ''
        asciiValue = []
        for i in range(len(cipher)):
            asciiValue.append(int(helperObj.funAscii(cipher[i]-value)))
            s += chr(int(helperObj.funAscii(cipher[i]-value)))

        return [s, asciiValue]
        