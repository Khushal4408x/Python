def decor(addition):
    def inner():
        result=addition()
        num3=float(input("Enter num 3: "))
        result=result+num3
        return result
    return inner
@decor
def addition ():
    num1=float(input("Enter num1:"))
    num2=float(input("ENter num2: "))
    res=num1+num2
    return res
print("addition: " , )