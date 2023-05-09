### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))



my_list = [35, 24, 62 ,54 ,45 ,54]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Manolo", "Lama"]

print(my_list + my_other_list)

print(type(my_other_list))
print(type(my_list))

print(my_other_list[-1])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-4])

print(my_list.count(54)) # Cuenta valores repetidos

age, height, name, surname = my_other_list # Mismo numero de elementos que la lista
print(name)

age, height, name, surname = my_other_list = my_other_list[1], my_other_list[2], my_other_list[0], my_other_list[3]
print(name)

print(my_list, my_other_list)

my_list.append("Dani") # Agrega al final de la lista un elemento
print(my_list)

my_list.insert(2, "Daniel") # Inserta el elemento en la posición que le indiquemos
print(my_list)

my_list[2] = "Manolo" # Sirve para cambiar un elemento
print(my_list)

my_list.remove("Dani") # Borra el elemento (si esta repitido solo borra 1)
print(my_list)

print(my_list.pop(1)) # Elimina el ultimo elemento , y lo desapila
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy() # Copiamos la lista a otra lista

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # Se le da la vuelta a la lista
print(my_new_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))

print(my_new_list[1:3]) # Cojemos los valores seleccionados






