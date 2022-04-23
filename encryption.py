import newtonRaphson

newtonRaphsonObj = newtonRaphson.newtonRaphsonClass

class Encryption:
    def encrption(list):
        x0 = 1
        cipher = []
        for i in range(len(list)):
            temp = newtonRaphsonObj.newtonRaphson(x0, list[i])
            cipher.append(temp)
        return cipher