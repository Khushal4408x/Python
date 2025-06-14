class father:
    def __init__(self):
        print("Father class const")
    def show_fath(self):
        print("father class method") 
class son(father):
    def __init__(self):
        print("son class const")
    def show_son(self):
        print("Son class method")
class daughter(son):
    def __init__(self):
        print("daughter class const")
    def show_daughter(self):
        print("daughter class method")
s=son()
s.show_son()
s.show_fath()        