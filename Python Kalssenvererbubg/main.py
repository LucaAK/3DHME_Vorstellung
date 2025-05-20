#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class davidmiskovic(Person):
    def say_hi(self):
        print(f"Hi, ich heiße David!")
#Hauptprogramm
davidmiskovic = davidmiskovic("david")
davidmiskovic.say_hi()