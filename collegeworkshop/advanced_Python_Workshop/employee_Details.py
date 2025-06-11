class person:
    def __init__(self,n,designation):
        self.name=n
        self.designation=designation
        print("Const created")
    def info(self):
        print(self.name,self.designation) 
       
p1=person("Khushal","CEO")#parameterised const , since args are there
p1.info()
p2=person("Harsh","HR")
p2.info()    