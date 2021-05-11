#Raghu Alluri
#Problem J1: Quadrant Selection


x_cor = int(input())
y_cor = int(input())

cor = [x_cor, y_cor]

if -1000<=cor[0]<=1000 and -1000<=cor[1]<=1000:
    if cor[0] != 0 and cor[1] != 0:
        if cor[0] > 0 and cor[1] > 0:
            print(1)
        elif cor[0] < 0 and cor[1] > 0:
            print(2)
        elif cor[0] < 0 and cor[1] < 0:
            print(3)
        elif cor[0] > 0 and cor[1] < 0:
            print(4)
    
