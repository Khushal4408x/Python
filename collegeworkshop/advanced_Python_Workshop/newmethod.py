class person:
    def __new__(self):
        print("THis is new method")
        self.__init__(self)
    def __init__(self):
        print("init method")        
        