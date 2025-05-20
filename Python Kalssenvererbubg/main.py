#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class Raphael(Person):
    def say_hi(self):
         print(f"Hi, ich heiße Raphael")
#Hauptprogramm
raphaelhofer = Raphael("Raphael Hofer")
raphaelhofer.say_hi()