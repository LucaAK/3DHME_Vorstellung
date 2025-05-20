#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class Jonathanburgstaller(Person):
    def say_hi(self):
        print(f"Hi, ich heiße Jonathan!")
#Hauptprogramm
jonathan = Jonathanburgstaller("Jonathan")
jonathan.say_hi()