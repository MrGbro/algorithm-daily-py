import math

a: int = 2
b: int = 3
d: float = 2.0
e: bool = False

f: str = "Hello"
if a == 2:
    print("a is 2")
print(a ** b)
print(a / b)

x: str = hex(a)
binary: str = bin(a)
print(x)
print(binary)
print(int(binary,2))
print(math.pi)

print(math.pi * (12.5*12.5)*28 /1000)