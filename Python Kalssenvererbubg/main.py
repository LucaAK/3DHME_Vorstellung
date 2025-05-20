#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class alenzehic(Person):
    def say_hi(self):
        print(f"HI, ich heiße Alen")
#Hauptprogramm
alenzehic =alenzehic("Alen")
alenzehic.say_hi()