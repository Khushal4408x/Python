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
class grandson(son):
    def __init__(self):
        print("Grandson class const")
    def show_grandson(self):
        print("grandson class method")
g=grandson()
g.show_grandson()
g.show_son()
g.show_fath()                                               