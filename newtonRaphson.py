
import helper
import helper2

helperObj = helper.Helper
helper2Obj = helper2.AdvHelper

class newtonRaphsonClass:
    def newtonRaphson( x , c ):
        h = helperObj.funIter(x , c) / helperObj.derivFunc(x)
        while abs(h) >= 0.0001:
            h = helperObj.funIter(x , c)/helperObj.derivFunc(x)
            
            # x(i+1) = x(i) - f(x) / f'(x)
            x = x - h
        return x
    
    def newtonRaphson_KeyGeneration(x,c):
        h = helper2Obj.func_2(x,c) / helper2Obj.derivFunc_2(x)
        while abs(h) >= 0.0001:
            h = helper2Obj.func_2(x,c)/helper2Obj.derivFunc_2(x)
            x = x - h             # x(i+1) = x(i) - f(x(i)) / f'(x(i))
        # print("The value of the root is : ", "%.4f"% x)
        return x

