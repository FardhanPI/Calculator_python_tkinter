class BaseClass:
    def SetName(self,name):
        self.name=name
        print("hello")




class SubClass(BaseClass):
    def welcome(self):
        print("welcome")

    def NameDisplayer(self):
        print(self.name)


xyz=SubClass()

xyz.welcome()
xyz.SetName("Fardhan")
xyz.NameDisplayer()
#this display function is in BaseClass,
# but it inherited to SubClass and accessed through object of SubClass

