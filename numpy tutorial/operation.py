import numpy as np
from mpmath import rand

a = np.array([10, 20, 30, 40])
b = np.arange(4)

# +, -, *, /, **
c = a-b

print(a)
print(b)
print(c)

# Tri func., sin(), cos(), ......
c = 10*np.sin(a)

# >, <, ==, ......
print(b>1)

# Matrix op.
a = a.reshape((2, 2))
b = b.reshape((2, 2))

c = a*b
cDot = np.dot(a, b) # inner product
cDot2 = a.dot(b) # alternative

print(a)
print(b)
print(c)
print(cDot)
print(cDot2)

# Statistic
randomArr = np.random.random((2, 4))
print(randomArr)
print(np.sum(randomArr))
print(np.sum(randomArr, axis=1))
print(np.min(randomArr))
print(np.max(randomArr))
print(np.mean(randomArr))
print(np.median(randomArr))
print(randomArr.mean())
a = np.arange(2, 14).reshape(3,4)
print(np.cumsum(a)) # cumulated sum
print(np.diff(a))   # difference
print(np.nonzero(a))
a = np.arange(14, 2, -1).reshape(3,4)
print(np.sort(a)) # sort by row
print(a)
print(np.median(randomArr, axis=0))


# Transpose
print(np.transpose(a))
print(a.T)

# Arg: to find the index
a = np.arange(2, 14).reshape(3,4)
print(a)
print(np.argmin(a))
print(np.argmax(a))

# Clip
print(np.clip(a, 5, 9)) # Like mid-band filter 
