#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen

class lusserjohannes(Person):
    def say_hi(self):
        print(f"Hi, ich heiße Johannes!")


#Hauptprogramm
lusserjohannes = lusserjohannes("Johannes")
lusserjohannes.say_hi()