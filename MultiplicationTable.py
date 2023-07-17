number=int(input("Enter a number for its Multiplication table : "))
limit=int(input("Then enter the limit : "))

for x in range(limit):
    x=x+1
    result=x*number
    print(str(x)+" x "+str(number)+" = "+str(result))

