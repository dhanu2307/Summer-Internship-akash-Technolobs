a = int(input("Enter a value bigger than 100: "))
if(a <= 100 ) :
    if (a % 2) == 0:
        print("{0} is Even".format(a))
    else:
        print("{0} is Odd".format(a))
else:
    print("You entered a value bigger than 100")