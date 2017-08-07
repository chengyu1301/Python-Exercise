import numpy as np

a = np.arange(3, 15)
print(a)

# Index
print(a[3])

a = a.reshape((3,4))
print(a)
print(a[1])
print(a[1][1])
print(a[1, 1])

print(a[2,:])
print(a[:, 1])
print(a[1, 1:3])

for row in a:
    print(row)
for col in a.T: # tricky means 
    print(col)
    
# Flat
print('a.flatten()', a.flatten())
for item in a.flat:
    print(item)

# Merge
a = np.array([1,1,1])
b = np.array([2,2,2])
c = np.vstack((a, b)) # vertical
print(c)
print(c.shape)


print('=====d=====')
d = np.hstack((a[:,np.newaxis], b[:,np.newaxis])) # horizontal
print(d)
print(d.shape)

# New Axis: add dimension
print('=====Transpose=====')
print(a.T)
e = a[np.newaxis, :]
print(e)
print(e.shape)
e = a[:, np.newaxis]
print(e)
print(e.shape)


# Concat: merge
a = np.array([1,1,1])[:, np.newaxis]
b = np.array([2,2,2])[:, np.newaxis]
c = np.concatenate((a, b, b, a), axis=1)
print(c)
