#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class Florian(Person):
    def say_hi(self):
        print(f"Hi, ich heiße Florian")

#Hauptprogramm

Florian = Florian("Florian")
Florian.say_hi()