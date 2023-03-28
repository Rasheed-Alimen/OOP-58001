class Person():
  def __init__(self, std, pre, mid, fin):
      self.__std = std
      self.__pre = pre
      self.__mid = mid
      self.__fin = fin
  def Grade(self):
      print(" Average Grade is : ", round((self.__pre + self.__mid + self.__fin) / 3, 2))
      print()
  def Display(self):
      print(self.__std)
      print(" your Prelim grade is : ", self.__pre)
      print(" your Midterm grade is : ", self.__mid)
      print(" your Finals grade is : ", self.__fin)
class std1(Person):
  pass
class std2(Person):
  pass
class std3(Person):
  pass

Student1 = std1("Guy somewan", 87, 89, 92)
Student1.Display()
Student1.Grade()
Student2 = std2("Dood somwer", 89, 88, 91)
Student2.Display()
Student2.Grade()
Student3 = std3("David normal", 88, 81, 96)
Student3.Display()
Student3.Grade()