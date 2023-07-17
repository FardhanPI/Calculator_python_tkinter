value = 10

def sample():
    fe="ferrum"
 
    global value
    value=10

    print(value)

print(value)
sample()
#fe is local variable-not accessible outside the function
#print(fe)