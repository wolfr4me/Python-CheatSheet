### Classes ###

# Las clases se escriben sin "_" y asi MyEmptyPerson
class MyEmptyPerson:
    pass    # Evita la clase

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ***{alias}" # Propiedad publica
        self.__name = name  # Propiedad privada

    def get_name (self):
        return self.__name


    def walk (self):
        print(f"{self.full_name} Esta caminado")


my_person = Person("Manolo", "Lama")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Manolo", "Balao", "Caracas")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Me llaman romeo"
print(my_other_person.full_name)
