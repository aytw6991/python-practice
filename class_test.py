class Person:

    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address


person1 = Person("Ram", 24, "Male", "Kathmandu")

print(person1.name+" , "+str(person1.age))
