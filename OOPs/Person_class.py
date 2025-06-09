class Person:
    name="Khushal"
    occupation="Student"
    networth='-1'
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
a.info()
a.name="Shub"
a.occupation="CEO"
#print (a.name,a.occupation)    
a.info()
b=Person()
b.name="Ritu"
b.occupation="Teacher"
b.info()