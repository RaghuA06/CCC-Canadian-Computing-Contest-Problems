# Raghu Alluri

# Problem J2: Shifty Sum
# 12, shift it 3 times, 12 + 120 + 1200 + 12000 = 13332
# N is the number and k is the number of times you want to shit the number.

def shifting_number(N, k):
    r = 10
    d = r - 1
    exp = pow(r, k + 1) - 1
    shift_sum = int((N * exp) / d)
    print(shift_sum)

N = int(input())
k = int(input())

shifting_number(N, k)
        
