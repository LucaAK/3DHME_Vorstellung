#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class davidoberzaucher(Person):
    def say_hi(self):
        print(f"Hi, ich heiße David")

#Hauptprogramm
davidoberzaucher = davidoberzaucher("David")
davidoberzaucher.say_hi()