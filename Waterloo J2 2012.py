# Raghu Alluri

d_1 = int(input())
d_2 = int(input())
d_3 = int(input())
d_4 = int(input())

depthRise = bool(d_1 < d_2 < d_3 < d_4)
depthDiving = bool(d_1 > d_2 > d_3 > d_4)
depthConstant = bool(d_1 == d_2 == d_3 == d_4)

if depthRise == True:
    print('Fish Rising')
elif depthDiving == True:
    print('Fish Diving')
elif depthConstant == True:
    print('Fish At Constant Depth')
else:
    print('No Fish')
