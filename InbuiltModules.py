import platform

print(platform.system())
print(platform.version())
print(platform.processor())
print(platform.python_compiler())
print(platform.architecture())
print(platform.machine())
print(platform.uname())


try:
    print(4 / 0)
except ZeroDivisionError:
    print("Sorry, Can't divide by zero (Undifined)")
