class person:
    def __init__(self,fn,ln):
        self.fname=fn 
        self.lname=ln
        print("first name is {} and last name is {}".format(self.fname,self.lname))
class stud(person):
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        print("Inside student class init")
s=stud("Mohit","Kumar")



