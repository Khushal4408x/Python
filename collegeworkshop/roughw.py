n=int(input("enter the number"))
i=n
while i>0:
    j=i
    while j>0:
        print(j,end=" ")
        j=j-1
    j=2
    while j<=n-i+1:
        print(j,end=" ")
        j=j+1    
    print()
    i=i-1     



    

