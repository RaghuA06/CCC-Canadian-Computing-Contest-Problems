# Raghu Alluri
# Special Day is February 18th

month = int(input())
day = int(input())

year = [month, day]

if year[0] > 2:
    print('After')
elif year[0] < 2:
    print('Before')
elif year[0] == 2 and year[1] == 18:
    print('Special')
elif year[0] == 2 and year[1] > 18:
    print('After')
elif year[0] == 2 and year[1] < 18:
    print('Before')
