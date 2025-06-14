def decor(func):
    def inner():
        print("hee decor strt")
        func()
        print("Hello by decor end")
    return inner

def printer():
    print("Hello")
alias=decor(printer) 
alias()