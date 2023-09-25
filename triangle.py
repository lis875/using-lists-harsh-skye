num = input("what size of triangle do you want to create? ")
for i in reversed(range(int(num))):
    for j in range(int(num)-i):
        print("*", end="")
    print("")
