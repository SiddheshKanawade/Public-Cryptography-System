import EEA

EEAObj = EEA.Euclidean

class KeyGeneration:
    # Overall Key Generation Algorithm
    def Key_Generation(p,q,x):
        n = p * q ; y = x ;
        phi_n = (p-1)*(q-1)
        (g,x,d) = EEAObj.EEA(EEAObj, phi_n,x)
        return (int(y),int(d),int(n))