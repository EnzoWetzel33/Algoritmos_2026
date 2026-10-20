from list_ import List

from super_heroes_data import superheroes

from queue_ import Queue

class Superhero():
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name} ({self.alias})"

# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
  
lista_15_heroes = List()
        
for i in range(15):
    hero = superheroes[i]
    lista_15_heroes.append(
        Superhero(
            hero['name'], 
            hero['alias'], 
            hero['real_name'], 
            hero['short_bio'], 
            hero['first_appearance'], 
            hero['is_villain']
        )
    )

def buscar_capitan_america(lista, indice):
    if indice == lista.size():
        return False
    
    if lista[indice].name == "Captain America":
        return True
    
    return buscar_capitan_america(lista, indice + 1)

def listar_superheroes(lista, indice):
    if indice == lista.size():
        return
    
    print(lista[indice])
    
    listar_superheroes(lista, indice + 1)

print("Listado de superheroes")
listar_superheroes(lista_15_heroes, 0)

print("¿Se encuentra el capitan america en la lista?")
if buscar_capitan_america(lista_15_heroes, 0):
    print("Capitán América está en la lista de 15.")
else:
    print("Capitán América NO está en la lista de 15.")


lista_completa_heroes = List()

for hero in superheroes:
    lista_completa_heroes.append(
        Superhero(
            hero['name'], 
            hero['alias'], 
            hero['real_name'], 
            hero['short_bio'], 
            hero['first_appearance'], 
            hero['is_villain']
        )
    )

# A. Listado ordenado de manera ascendente por nombre

def orden_nombre(item):
    return item.name

lista_completa_heroes.add_criterion('name', orden_nombre)
lista_completa_heroes.sort_by_criterion(key_criterion='name')
print("Listado completo")
lista_completa_heroes.show()

# B. Determinar en que posicion esta The Thing y Rocket Raccoon.

pos_the_thing = lista_completa_heroes.search('The Thing', 'name')
pos_rocket = lista_completa_heroes.search('Rocket Raccoon', 'name')

print(f"The Thing se encuentra en la posición (índice): {pos_the_thing}")
print(f"Rocket Raccoon se encuentra en la posición (índice): {pos_rocket}")

# C. Listar todos los villanos de la lista.

print("Listado de villanos")
for personaje in lista_completa_heroes:
    if personaje.is_villain:
        print(personaje)

# D. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.

print("Villanos anteriores a 1980")

cola_villanos = Queue()

for personaje in lista_completa_heroes:
    if personaje.is_villain:
        cola_villanos.arrive(personaje)

for i in range(cola_villanos.size()):
    villano_actual = cola_villanos.on_front()
    
    if villano_actual.first_appearance < 1980:
        print(f"Villano: {villano_actual.name} - Año: {villano_actual.first_appearance}")
    
    cola_villanos.move_to_end()

# E. Listar los superheores que comienzan con  Bl, G, My, y W.

print("Superheroes que comienzan con Bl, G, My, y W")

lista_completa_heroes.filter_start_with(('Bl', 'G', 'My', 'W'))

# F. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.

print("listado por nombre real")

def orden_nombre_real(item):
    return item.real_name

lista_completa_heroes.add_criterion('real_name', orden_nombre_real)
lista_completa_heroes.sort_by_criterion(key_criterion='real_name')
lista_completa_heroes.show()

#G. Listado de superheroes ordenados por fecha de aparación.

print("Listado por año de aparicion")

def orden_año_aparicion(item):
    return item.first_appearance

lista_completa_heroes.add_criterion('first_appearance', orden_año_aparicion)
lista_completa_heroes.sort_by_criterion(key_criterion='first_appearance')
lista_completa_heroes.show()

#H. Modificar el nombre real de Ant Man a Scott Lang.

print("Modificacion del nombre de Ant Man")

pos_ant_man = lista_completa_heroes.search('Ant Man', 'name')
lista_completa_heroes[pos_ant_man].real_name = "Scott Lang"
print(f"Modificado: {lista_completa_heroes[pos_ant_man].name} - Nuevo Nombre Real: {lista_completa_heroes[pos_ant_man].real_name}")

#I. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

print("Personajes con 'time-traveling' o 'suit' en su bio")

lista_completa_heroes.filter_contain_on_bio(['time-traveling', 'suit'])

#J. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

eliminado_electro = lista_completa_heroes.delete_value("Electro", 'name')

if eliminado_electro is not None:
    print(f"Se eliminó correctamente a: {eliminado_electro}")
    print(f"-> Nombre real: {eliminado_electro.real_name} | Alias: {eliminado_electro.alias}")
else:
    print("Electro no se encontraba en la lista.")

eliminado_zemo = lista_completa_heroes.delete_value("Baron Zemo", 'name')

if eliminado_zemo is not None:
    print(f"Se eliminó correctamente a: {eliminado_zemo}")
    print(f"-> Nombre real: {eliminado_zemo.real_name} | Alias: {eliminado_zemo.alias}")
else:
    print("Baron Zemo no se encontraba en la lista.")