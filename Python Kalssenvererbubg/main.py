#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class markopetkovic(Person):
    def say_hi(self):
        print(f"Hi, ich heiße Marko!")







#Hauptprogramm
markopetkovic = markopetkovic("Marko")
markopetkovic.say_hi()
