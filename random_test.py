import random

print(random.random())
print(random.randint(1, 100))

numbers = [1, 3, 5, 7, 2, 10]
print(random.choice(numbers))
print(random.shuffle(numbers))
print(numbers)

print(random.sample(numbers, 2))
