class father:
    money =1000
    def show(self):
        print("Parent class instance method")
    @classmethod
    def moneyshow(cls):
        print("Parent class Class method: total money = ",cls.money)
    @staticmethod
    def stat_method():
        a=5
        print("Parent class static method: the value of a is ")            