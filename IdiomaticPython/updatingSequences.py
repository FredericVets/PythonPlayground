from collections import deque

names = ["raymond", "rachel", "matthew", "roger", "betty", "melissa", "judith", "charlie"]

# You're doing it wrong
del names[0]
print(names.pop(0))
names.insert(0, "mark")
print(names)

# Do this instead : use the correct data structure for efficiency
names = deque(["raymond", "rachel", "matthew", "roger", "betty", "melissa", "judith", "charlie"])
del names[0]
print(names.popleft())
names.appendleft("mark")
print(names)
