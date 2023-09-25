import random
count = 0
times = input("how many times should the coin be flipped?\n")
for i in range(int(times)):
  num = random.randint(1,2)
  if (num == 1):
    print("Heads")
    count = count + 1
  else:
    print("Tails")

print(count)
