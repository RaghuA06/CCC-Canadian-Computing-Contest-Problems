# Raghu Alluri
# March 11th 2018
# Input: 120 71 --> 120, 71, 49, 22, 27.

t1 = int(input())
t2 = int(input())

t1b = bool(0 < t2 < t1 < 10000)

length = 2
while t1b == True:
    length += 1
    tm = t1 - t2
    t1 = t2
    t2 = tm
    if tm < 0:
        print(length - 1)
        break
    else:
        continue
    
