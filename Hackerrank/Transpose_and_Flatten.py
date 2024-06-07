# Transpose and Flattten
import numpy
K = list(map(int,input().split()))
L = []
for i in range(K[0]):
    L.append(list(map(int,input().split())))
print(numpy.transpose(numpy.array(L)))
print(numpy.array(L).flatten())
