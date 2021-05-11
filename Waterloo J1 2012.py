# Raghu Alluri
# 1-20,  21-30,  31 ~

class carSpeeds:
    fines = ['$100', '$270', '$500']
    
limit = int(input("Enter the speed limit:	"))
speed = int(input("Enter the recorded speed of the car:	"))

over_limit = speed - limit

if over_limit <= 0:
    print('Congratulations, you are  within the speed limit!')
elif 1<= over_limit <=20:
    print('You are speeding and your fine is %s' % (carSpeeds.fines[0]))
elif 21 <= over_limit <= 30:
    print('You are speeding and your fine is %s' % (carsSpeeds.fines[1]))
elif over_limit >= 31:
    print('You are speeding and your fine is %s' % (carSpeeds.fines[2]))
