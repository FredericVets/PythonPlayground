person = ("John", "Doe", 0x30, "john@doe.com")
print(type(person))

# Don't do this :
fname = person[0]
lname = person[1]
age = person[2]
email = person[3]
print(fname, lname, age, email)

# Do it like this instead (use tuple unpacking) :
fname, lname, age, email = person
print(fname, lname, age, email)