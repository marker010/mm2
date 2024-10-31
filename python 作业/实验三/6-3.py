import copy
x = [1,2,3]
y=copy.deepcopy(x)
y[2]='a'
print("x=",x)