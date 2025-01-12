n=int (input("Enter num of terms to be printed: "))
i=0
j=i+1
print(i, end=" ")
print(j, end=" ")
a=0
while(a<n-2):
    k=i+j
    print(k, end=" ")
    i=j
    j=k
    a+=1