"""
A Dictionary is The Fundamental tool for expressing relationships, linking, counting and grouping.
"""
from collections import defaultdict, ChainMap

d = {
    "matthew": "blue",
    "rachel": "green",
    "raymond": "red"
}

# This will itterate over the keys.
for k in d:
    print(k)

# Make a copy of the dictionary
my_dict = dict(d)
# This will also itterate over the keys.
# You shouldn't and can't modify a dictionary when you're itterating over it.
for k in list(my_dict.keys()):
    if k.startswith('r'):
        del my_dict[k]
print(my_dict)

my_dict = {k: d[k] for k in d if not k.startswith('r')}
print(my_dict)


# Looping over a dictionary keys and values
# Don't do this, causes slow down. It rehashes every key and does a lookup on it.
for k in d:
    print(k, "-->", d[k])
# Do it like this (with tuple unpacking)
for k, v in d.items():
    print(k, "-->", v)


# Construct a dictionary from pairs.
names = ["raymond", "rachel", "matthew"]
colors = ["red", "green", "blue"]

d = dict(zip(names, colors))
print(d)


# Counting with dictionaries
colors = ["red", "green", "red", "blue", "green", "red"]
# The default way
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)

# Using get, lookup will not raise an error when unknown key is specified.
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)


d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)

# Grouping with dictionaries
names = ["raymond", "rachel", "matthew", "roger", "betty", "melissa", "judith", "charlie"]
# Basic
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)

# More elegant
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print(d)

# Even more elegant ... The new idiom to grouping.
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)


# Is dictionary popitem() atomic (removes item)?
# Yes, so no need for locking in multi-threading context.
d = {"matthew": "blue", "rachel": "green", "raymond": "red"}
while d:
    key, value = d.popitem()
    print(key, "-->", value)
# The source is now empty.
print(d)

# Linking dictionaries together.
defaults = {"color": "red", "user": "guest", "os": "Debian"}
user_values = {"user": "matthew"}
environment_values = {"os": "Ubuntu"}

# Don't do this : it will copy all the data.
actuals = defaults.copy()
actuals.update(user_values)
actuals.update(environment_values)
print(actuals)
# use this instead :
actuals = ChainMap(user_values, environment_values, defaults)
for k, v in actuals.items():
    print(k, "-->", v)

