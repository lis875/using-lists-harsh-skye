length = input("What length of rectangle do you want to create? ")
width = input("What width of rectangle do you want to create? ")
for i in reversed(range(int(length))):
    for j in range(int(width)):
        print("*", end="")
    print("")
