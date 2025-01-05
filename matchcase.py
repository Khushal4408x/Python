a= int (input('Enter num'))
match a:
    case 1 :
        print("Case is 1")
    case 2:
        print("case is 2")
    case 32:
        print('case is 32')
    case _:
        print("no match found")