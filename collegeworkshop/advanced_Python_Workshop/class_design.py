class student:
    def __init__(self):
        print("Default const called")
    def __init__(self,n,m,a):
        self.name=n
        self.marks=m
        self.age=a
        print ("parameterised const called ")
    def info(self):
        print("Name",self.name)
        print("Marks",self.marks)
        print("Age", self.age)
    def __del__(self):
        print("Destructor called ")
#s=student() this'll give error since prev const is overridden by new one
s1=student("Rohit",99,19)
s1.info()
