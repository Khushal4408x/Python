l1=[22,45,2,87,56,"Khushal"]
l2=[3,44,2,87,0,-34]
print (type(l1),type(l2))
l1.remove("Khushal")
print (l1)
l2.append(9999)
print(l2)
l1,l2.sort()
print (l1,l2)
print ("slicing",l1[0:3])
l1[0]="Khushal"#list is mutable but tupple is immutable
print (l1)