class First:
    def Display(self):
        print("First")

class Second(): #multi-level inheritennce
    def Display(self):
        print("Second")

class Third (Second,First):
    def Display_third(self):
        print("Third")

x=Third()
x.Display_third()
x.Display()#Display method of Second class works,
# because it is first inherited or written to Third class

print(Third.mro()) #order check fnctn

