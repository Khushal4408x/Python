from functools import reduce
num_list=[20,12,52,22,72,19,7]
small=reduce(lambda x,y:x if x<y else y, num_list)
print (small)