def A():
    print("heloo")
    def inner():
        print("bye")
    return inner 
a=A()
a()
print(type(a))