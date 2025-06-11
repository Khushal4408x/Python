class Mathop:
    @staticmethod
    def sub_num(a,b):
        return(a-b)
    @staticmethod
    def add(a,b):
        return(a+b)
ob=Mathop()
res_add=Mathop.add(3,4)
res_sub=Mathop.sub_num (4,4)       
print(res_add)