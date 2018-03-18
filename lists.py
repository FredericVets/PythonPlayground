grocery_list = ["Juice", "Tomatoes", "Potatoes", "Bananas"]

print("First Item : ", grocery_list[0])
grocery_list[0] = "Green Juice"
print("First Item : ", grocery_list[0])

# Sublists
print(grocery_list[1:3])
print(type(grocery_list[:3]))
print(type(grocery_list[-1]))

other_events = ["Wash Car", "Pick Up Kids", "Cash Check"]
# A list can contain other lists as well.
to_do_list = [other_events, grocery_list]
print(to_do_list)
print(len(to_do_list))  # Prints 2.

print(to_do_list[1][1])
grocery_list.append("Onions")
print(grocery_list)

grocery_list.insert(1, "Pickle")

grocery_list.remove("Pickle")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]  # Deletes the Bananas.
print(grocery_list)

# Join lists.
to_do_list2 = other_events + grocery_list
print(len(to_do_list2))  # Prints 7, the two lists are concatenated.

print(max(to_do_list2))  # Compared alphabetically.
print(min(to_do_list2))