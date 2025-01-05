a=[40,3,44,5,0]
b={44,555,2,55}
for i in range(5):
    if(i==2):
        continue#skips the second iteration
    print(i)
for item in a:
    print(item)
print ('printing set....')    
for i in b:
    print(i)    
    if(i==8):
        break #if i is assigned 8 then loop breaks
    if(i==55):
        continue#if i is assigned 55 then current iteration gets skipped and everything remains same
