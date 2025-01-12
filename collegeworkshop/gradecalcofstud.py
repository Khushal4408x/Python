a=int(input("enter the marks of first subject"))
b=int(input("enter the marks of second subject"))
c=int(input("enter the marks of third subject"))
d=int(input("enter the marks of fourth subject"))
totalmark=a+b+c+d
percent=(totalmark/400)*100
print("Percentage:", percent)
if(percent<=100 and percent>=90):
    print("Result - A Grade")
elif(percent<90 and percent>=75):
    print("Result - B Grade")
elif(percent<75 and percent>=60):
    print("Result - C Grade")
elif(percent<60 and percent>=40):
    print("Result - D Grade")
else:
    print("Result - Fail")                

