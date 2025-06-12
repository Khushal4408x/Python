import math 
class frac:
    def __init__(self,n,d):
        self.numerator=n
        self.denominator=d
        self.simplify()
    def simplify(self):
        comm_div=math.gcd(self.numerator,self.denominator)
        self.numerator//=comm_div
        self.denominator//=comm_div
    def __add__(self,other):
        new_num=self.numerator*other.denominator+other.numerator*self.denominator
        new_den=self.denominator*other.denominator
        return frac(new_num,new_den)
    def __eq__(self,other):
        return self.numerator==other.numerator and self.denominator==other.denominator
    def __lt__(self,other):
        return self.numerator*other.denominator<other.numerator*self.denominator
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
f1=frac(1,2)          
f2=frac(2,3)
f3=f1+f2
print(f3)
print(f1==f2)
print(f1<f2)    