import sys


def add(x, y):
    return x + y


print(add(1, 4))
addLambda = lambda x, y: x + y
print(addLambda(1, 4))

print("Whatis your name?")
name = sys.stdin.readline()

print("Hello and goodbye", name)
