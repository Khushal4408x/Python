class Person:
    def __init__(self,n,o):
        print("Hey i am a person")
        self.name=n
        self.occ=o
    name="Khushal"
    occ="Student"
    networth='-1'
    def info(self):
        print(f"{self.name} is a {self.occ}")
a= Person( "Harsh","HR")
b=Person( "Kunal","CEO")
a.info()
b.info()

