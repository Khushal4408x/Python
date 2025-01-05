s="I am a programmer"
#writing to a file
with open("test.txt","w") as f:
    f.write(s)

with open ("test.txt","r") as f:
    d=f.read(s)    
    print(d)

with open ("test.txt", "a")as f:
    f.write(s)

