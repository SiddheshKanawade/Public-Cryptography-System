import helper

helperObj = helper.Helper

class Decryption:
    def decryption(cipher):
        func_list=[]
        s = ''
        for i in range(len(cipher)):
            s += chr(int(helperObj.funAscii(cipher[i])))

        return s
        