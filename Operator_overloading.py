class sample:
    def set_name(self,name):
        self.name=name

    def __add__(self, other):
        name=self.name+other.name
        return name

first_name=sample()
second_name=sample()


first_name.set_name("Fardhan ")
second_name.set_name("PI")

First_method_full_name=first_name.name+second_name.name #this is a striaght way
Second_method_full_name=first_name+second_name #this is a special method

print(First_method_full_name)
print(Second_method_full_name)



