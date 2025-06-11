class person():
    def __init__(self,n,a):
        self.name=n
        self.age=a
Person= person("Alice",19)
name = getattr(person,"age") 
print(f"Name:{name}")      