import argparse
import os
from typing import ChainMap

defaults = {"color": "red", "user": "guest", "os": "Debian", "language": "english", "country": "US"}
print("Default command line args :")
print(defaults)

parser = argparse.ArgumentParser(description="Test reading command line arguments.")
parser.add_argument("-c", "--color", help="Specifies the preferred color.")
parser.add_argument("-u", "--user", help="Specifies the current user.")
parser.add_argument("-o", "--os", help="Specifies the preferred Operating System.")
parser.add_argument("-l", "--language", help="Specifies the user language.")
parser.add_argument("-n", "--country", help="Specifies the current country.")
namespace = parser.parse_args()

actual_command_line_args = {k:v for k, v in vars(namespace).items() if v}
# vars(obj) :   returns the __dict__ attribute for an object (if present).
print("actual_command_line_args:", actual_command_line_args)

# Dont't link them together like this, it will copy all the data:
# result = defaults.copy()
# result.update(os.environ)
# result.update(actual_command_line_args)

# use this instead, doesn't copy but itterates :
result = ChainMap(actual_command_line_args, defaults)
print("Resulting command line args :")
for k, v in result.items():
    print(k, "-->", v)

