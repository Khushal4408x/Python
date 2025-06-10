def gen_report(name,marks,subject="Python"):
    average=sum(marks)/len(marks)
    if(average>=90):
        grade="A"
        print(grade)
    elif(average>=75):
        grade="B"
        print(grade)
    else:
        grade="C"
        print(grade)
gen_report("Khushal",[89,80,99])        
