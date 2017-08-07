import numpy as np

# Warning!!!
# a = b = c = d, all are the same
a = np.arange(4)
b = a
c = a
d = b

a[0] = 11

print(a)
print(b)
print(c)
print(d)
print('b is a: ', b is a)
print('c is b: ', c is b)
print('d is a: ', d is a)

# deep copy
b = a.copy()
print('b is a', b is a)