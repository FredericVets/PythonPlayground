"""
Most of the time whenever you're using an index directly : your doing it wrong.

    Some brief explanation :
    1. Iterables:
            An iterable is an object with an __iter__() method, which creates an iterator.
            E.g. lists, strings, files.
            Everything you can use in a for ... in ... is an iterable. (for creates the iterator behind the scenes)
            You can iterate over iterables as much as you want. All values are stored in memory.
    2. Iterators:
            An iterator is an object with an __next__() method
            Used to iterate over iterables. Every iterable contains a way of creating an iterator (__iter__).
    3. Generators:
            Generators are iterators. A special kind of iterator you can only iterate over once.
            Generators do not store all the values in memory, they generate values on the fly.
    4. Yield statement:
            yield is a keyword that is used like return, except the function will return a generator.
            To master yield, you must understand that when you call the function, the code you have written in the
            function body does not run. The function only returns the generator object, this is a bit tricky :-)
            Then, your code will be run each time the for uses the generator.

            The first time the for calls the generator object created from your function, it will run the code in your
            function from the beginning until it hits yield, then it'll return the first value of the loop.
            Then, each other call will run the loop you have written in the function one more time, and return the next
            value, until there is no value to return.
            The generator is considered empty once the function runs but does not hit yield anymore. It can be because
            the loop had come to an end, or because you do not satisfy an "if/else" anymore.

    See : https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
"""

from functools import partial
import random

# Don't do this :
for i in [0, 1, 2, 3, 4, 5]:
    print(i ** 2)

# Do this instead :
# Uses the range generator that creates the values.
for i in range(6):
    print(i ** 2)


# Function that will return a generator.
def create_number_generator(count):
    for i in range(count):
        yield i


# Create the generator that can only be used ONCE.
my_generator = create_number_generator(6)
for i in my_generator:
    print(i ** 2)
print("Second time. Will show no results.")
for i in my_generator:
    print(i ** 2)
print("See, Nothing happened.")

# Achieve the same with a list comprehension, which creates a list.
my_list = [i ** 2 for i in range(6)]
for i in my_list:
    print(i)

# Create a generator, which can only be used once.
my_generator = (i ** 2 for i in range(6))
for i in my_generator:
    print(i)
print("Second time. Will show no results.")
for i in my_generator:
    print(i)
print("See, Nothing happened.")


colors = ["red", "green", "blue", "yellow"]
# Don't do this :
for i in range(len(colors)):
    print(colors[i])
# Do this instead
for color in colors:
    print(color)

# Loop backwards
# Don't do this :
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])
# Do this instead :
for color in reversed(colors):
    print(color)


# Looping over a collection and indicies at the same time.
# Don't do this :
for i in range(len(colors)):
    print(i, "-->", colors[i])
# Do this instead :
for i, color in enumerate(colors):
    print(i, "-->", colors[i])


# Looping over 2 collections.
names = ["raymond", "rachel", "matthew"]
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], "-->", colors[i])
# Do this instead :
for name, color in zip(names, colors):
    print(name, "-->", color)


# Looping in sorted order
for color in sorted(colors):
    print(color)
for color in sorted(colors, reverse=True):
    print(color)
# Custom sort order.
print(sorted(colors, key=len))


# partial: takes a function with many arguments and transforms it into a function with fewer arguments.
six_numbers = partial(create_number_generator, 6)
for i in iter(six_numbers()):
    print(i)

# Call a function until a sentinel value (break style programming)
# traditionally :
numbers = []
sentinel = 12
while True:
    number = random.randint(0, 50)
    if number == sentinel:
        break
    numbers.append(number)
print("sentinel hit after ", len(numbers), "tries : ", numbers)

# Use the iter() function instead :
numbers = list(iter(partial(random.randint, 0, 50), sentinel))
print(numbers)
print("sentinel hit after ", len(numbers), "tries : ", numbers)


# Distinguishing multiple exit points in a loop.
def find(sequence, target):
    # A for can have an else... what?
    # The else clause of a for will be executed when no break occurred.
    for i, value in enumerate(sequence):
        if value == target:
            break
    else:
        # the no-break part
        return -1
    return i


print(find(create_number_generator(6), 5))  # returns 5
print(find(create_number_generator(6), 6))  # returns -1 (no break occurred)


