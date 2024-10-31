import random
import numpy as np

random.seed=42

a=[]
for i in range(100):
    a.append(random.randint(200,800))

max1 = max(a)
min1 = min(a)
a.remove(max1)
a.remove(min1)

print(sum(a))

print(np.mean(a))