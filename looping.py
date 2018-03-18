import random_test

for x in range(0, 10):
    print(x, " ", end="")
print()

for x in [2, 4, 6, 8]:
    print(x, " ", end="")
print()

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, len(num_list)):
    for y in range(0, len(num_list[x])):
        print(num_list[x][y], " ", end="")
    print()

random_num = random_test.randrange(0, 100)
count = 0
while random_num != 15:
    print(random_num)
    count += 1
    random_num = random_test.randrange(0, 100)

print("We needed %d tries." % count)
