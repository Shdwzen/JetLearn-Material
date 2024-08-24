import numpy as np

"""List = [1,3,2,6,7]
List2 = [4,8,2,0,1]

ListResult = List + List2
print(ListResult)"""

Array = np.array(List)
Array2 = np.array(List2)
Array3 = np.arange(1,91)
Array4 = np.linspace(1,10,19)
FullArray = Array3.reshape(3,3,10)
print(FullArray.ndim)
print(FullArray)

"""SqrtVal = int(np.sqrt(25))
print(SqrtVal)"""