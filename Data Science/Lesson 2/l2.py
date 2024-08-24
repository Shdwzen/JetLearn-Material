import numpy as np

ArrayPre = [1,4,2,6,8,4,9,3,7,4,8]
Array = np.array(ArrayPre)
"""print(Array)
print(Array[4:11:5])
print(Array[Array%2 == 0])"""

def ReList():
    ArrayPre2 = []
    for i in range(len(ArrayPre)):
        NewVal = ArrayPre[i] + 1
        ArrayPre2.append(NewVal)
    return ArrayPre2

print(ReList())

NewList = [[2,3,4],[2,5,7],[1,2,9]]
TwoDList = np.matrix(NewList)
print(type(TwoDList))
DirMatrix = np.matrix("1 3 5;0 7 1;8 9 9")
print(DirMatrix)
print(DirMatrix.T)
IdMatrix = np.identity(4,dtype=int)
print(IdMatrix)

"8x + 7y = 38"
"3x - 5y = -1"
Step1a = np.matrix("8 7;3 -5")
Step1b = np.matrix("38;-1")

InvStep1a = np.linalg.inv(Step1a)
print(np.matmul(InvStep1a,Step1b).astype(int))



