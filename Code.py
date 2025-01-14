import numpy as np

A = np.array([[3,-4,1],[-4,8,-4],[1,-4,3]])

x = np.array([[1],[0],[0]])

n = 19

list = [0 for i in range(n)]
list[0] = x
for i in range(n-1):
    list[i+1] = A.dot(list[i])

div = list[n-1]/list[n-2]

print(f"The largest eigenvalue of A is {round(div[0][0],3)}")
