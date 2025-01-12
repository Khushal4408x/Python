a=int (input("Enter a num"))
i=1
sum=0
while (i<=a/2):
    if(a%i==0):
        sum+=i
    i=i+1
if(sum==a):
    print ("The number is perfect")        