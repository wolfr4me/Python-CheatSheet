### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente un diccionario

my_other_set = {"Manolo", "Lama", 43}
print(type(my_other_set))  # En el momento que metemos datos se convierte en un set

print(len(my_other_set))

my_other_set.add("Daniel")
print(my_other_set)      # Un set no es una estructura ordenada

my_other_set.add("Daniel")
print(my_other_set)      # Un set no admite repeticiones

print("Daniel" in my_other_set) # Comprobamos si la variable existe en el set
print("Dani" in my_other_set)   # Comprobamos si la variable existe en el set

my_other_set.remove("Daniel")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set                # Con del te cargas todo
#print(my_other_set)

my_set = {"Manolo", "Lama", 43}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"CCS", "HTML", "SI"}

my_new_set = my_set.union(my_other_set) # Unir sets y no acepta repetidos
print(my_new_set.union())
print(my_new_set.union({"Java"}))

print(my_new_set.difference(my_set))    # Quitamos las variables de my_set y solo dejamos las variables de my_new_set






  
