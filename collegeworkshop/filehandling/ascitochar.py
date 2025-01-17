f=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/ascinum.txt","rt")
r=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/ascinum.txt","a")
content=f.read()
print(type(content))
contlst=content.split(" ")
print(contlst)
print(len(contlst))
finalist=[]
i=0
while(i<len(finalist)):
    x=int(contlst[i])
    finalist.append(x)
    i=i+1
print("int list ",finalist)    
