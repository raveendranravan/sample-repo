import math
import os
import sys

import requests

name = input("Your name?")
print("Hi,", name)

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Ravee'))
r = requests.get("https://www.google.com")
print(r.status_code)
