class Person:
  def __init__(self, name, age,gender):
    self.name = name
    self.age = age
    self.gender =gender

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36,"male")

p1.age = 40

print(p1.age);
print(p1.gender)

