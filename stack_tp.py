# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son:
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones: N - S - E - O - NE - NO - SE - SO 
# Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.

from stack_ import Stack

pila_camino = Stack()
pila_regreso = Stack()
pila_aux = Stack()

cantidad = int(input("Cuantos movimientos realizara el robot: "))
print()

contador = 0
while contador < cantidad:
    pasos     = int(input("Pasos: "))
    direccion = input("Direccion (nor/sur/est/oes/ne/no/se/so): ")
    pila_camino.push({"pasos": pasos, "direccion": direccion})
    contador += 1

while pila_camino.size() > 0:
    movimiento = pila_camino.pop()
    pila_aux.push(movimiento)

print()
print("Camino recorrido por el robot:")
print()
pila_aux.show()
print()

while pila_aux.size() > 0:
    movimiento = pila_aux.pop()
    dir_actual = movimiento["direccion"]
    dir_vuelta = None

    if dir_actual == "nor":
        dir_vuelta = "sur"
    elif dir_actual == "sur":
        dir_vuelta = "nor"
    elif dir_actual == "est":
        dir_vuelta = "oes"
    elif dir_actual == "oes":
        dir_vuelta = "est"
    elif dir_actual == "ne":
        dir_vuelta = "so"
    elif dir_actual == "so":
        dir_vuelta = "ne"
    elif dir_actual == "no":
        dir_vuelta = "se"
    elif dir_actual == "se":
        dir_vuelta = "no"

    pila_regreso.push({"pasos": movimiento["pasos"], "direccion": dir_vuelta})

print("Secuencia de regreso al punto de partida:")
print()
pila_regreso.show()
print()

# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone:
#     Nombre - Cantidad de películas de la saga en la que participó. Implementar las funciones necesarias para resolver las siguientes actividades:
# a. Determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición 1 la cima de la pila;
# b. Determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. Determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. Mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from stack_ import Stack

pila_mcu = Stack()

pila_mcu.push({"nombre": "Thor",           "pelis": 8})
pila_mcu.push({"nombre": "Groot",          "pelis": 5})
pila_mcu.push({"nombre": "Doctor Strange", "pelis": 4})
pila_mcu.push({"nombre": "Black Widow",    "pelis": 7})
pila_mcu.push({"nombre": "Captain America","pelis": 5})
pila_mcu.push({"nombre": "Deadpool",       "pelis": 3})
pila_mcu.push({"nombre": "Gamora",         "pelis": 6})
pila_mcu.push({"nombre": "Rocket Raccoon", "pelis": 6})
pila_mcu.push({"nombre": "Iron Man",       "pelis": 9})
pila_mcu.push({"nombre": "Clint Barton",   "pelis": 5})

pila_mcu.show()
print()

print("a. Posicion de Rocket Raccoon y Groot en la pila:")
print()

pila_aux = Stack()
posicion        = 1
pos_rocket      = None
pos_groot       = None

while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()

    if personaje["nombre"] == "Rocket Raccoon":
        pos_rocket = posicion
    if personaje["nombre"] == "Groot":
        pos_groot = posicion

    pila_aux.push(personaje)
    posicion += 1

if pos_rocket != None:
    print("Rocket Raccoon se encuentra en la posicion:", pos_rocket)
if pos_groot != None:
    print("Groot se encuentra en la posicion:", pos_groot)
print()


while pila_aux.size() > 0:
    pila_mcu.push(pila_aux.pop())
print("b. Personajes que participaron en mas de 5 peliculas:")
print()

pila_aux = Stack()

while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()

    if personaje["pelis"] > 5:
        print("Nombre:", personaje["nombre"])
    pila_aux.push(personaje)

print()

print("c. Cantidad de peliculas de Black Widow:")
print()

pelis_bw  = None

while pila_aux.size() > 0:
    personaje = pila_aux.pop()

    if personaje["nombre"] == "Black Widow":
        pelis_bw = personaje["pelis"]

    pila_mcu.push(personaje)

if pelis_bw != None:
    print("Black Widow participo en", pelis_bw, "peliculas")
print()

print("d. Personajes cuyo nombre empieza con C, D o G:")
print()

while pila_mcu.size() > 0:
    personaje = pila_mcu.pop()
    inicial   = personaje["nombre"][0]

    if inicial == "C" or inicial == "D" or inicial == "G":
        print("Nombre:", personaje["nombre"])
print()