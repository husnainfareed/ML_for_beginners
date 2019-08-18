
import numpy as np

aesterik = "*"

print('\nExample\n')
myList = [1, 2, 3]
x = np.array(myList)
print(x)

print('\nExample\n')
y = np.array([[4, 5, 6, 7], [6, 7, 8, 9]])
print(y)

print('\nExample\n')
print(y.shape)
# show size of matrix like, (2, 3) 2 rows, 3 col


print('\nExample\n')
z = np.arange(0, 30, 2)
print(z)
# will generate range upto 28 of number divided by 2


print('\nExample\n')
x = x.reshape(3, 1)
print(x)
# will convert array into 3 rows and 1 col

print('\nExample\n')
o = np.linspace(0, 2, 9)
print(o)
# return evenly spaced number over a specified interval

print('\nExample\n')
o.resize(3, 3)
print(o)
# return a new array with specified shape


print('\nExample\n')
print(np.ones((3, 2)))
# will return array of ones with shape 3 row, 2 col

print('\nExample\n')
print(np.zeros((4, 4)))
# will return array of zeros with shape 4 row, 4 col


print('\nExample\n')
print(np.eye(3))
# Return a 2-D array with ones on the diagonal and zeros elsewhere


print('\nExample\n')
print(np.diag(o))
# construct a diagonal array


print('\nExample\n')
print(np.array([1, 2, 3] * 4))
# multiply array elements with 4

print('\nExample\n')
print(np.repeat([5, 4, 3], 3))
# multiply each element 3 times

print('\nExample\n')
print(np.ones([2, 3], int))
# Return a new array of given shape and type, filled with ones.

print('\nExample\n')
print(np.vstack([4*x, 3*x]))
# generate 2x3 matrix, row 1 multiplied by 4 with each element,
# row 2 multiplied by 3 with each element


print('\nExample\n')
print(np.hstack([y*2]))
# multiplies each element with 2 and return matrix in original shape


# Operations
print('\nExample\n')
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)
# returns array summing corresponding elements


print('\nExample\n')
print(a*b)
# returns array multiplying corresponding elements


print('\nExample\n')
print(a/b)
# returns array dividing corresponding elements


print('\nExample\n')
print(a-b)
# returns array subtracting corresponding elements


print('\nExample\n')
print(a % b)
# returns array moduling corresponding elements


print('\nExample\n')
print(a**b)
# returns array after 2's power corresponding elements

print('\nExample\n')
print(a.dot(b))
# returns dot product of a and b

print('\nExample\n')
c = np.array([a, a**2])
print(c)
# return 2x3 array, row 1 with original elements, row 2 with power

print('\nExample\n')
print(c.T)
# returns transpose of matrix c

print('\nExample\n')
print(c.dtype)
# returns object's data type

print('\nExample\n')
print(a.sum())
# return sum of all elements of matrix a

print('\nExample\n')
print(a.max())
# returns max value

print('\nExample\n')
print(a.min())
# returns min value

print('\nExample\n')
print(a.mean())
# returns mean of the array

print('\nExample\n')
d = np.arange(13)**2
print(d)
# return matrix of 13 value, each value with exponent 2

print('\nExample\n')
print(str(d[0]) + ", " + str(d[3]) + ", " + str(d[0:3]))

print('\nExample\n')
e = np.arange(36)**2
e.resize(6, 6)
print(e)

print('\nExample\n')
print(e[1:4, 2:5])

print('\nExample\n')
print(e[e > 256])

print('\nExample\n')
test = np.random.randint(0, 10, [4, 3])
print(test)

print('\nExample\n')
for i, row in enumerate(test):
    print("row", i, "is", row)

print('\nExample\n')
test2 = test**2
print(test2)

print('\nExample\n')
for i, j in zip(test, test2):
    print(i, '+', j, '=', i + j)

print('\nExample\n')
n_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(n_array.ravel())
# ravel() method flattens array

print('\nExample\n')
n_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(n_array.ndim)
# returns number of dimension of array
