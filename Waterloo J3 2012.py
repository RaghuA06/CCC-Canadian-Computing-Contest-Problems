# Raghu Alluri
# *x*
#   xx
# *  *

print("Depending on your value of k, this will maximize your icon by the value of k. \nYour value of k, although, has to be lower than 25 as greater than this value will be too big.")

endLoop = False
while not endLoop:
    try:
        print("\n")
        k = int(input("Enter value of k:	"))
        
        side = 3 * k
        num_x = k
        print("\n")
        for i in range(k):
            print(k * "*" + k * "x" + k * "*")
        for j in range(k):
            print(k * "  " + k * "xx")
        for m in range(k):
            print(k * "*" + k * "  " + k * "*")
    except Exception as e:
        print("\nOops. Something went wrong.\nYour value of k might be a floating point.")
        
        again = input("Would you like to quit: [yes/no]: 	").lower()
        if again == "yes":
            continue
        else:
            endlLoop = True


