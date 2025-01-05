a={3,4,5,23,33}
a2={3,55,34,44}
print (a2.pop())#pop returns a random value choosen from set
a.clear
print(a,a2)
a.add(25)
print(a.union(a2))
print(a.intersection(a2))