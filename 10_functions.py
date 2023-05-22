### Functions ###

def my_function ():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values (first_number, second_number):   # Sirve para introducir valores y luego rellenarlos al ejecutar la funcion
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(241234, 3452345243)
sum_two_values("5", "7")
sum_two_values(1.3, 3.2)


def sum_two_values_with_return (first_number, second_number):   
    return first_number + second_number

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Man")

def print_name_1 (name, surname, alias = "Sin alias"):  # "Sin alias" sirve para si no hay valor que se ponga "Sin alias" automaticamente
    print(f"{name} {surname} {alias}")

print_name_1("Moure", "Lama")
print_name_1("Moure", "Lama", "Br")

def print_texts(*texts): # El * indica que puedo poner infinitos paramateros de un mismo tipo
    for text in texts:
        print(text)

print_texts("Hola", "de", "Mas")



