import function1
from .function1 import odd
for i in range(11):
    print(f"The square of {i} is {function1.square(i)} ")

print(odd(12))