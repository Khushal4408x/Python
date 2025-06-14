class MyClass:
    def my_method(self, arg1, arg2=None):
        if arg2 is not None:
            print(arg1 + arg2)
        else:
            print(arg1)
