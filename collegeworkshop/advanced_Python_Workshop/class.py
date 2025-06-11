class person:
    def __init__(self,n,occ):
        self.name=n
        self.occ=occ
        print("Const created")
    def info(self):
        print(self.name,self.occ) 
       
p1=person("Khushal","Student")#parameterised const , since args are there
p1.info()
p2=person("Harsh","HR")
p2.info()    
p3=person("Ritu","Teacher")
p3.info()

