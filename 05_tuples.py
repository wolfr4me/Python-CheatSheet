### Tuples ###

my_tuple = tuple()      # Una tupla es un conjunto de valores
my_other_tuples = ()    # La lista se define con [] y la tupla con ()

my_tuple = (35, 1.77, "Manolo", "Lama")
my_other_tuples = (12, 34, 12 ,45 )
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Manolo"))
print(my_tuple.index("Lama"))
print(my_tuple.index("Manolo"))

#my_tuple[1] = 1.80
print(my_tuple)         # Las Tuplas son valores constantes no pueden cambiar, eso es la principal diferencia con las listas 

my_sum_tuple = my_tuple + my_other_tuples
print(my_sum_tuple)
print(my_tuple + my_other_tuples)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)  # Transformar tupla en lista
print(type(my_tuple))

my_tuple[3] = "Manolo"
my_tuple.insert(1, "Rojo")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))

del my_tuple              # Elimina la tupla
#print(my_tuple)






