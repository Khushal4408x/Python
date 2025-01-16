f=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/num.txt","w")
f.write('1 2 3 4 5')
f.close()
z=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/num.txt","rt")
even=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/even.txt","a")
odd=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/odd.txt","a")
fileContent=z.read()
numbers=fileContent.split()
i=0
finalst=[]
while(i<len(numbers)):
    j=int(numbers[i])
    finalst.append(j)
    i=i+1
print("final list of fileContent in int values ",finalst)
p=0
while(p<(len(finalst))):
    x=str(finalst[p])
    if(((finalst[p])%2)==0):
        
        even.write(x)
    else:
        odd.write(x)
    p=p+1
even.close()          
odd.close()






