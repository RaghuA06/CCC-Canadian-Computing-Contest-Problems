# Raghu Alluri 
# March 11th, 2018

year = int(input())
year = year + 1

Y = bool(0<=year<=10000)

while Y == True:
    year_string = str(year)
    if len(year_string) == 4:
        a = year_string[0]
        b = year_string[1]
        c = year_string[2]
        d = year_string[3]

        A = bool(a==b or a==c or a==d)
        B = bool(b==a or b==c or b==d)
        C = bool(c==a or c==b or c==d)
        D = bool(d==a or d==b or d==c)

        if A == False and B == False and C == False and D == False:
            print(year)
            break
        else:
            year += 1
            continue
    elif len(year_string) == 3:
        a = year_string[0]
        b = year_string[1]
        c = year_string[2]

        A = bool(a==b or a==c)
        B = bool(b==a or b==c)
        C = bool(c==a or c==b)

        if A == False and B == False and C == False:
            print(year)
            break
        else:
            year += 1
            continue

    elif len(year_string) == 2:
        a = year_string[0]
        b = year_string[1]

        A = bool(a==b)
        B = bool(b==a)

        if A == False and B == False:
            print(year)
            break
        else:
            year += 1
            continue

    else:
        print(year)
        break
            









        
