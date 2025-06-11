class comp:
    semicond_based=1
    def __init__(self,cpu,gpu,ram,mb,psu):
        self.cpu=cpu
        self.ram=ram
        self.gpu=gpu
        self.mb=mb
        self.psu=psu
    def specs(self):
        print("CPU---",self.cpu)
        print("GPU---",self.gpu)
        print("RAM---",self.ram)
        print("Motherboard---",self.mb)
        print("PsU---",self.psu)
portable=comp("R5 5700","RTX 4070 Mobile","16 gigs DDR5","AM4 Socket","170W")  
print(portable.specs())    
a=5
a.bit_length()  
          