def f1():
    return "f1"


def f2():
    return "f2"


x = f2  # now x is a reference to 2nd function memory address
f2 = f1  # now f2 is a reference to 1st function memory address

print(f1())
print(f2())

f2 = x # now f2 is again reference to 2nd function memory address

print(f1())
print(f2())
