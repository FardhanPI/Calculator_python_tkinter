class BaseClass:
    def __init__(self):

        print("Base Init")

    def printer(self):
        print("Base Method")

class SubClass(BaseClass):
    def printer(self):
        print("Sub Method")
        super().printer()
    #this constructer overrided constructer in BaseClass
    def __init__(self):
        print("Sub Init")
        super().__init__()
    # this Method overrided Method in BaseClass


    BaseClass.__init__(self="")




x=SubClass()
x.printer()

