import threading
import decimal
import contextlib

# Don't do the following when factoring out temporary contexts :
import os

import sys
from Tools.scripts.objgraph import ignore

print(decimal.Decimal(355) / decimal.Decimal(113))

old_context = decimal.getcontext().copy()
decimal.getcontext().prec = 50
print(decimal.Decimal(355) / decimal.Decimal(113))
decimal.setcontext(old_context)

# Do it like this :
with decimal.localcontext(decimal.Context(prec=50)):
    print(decimal.Decimal(355) / decimal.Decimal(113))
# Back to the old context.
print(decimal.Decimal(355) / decimal.Decimal(113))


# Same principle when opening and closing files
# Don't do :
# Create the file
f = open("foo.txt", mode="x")
f.write("bla")
f.close()

f = open("foo.txt", mode="r")
try:
    data = f.read()
finally:
    f.close()

# Do this instead :
with open("foo.txt") as f:
    data = f.read()

# remove the file.
os.remove("foo.txt")

# Same principle when acquiring and releasing locks
# Don't do :
lock = threading.Lock()
lock.acquire()
try:
    print("Critical section 1")
    print("Critical section 2")
finally:
    lock.release()

# Do this instead :
with lock:
    print("Critical section 1")
    print("Critical section 2")


# Factoring out temporary contexts
# Don't do :
file_name = "non-existing-file.tmp"
try:
    os.remove(file_name)
except OSError:
    pass
# Do :
def remove_file_no_error(file_name):
    with contextlib.suppress(OSError):
        os.remove(file_name)


# Help sends it output directly to stdout.
# But I want it to go to a file ... So redirect it manually :
file_name =  "pow_function_help.txt"
remove_file_no_error(file_name)
with open(file_name, mode="w") as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

# More elegant :
# This way you can write your functions with print statements and wrap them with "with" statements
# to redirect them to files, stderr
# Restores the beauty of using print everywhere.
remove_file_no_error(file_name)
with open(file_name, mode="w") as f:
    with contextlib.redirect_stdout(f):
        help(pow)
