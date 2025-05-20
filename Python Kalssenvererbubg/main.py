#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class lucakabusch(Person):
     def say_hi(self):
         print(f"Hi, ich heiße Luca!")

#Hauptprogramm
lucakabusch = lucakabusch("Luca")
lucakabusch.say_hi()
