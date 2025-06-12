def my_func():
    a=5
    b=3
    print("In Local")
    print(" inside Outer dir -:",dir())
    def inner_func():
        a=5
        print("Inner funct ")
        print("inside inner dir -:",dir())    
    inner_func()
    print("Updated inside outer dir -:",dir())    
my_func()
print(" outside dir -:",dir())