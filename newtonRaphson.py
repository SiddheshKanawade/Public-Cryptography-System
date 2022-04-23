
import helper

helperObj = helper.Helper


class newtonRaphsonClass:
    def newtonRaphson( x , c ):
        h = helperObj.funIter(x , c) / helperObj.derivFunc(x)
        while abs(h) >= 0.0001:
            h = helperObj.funIter(x , c)/helperObj.derivFunc(x)
            
            # x(i+1) = x(i) - f(x) / f'(x)
            x = x - h
        
        # print("The value of the root is : ",
        #                          "%.4f"% x)

        return x

