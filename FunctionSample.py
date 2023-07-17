def printer():
    print((5 + 10) * 10)


printer()
printer()
printer()
printer()


# functn with argument
def adder(a):
    rst = int(a) + 10
    print(rst)


value = int(input("Enter a value"))
adder(value)


# albetry argument(unlimited argument)-work as list
def unlimiter(*values):
    print(values)
    for k in range(len(values)):
        print(str(k + 1) + " : " + str(values[k]))


hjgfjhg = "gkjgkh"
unlimiter(10, "fardhan", "lasin", "rahan", hjgfjhg, 15, 20, 30, 40, 28, 14)
