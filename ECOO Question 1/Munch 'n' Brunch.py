#Raghu Alluri
#March 10th 2018
# N is total students
# Percentages (0.5 0.2 0.1 0.2)
import readingfiles

cost_trip = int(readingfiles.file_cn1)
percent = readingfiles.file_cn2
N = int(readingfiles.file_cn3)

x = bool(50<=cost_trip<=50000)
z = bool(4<=N<=2000)

percentages = percent.split()

y1 = float(percentages[0])
y2 = float(percentages[1])
y3 = float(percentages[2])
y4 = float(percentages[3])

sy1 = N * y1
sy2 = N * y2
sy3 = N * y3
sy4 = N * y4

p1 = sy1 * 12
p2 = sy2 * 10
p3 = sy3 * 7
p4 = sy4 * 5

ptotal = p1 + p2 + p3 + p4

if x == True and z == True:
    ptrip = ptotal / 2
    if ptrip >= cost_trip:
        print('NO')
    else:
        print('YES')

x = input("Press any key to exit:	")
if x.isalpha():
    quit()
else:
    quit()
















