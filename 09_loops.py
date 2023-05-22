### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2  # Significa sumarle cada vez 2 a my_condition
else:   # Es opcional
    print("Mi condicion es mayor o igual que 10")


print("La ejecuccion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene")
        break   # Sirve para detener la ejecucion del loop
    
    print(my_condition)

print("La ejecuccion continua")

# For

my_list = [35, 24, 62 ,54 ,45 ,54]

for element in my_list: # For se ejecute tantos elementos tenga la lista
    print(element)

my_tuple = (35, 1.77, "Manolo", "Lama")

for element in my_tuple: 
    print(element)

my_set = {"Manolo", "Lama", 43}

for element in my_set: 
    print(element)
    
my_dict = {
    "Nombre":"Brais",
    "Apellido":"Lama",
    "Edad":"35",
    "Lenguajes" : {"Python", "Swift", "Kotlin"},
    1:1.77
}

for element in my_dict: # En diccionario solo imprime las claves
    print(element)
    if element == "Edad":
        continue    # Continua el bucle y detiene la ejecucion en edad y continua
    print("Se ejecuta")
else:
    print("El bucle for para el diccionario ha finalizado")


 
    