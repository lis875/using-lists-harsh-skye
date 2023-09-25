import random
restaurants = []
num = input("How many places are you thinking about for lunch?\n")
for i in range(int(num)):
    place = input("Enter the name of restuarant " + str(i) + ": ")
    restaurants.append(place)

print(random.choice(restaurants))
