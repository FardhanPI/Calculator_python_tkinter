#Object Oriented Programming

class Sample:
    def hello(zxcvaswd,nm=""):
        print("hello "+ nm)

objx = Sample()
name="Fardhan"
objx.hello()
Sample.hello(objx)


objx.hello(name)
print()
print()
print()

class Class2:
    def hi(self,n):
        self.name=n
    def printName(self):
        print(self.name)

x=Class2()
y=Class2()
name="Fardhan"
x.hi(name)
y.hi("Hi Hello")

x.printName()
y.printName()

