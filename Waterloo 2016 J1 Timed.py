# Raghu Alluri
#5 or 6 = 1, 3 or 4 = 2, 1 or 2 = 3, none = -1

t1 = input().upper()
t2 = input().upper()
t3 = input().upper()
t4 = input().upper()
t5 = input().upper()
t6 = input().upper()

t_list = [t1, t2, t3, t4, t5, t6]
count = t_list.count('W')

if count == 5 or count == 6:
    print(1)
elif count == 3 or count == 4:
    print(2)
elif count == 1 or count == 2:
    print(3)
elif count == 0:
    print(-1)

