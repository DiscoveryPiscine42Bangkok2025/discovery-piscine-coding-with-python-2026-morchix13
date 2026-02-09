#!/usr/bin/env python3

a = int(input())
b = int(input())

result = a * b

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

print(result)
