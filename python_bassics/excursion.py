# new task
class MyClass:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = MyClass("John", 36)
p1.myfunc()
