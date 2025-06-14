class stud:
    _name=None
    _roll=None
    _branch=None
    def __init__(self,n,r,b):
        self._name=n 
        self._roll=r 
        self._branch=b 
    def _info(self):
        print("roll: ",self._roll)
        print("Branch: ",self._branch)
class Learnowx(stud):
    def __init__(self,name,roll,branch):
        stud.__init__(self,name,roll,branch)
    def displayDet(self):
        print("Name: ", self._name)
        self._info()           

obj=Learnowx("Aditya",3424,"ds")
obj.displayDet()