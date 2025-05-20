#Superklasse
class Person:
      def __init__(self, name):
          self.name = name

      def say_hi(self):
          print(f"Hi, ich heiße {self.name}")

#Eigene Klassen
class LukasKeller(Person):
    def __init__(self, name, alter):
        super().__init__(name)
        self.alter = alter

    def say_hi(self):
        print(f"Hi, ich heiße {self.name} und ich bin {self.alter} Jahre alt")
#Hauptprogramm
LukasKeller = LukasKeller("Lukas Keller", 17)
LukasKeller.say_hi()