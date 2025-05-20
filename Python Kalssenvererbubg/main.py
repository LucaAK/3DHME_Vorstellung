#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class simon (Person):
    def say_hi(self):
        print(f"Hi, ich heiße Simon") 
#Hauptprogramm
simonpichler = simon("Simon")
simonpichler.say_hi()
