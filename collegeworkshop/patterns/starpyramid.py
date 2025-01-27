n=int(input("enter num: "))
i=0
while(i<n):
    j=n-1-i
    while (j>0):
        print(" ",end="")
        j=j-1
    k=1
    while(k<=i*2+1):
        print("*",end="")
        k=k+1
    print()
    i=i+1; 
   
    
    
    