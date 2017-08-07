import numpy as np

# Simple array
array = np.array([[1,2,3],
                  [4,5,6]], dtype=np.int) # np.float32, np.int32, ......

print('Array=')
print(array, '\n')
print('Type of array: ', type(array))
print('Type of element: ', array.dtype)
print('Number of dim: ', array.ndim)
print('Shape: ', array.shape)
print('Size: ', array.size)

# Array with all zero's
zeroArr = np.zeros((3,4), dtype=np.int) #1st arg: shape, 2nd:dtype
print('=====Zero\'s=====')
print(zeroArr)
# Array with all one's
oneArr = np.ones((3,4), dtype=np.int)
print('=====One\'s=====')
print(oneArr)
# Array with all empty's
emptyArr = np.empty((3,4), dtype=np.int)
print('=====One\'s=====')
print(emptyArr)

# A range
arangeArr = np.arange(5, 20)
arangeArr = np.arange(12)
print('=====Arange\'s=====')
print(arangeArr)

# Reshape
reshapeArr = arangeArr.reshape((3,4))
print('=====Reshape\'s=====')
print(reshapeArr)

#Line
lineArr = np.linspace( 0, 20, 10)
print('=====Line\'s=====')
print(lineArr)

#Random
randomArr = np.random.random((2, 4))
print('=====Random\'s=====')
print(randomArr)
