### Conditionals ###

my_condition = False    # Con true se ejecuta, con false no se ejecuta

if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")   # Si el if no funciona antes de coger el else coge el elif
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continua")

my_string = "" # String vacio == false # String con palabras == true

if not my_string: # not le da negacion a la variable
    print("My cadena de texto esta vacia")

if my_string == "Mi cadena de textoooo":
    print("Anuel")