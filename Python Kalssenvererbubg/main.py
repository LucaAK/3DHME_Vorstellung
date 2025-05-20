#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class dominicsmole(Person):
     def say_hi(self):
          print(f"Hi, ich heiße Dominic!")

#Hauptprogramm
dominicsmole = dominicsmole("Dominic")
dominicsmole.say_hi()