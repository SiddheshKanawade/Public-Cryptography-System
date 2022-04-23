
class Euclidean:
    # Extended Euclidean Algorithm
    @staticmethod
    def EEA(self, a,b):
        y=0
        d=1
        if(a==0): 
            return b,y,d
        
        (g,yy,dd) = self.EEA(self, b%a,a)
        d = yy
        y = (dd-(b/a)*yy)
        return (g,y,d)
