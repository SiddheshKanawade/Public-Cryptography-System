
class Helper:
    def funIter( x , c):
        return 3.5*(x**3)- 2.7 * x - 17 - c
 
    # Derivative of the above function
    # which is 3*x^x - 2*x
    def derivFunc( x ):
        return 10.5 * (x**2) - 2.7 

    def funAscii(x):
        ascii = 3.5*(x**3)- 2.7 * x - 17
        ascii = round(ascii, 0)
        return ascii