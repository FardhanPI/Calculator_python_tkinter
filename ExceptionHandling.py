
b=int(input("Enter a number to divide by '4' : "))
try:
    print("Answer : "+str(4 / b))
except ZeroDivisionError:
    print("Sorry, Can't divide by zero (Undefined)")
