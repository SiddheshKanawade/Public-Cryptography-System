import newtonRaphson

newtonRaphsonObj = newtonRaphson.newtonRaphsonClass

class Encryption:
    def encrption(list, addition):
        x0 = 1
        cipher = []
        for i in range(len(list)):
            temp = newtonRaphsonObj.newtonRaphson(x0, list[i]) + addition
            cipher.append(temp)
        return cipher