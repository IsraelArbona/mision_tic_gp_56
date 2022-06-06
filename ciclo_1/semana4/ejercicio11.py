# libreria numpy
import numpy as np

'''
a = np.array(
    [34,25,7]
)

print(type(a))
# print(dir(a))
print(a)
print(a.shape)

print(a[0],a[1],a[2])
a[0] = 5
print(a)
'''

'''
b = np.array(
    [
        [1,2,3],
        [4,5,6],
    ]
)

print(b, '\n')
print(b.shape)
print(b[0,0], b[0,1], b[0,2], b[1,2])
'''

matriz = np.zeros((3,3))
print(matriz)

b_one = np.ones((2,3))
print(b_one)

c_full = np.full((5,5),8)
print(c_full)

d = np.eye(4)
print(d)

e = np.random.random((6,6))
print(e)