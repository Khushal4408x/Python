f=open("/home/kali/Documents/coding/Pythonbg/collegeworkshop/filehandling/myfile.txt","r")
print(f.read())
g=open("myfilewrite.txt","a")
print(g.write("Lets commoditize the petaflops"))
g.write(" !!!!!!!!Khushal@")
f.close()

