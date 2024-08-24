import math as m
Numbs = [13,53,4,3,1,56,24,666,2334,53,32,5,34454]

def EvenDigitCount(array):
    Count = 0
    for i in range(len(array)):
        Digit = int(m.log10(array[i]))+1
        if Digit%2==0:
            Count += 1
    print("The total values are: %s \nThe total values with an even number of digits are: %s"%(len(array),Count))

EvenDigitCount(Numbs)

