n=int(input("enter the num"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j%2==1):
            print(n-j+1, end=" ")
        else:
            print("*", end=" ")    
    print()    
