class comp:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("selling prince: {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price
        print("selling prince: {}".format(self.__maxprice))
c=comp()
c.sell()
c.setmaxprice(1000)
