long_string = "I'll catch you if you fall - The Floor"

sub_string = long_string[:4]
print(sub_string)
print(type(sub_string))

print(long_string[-5:])
print(long_string[:-12])

if "Floor" in long_string:
    print("Floor found!")

print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f" %
      ('X', "favorite", 1, 3.14))

print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())
quote_list = long_string.split(" ")
print(quote_list)

# Concatenating strings :
names = ["raymond", "rachel", "matthew", "roger", "betty", "melissa", "judith", "charlie"]
# Don't do it like this :
s = names[0]
for name in names[1:]:
    s += ", " + name
print(s)
# Do it like this instead, always use join()
print(", ".join(names))