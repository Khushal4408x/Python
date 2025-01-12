print("Basic calculator")
num1=int(input("Enter the first num "))
num2= int(input("Enter the second num "))
operation=int (input("Enter 1,2,3,4 for add, sub, mul,div respectively"))
if(operation==1):
    out=num1+num2
elif(operation==2):
    out=num1-num2    
elif(operation==3):
    out=num1*num2    
elif(operation==4):
    out=num1/num2  
else:
    print("Enter the correct operation number")
print("The output is ",out)    