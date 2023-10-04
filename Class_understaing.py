class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def languages(self):
        print("the languages he knows are \n C \n C++ \n HTML \n Pyhton \n Java \n Css \n")
a = Employee("anant", 10)
print(a.name)
print(a.age)
a.languages()