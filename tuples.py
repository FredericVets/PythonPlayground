import collections

# Tuples are immutable.
pi_tuple = (3, 1, 4, 1, 5, 9)
pi_list = list(pi_tuple)
new_pi_tuple = tuple(pi_list)

# del pi_tuple[2]  # Error because a tuple is immutable.
del pi_list[2]  # Deletes the number 4.

print(pi_tuple)
print(pi_list)
print(type(pi_tuple[1:]))

print(len(pi_tuple))
print(min(pi_tuple))
print(max(pi_tuple))

tuple_with_one_element = (2, )
print(tuple_with_one_element)

# named tuple is a subclass of tuple, greatly improves clarity
Person = collections.namedtuple("Person", ["name", "age", "gender"])
print(type(Person))
bob = Person(name="Bob", age="30", gender="male")
print(type(bob))
print(bob)