try:
    a=int(input("Enter a num"))
    print(a+3)
except Exception as e:# Exception as e assigns the error to e and we can print the error
    print ("some error occured",e)  # its not necessary to assign and print the exception to a variable  
finally:
    print("This part will execute even when the exception occured")
        