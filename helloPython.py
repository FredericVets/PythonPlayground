"""
Notes from Python Programming
https://www.youtube.com/watch?v=N4mEzFDjqtA
by Derek Banas
"""
print("Hello Python")
print('Hello Python')  # single or double quotes are treated the same.
'''
I'm a multiline comment.
'''
name = "Frederic"
print(name)
name = 10
print(name)

# 5 main data types         : Numbers Strings Lists Tuples Dictionaries.
# 7 Arithmetic operators    : + - * / % ** //

print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 * 2 = ", 5 * 2)
print("5 / 2 = ", 5 / 2)
print("5 % 2 = ", 5 % 2)
print("5 ** 2 = ", 5 ** 2)
print("5 // 2 = ", 5 // 2)

# As in all programming languages order of mathematical operation matters.
print("1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)

x = 1
y = 2
print("x:", x, "y:", y)
x, y = y, x
print("x:", x, "y:", y)

quote = "\"Always remember you are unique"
multi_line_quote = ''' just
like everyone else'''
print("%s %s %s" % ("I like the quote", quote, multi_line_quote))

print("I don't like ", end="")
print("newlines")

print("repeat" * 5)
