import numpy as np

arr = np.array([[1,2],[3,4]])
print(arr)

np.savetxt('test.csv',arr,delimiter=',')
# arr = genfromtxt('test.csv',delimiter=',')
# print(arr)