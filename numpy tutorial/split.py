import numpy as np

a =  np.arange(12).reshape((3,4))
print(a)

b = np.split(a, 3, axis = 0) # split into 3 array 
print(b)

c = np.array_split(a, 3, axis=1) # inequivalent
print(c)

# vertical and horizontal
d = np.vsplit(a, 3)
print(d)
e = np.hsplit(a, 2)
print(e)

