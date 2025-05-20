#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class Konrad(Person):
    def say_hi(self):
        print(f"Hi, ich heiße Konrad")

#Hauptprogramm
konradkrakolinig = konradkrakolinig("Konrad")
konrad.say_hi()