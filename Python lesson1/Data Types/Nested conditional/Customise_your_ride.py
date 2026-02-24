print("Select your ride:")
print("1. bike")
print("2. car")

choice=int(input("Enter your choice:"))

if(choice==1):
    print("What kind of bike?")
    print("1.scootey")
    print("2.scooter")

    choice2=int(input("Select Bike!"))
    if choice2==1:
        print("You have selected scootey!")
    else:
        print("You have selected scooter")

elif(choice==2):
    print("What typr of car?")
    print("1. Suden")
    print("2. XUV")

    choice3=int(input("Select car"))
    if choice3==1:
        print("You have selected Suden")
    else:
        print("You have selected XUV")

else:
    print("Worng choice!!")