import helper

helperObj = helper.Helper

class Decryption:
    def decryption(cipher):
        func_list=[]
        s = ''
        asciiValue = []
        for i in range(len(cipher)):
            asciiValue.append(int(helperObj.funAscii(cipher[i])))
            s += chr(int(helperObj.funAscii(cipher[i])))

        return [s, asciiValue]
        