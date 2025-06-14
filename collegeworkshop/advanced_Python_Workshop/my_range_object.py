class myrange:
    def __init__(self,n):
        self.i=0
        self.n=n
    def __iter__(self):
        return self    
    def __next__(self):
        if self.i<self.n:
            val = self.i
            self.i+=1
            return val
        else:
            raise StopIteration 

for i in myrange(4):
    print(i)           