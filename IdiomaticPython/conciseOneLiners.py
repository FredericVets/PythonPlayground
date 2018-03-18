"""
Two conflicting rules :
    1. Don't put too much on one line. There's an infinite amount of vertical space.
    2. Don't break atoms of thought into subatomic particles.

Raymond's rule:
    -> One logical line of code equals one sentence in English.
"""

# Give me the sum of the squares of all the numbers up to 10.
# Tells what to do step by step.
# Following is to verbose, is actually one logical line.
result = []
for i in range(10):
    square = i ** 2
    result.append(square)
print(sum(result))

# List comprehensions and Generator Expressions :
# Tells what you want, more declarative.
# Single unit of thought.
print(sum([i ** 2 for i in range(10)]))
# Using a generator is even better, no in memory list
print(sum(i ** 2 for i in range(10)))
