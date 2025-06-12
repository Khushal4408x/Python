def outer():
    x=2
    def inner():
        print(x)
    inner()    
outer()    