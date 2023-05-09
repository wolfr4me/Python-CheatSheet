### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido":"Lama", "Edad":"35", 1:"Python"}
my_dict = {
    "Nombre":"Brais",
    "Apellido":"Lama",
    "Edad":"35",
    "Lenguajes" : {"Python", "Swift", "Kotlin"},
    1:1.77
}
print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" # Dentro del diccionario se pueden actualizar los valores
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle muñon" # De esta manera se añaden nuevos datos al diccionario
print(my_dict)

del my_dict["Calle"] # Eliminar elementos del diccionario
print(my_dict)

print("Nombre" in my_dict)
print("Brais" in my_dict)   # Tenemos que buscar clave no por nombres


print(my_dict.items())  # Listado de todo
print(my_dict.keys())   # Listado claves
print(my_dict.values()) # Listado valores

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))     # Crea diccionario sin valores y con las claves ya creadas
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Brais", "Moure")) #Mete en la claves los valores que se ponen
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))











