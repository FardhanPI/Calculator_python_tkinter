
def checkScope():
    def Local():
        test = "Local test"
    def NonLocal():
        nonlocal test
        test = "Non local test"
    def Global():
       global test
       test="Global test"
    test = "Default"
    Local()
    print("Test value after do local: "+test)
    NonLocal()
    print("Test value after do local: "+test)
    Global()
    print("Test value after do local: " + test)

checkScope()
print("Test value after do local: " + test)