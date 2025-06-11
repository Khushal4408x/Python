class add:
    first=0
    sec=0
    ans=0
    def __init__(self,f,s):
        self.first=f
        self.sec=s
    def display(self):
        print("first num = ", self.first)
        print("sec num = ", self.sec)  
        print("Add= ",self.ans)
    def calc(self):
        self.ans=self.first+self.sec
        print(self.ans)
obj=add(199,1)
obj.display()
obj.calc()            