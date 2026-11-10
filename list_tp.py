# Ejercicio Nº 6 de la guia de ejercicios de listas del libro.

# from list_ import List


# superheroes = [
#     {
#       "nombre": "Spider-Man",
#       "anio_aparicion": 1962,
#       "casa": "Marvel",
#       "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance en el Daily Bugle mientras protege Nueva York."
#     },
#     {
#       "nombre": "Iron Man",
#       "anio_aparicion": 1963,
#       "casa": "Marvel",
#       "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores y director de Stark Industries."
#     },
#     {
#       "nombre": "Wolverine",
#       "anio_aparicion": 1974,
#       "casa": "Marvel",
#       "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."
#     },
#     {
#       "nombre": "Thor",
#       "anio_aparicion": 1962,
#       "casa": "DC",
#       "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra. Miembro fundador de los Vengadores."
#     },
#     {
#       "nombre": "Black Widow",
#       "anio_aparicion": 1964,
#       "casa": "Marvel",
#       "biografia": "Natasha Romanoff fue entrenada desde niña en el programa Habitación Roja. Es una espía y agente de élite de S.H.I.E.L.D., experta en artes marciales y tecnología."
#     },
#     {
#       "nombre": "Batman",
#       "anio_aparicion": 1939,
#       "casa": "DC",
#       "biografia": "Bruce Wayne presenció el asesinato de sus padres de niño y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y entrenamiento físico para combatir el crimen. Usando un traje con muchas herramientas"
#     },
#     {
#       "nombre": "Superman",
#       "anio_aparicion": 1938,
#       "casa": "DC",
#       "biografia": "Kal-El fue enviado desde el planeta Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."
#     },
#     {
#       "nombre": "Mujer Maravilla",
#       "anio_aparicion": 1941,
#       "casa": "DC",
#       "biografia": "Diana, princesa de las Amazonas de la isla Temyscira, fue criada como guerrera. Porta el lazo de la verdad y las brazaletes indestructibles. Embajadora de paz y justicia."
#     },
#     {
#       "nombre": "The Flash",
#       "anio_aparicion": 1956,
#       "casa": "DC",
#       "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo durante un experimento. Obtuvo la capacidad de moverse a velocidades superlumínicas conectado a la Fuerza de la Velocidad."
#     },
#     {
#       "nombre": "Green Lantern",
#       "anio_aparicion": 1959,
#       "casa": "DC",
#       "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo. El anillo le permite crear construcciones de energía verde limitadas solo por su voluntad e imaginación."
#     },

#     {
#       "nombre": "Dr. Strange",
#       "anio_aparicion": 1963,
#       "casa": "DC",
#       "biografia": "Stephen Strange fue un neurocirujano que, tras un accidente, se convirtió en el Hechicero Supremo y protege la Tierra de amenazas místicas."
#     },
#     {
#       "nombre": "Capitana Marvel",
#       "anio_aparicion": 1968,
#       "casa": "Marvel",
#       "biografia": "Carol Danvers fue piloto de la fuerza aérea. Tras una explosión obtuvo superfuerza, vuelo y la capacidad de absorber energía."
#     },
#     {
#       "nombre": "Star-Lord",
#       "anio_aparicion": 1976,
#       "casa": "Marvel",
#       "biografia": "Peter Quill fue criado en el espacio y lidera a los Guardianes de la Galaxia. Usa pistolas de elementos y botas con propulsores."
#     }
# ]


# class Superhero():

#     def __init__(self, nombre, anio, casa, bio):
#         self.name = nombre
#         self.year = anio
#         self.house = casa
#         self.bio = bio

#     def __str__(self):
#         return f"{self.name} - {self.year} - {self.house}"


# def by_name(item):
#     return item.name

# def by_year(item):
#     return item.year


# # Funciones

# def mostrar_anio(lista, nombre):
#     pos = lista.search(nombre, 'name')
#     if pos is not None:
#         print(f'el anio de aparicion de {lista[pos].name} es {lista[pos].year}')
#     else:
#         print(f'{nombre} no esta en la lista')


# def cambiar_casa(lista, nombre, nueva_casa):
#     pos = lista.search(nombre, 'name')
#     if pos is not None:
#         lista[pos].house = nueva_casa
#     else:
#         print(f'{nombre} no esta en la lista')


# def mostrar_casa(lista, nombre):
#     pos = lista.search(nombre, 'name')
#     if pos is not None:
#         print(f'la casa de {lista[pos].name} es {lista[pos].house}')
#     else:
#         print(f'{nombre} no esta en la lista')


# def mostrar_datos(lista, nombre):
#     pos = lista.search(nombre, 'name')
#     if pos is not None:
#         hero = lista[pos]
#         print(f'nombre: {hero.name}')
#         print(f'anio de aparicion: {hero.year}')
#         print(f'casa: {hero.house}')
#         print(f'biografia: {hero.bio}')
#     else:
#         print(f'{nombre} no esta en la lista')


# def mostrar_anteriores_a(lista, anio):
#     for hero in lista:
#         if hero.year < anio:
#             print(f'{hero.name} - {hero.house}')


# def contar_por_casa(lista):
#     cantidades = {}
#     for hero in lista:
#         if hero.house in cantidades:
#             cantidades[hero.house] += 1
#         else:
#             cantidades[hero.house] = 1
#     return cantidades


# list_heroes = List()
# list_heroes.add_criterion('name', by_name)
# list_heroes.add_criterion('year', by_year)

# for hero in superheroes:
#     list_heroes.append(
#         Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
#     )

# print('a) eliminar Linterna Verde')
# deleted_value = list_heroes.delete_value("Green Lantern", 'name')
# print(f'valor eliminado: {deleted_value}')

# print('\nb) anio de aparicion de Wolverine')
# mostrar_anio(list_heroes, "Wolverine")

# print('\nc) cambiar la casa de Dr. Strange a Marvel')
# cambiar_casa(list_heroes, "Dr. Strange", "Marvel")
# mostrar_casa(list_heroes, "Dr. Strange")

# print('\nd) biografia con "traje" o "armadura"')
# list_heroes.filter_contain_on_bio(['traje', 'armadura'])

# print('\ne) aparecieron antes de 1963')
# mostrar_anteriores_a(list_heroes, 1963)

# print('\nf) casa de Capitana Marvel y Mujer Maravilla')
# mostrar_casa(list_heroes, "Capitana Marvel")
# mostrar_casa(list_heroes, "Mujer Maravilla")

# print('\ng) informacion de Flash y Star-Lord')
# mostrar_datos(list_heroes, "The Flash")
# print()
# mostrar_datos(list_heroes, "Star-Lord")

# print('\nh) nombres que comienzan con B, M o S')
# list_heroes.filter_start_with(('B', 'M', 'S'))

# print('\ni) cantidad de superheroes por casa')
# cantidades = contar_por_casa(list_heroes)
# for casa in cantidades:
#     print(f'{casa}: {cantidades[casa]}')

# Ejercicio Nº 15 de la guia de ejercicios de listas del libro.

from list_ import List


# Lista de lista: cada entrenador tiene el atributo 'pokemons', que es otra List.

class Pokemon():

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.name = nombre
        self.level = nivel
        self.type = tipo
        self.subtype = subtipo

    def __str__(self):
        return f"{self.name} - nivel {self.level} - {self.type}/{self.subtype}"


class Entrenador():

    def __init__(self, nombre, torneos, perdidas, ganadas):
        self.name = nombre
        self.tournaments = torneos
        self.lost = perdidas
        self.won = ganadas
        self.pokemons = List()      # sublista

    def __str__(self):
        return (f"{self.name} - torneos ganados: {self.tournaments} - "
                f"batallas ganadas: {self.won} - batallas perdidas: {self.lost}")


def by_trainer_name(item):
    return item.name

def by_tournaments(item):
    return item.tournaments

def by_pokemon_name(item):
    return item.name

def by_level(item):
    return item.level


# Datos de prueba
entrenadores_datos = [
    {
        "nombre": "Ash", "torneos": 5, "perdidas": 10, "ganadas": 90,
        "pokemons": [
            {"nombre": "Pikachu", "nivel": 50, "tipo": "electrico", "subtipo": "-"},
            {"nombre": "Charizard", "nivel": 60, "tipo": "fuego", "subtipo": "volador"},
            {"nombre": "Wingull", "nivel": 20, "tipo": "agua", "subtipo": "volador"},
            {"nombre": "Pikachu", "nivel": 30, "tipo": "electrico", "subtipo": "-"},
        ]
    },
    {
        "nombre": "Misty", "torneos": 2, "perdidas": 40, "ganadas": 60,
        "pokemons": [
            {"nombre": "Starmie", "nivel": 40, "tipo": "agua", "subtipo": "psiquico"},
            {"nombre": "Pelipper", "nivel": 35, "tipo": "agua", "subtipo": "volador"},
        ]
    },
    {
        "nombre": "Brock", "torneos": 4, "perdidas": 20, "ganadas": 80,
        "pokemons": [
            {"nombre": "Onix", "nivel": 45, "tipo": "roca", "subtipo": "tierra"},
            {"nombre": "Terrakion", "nivel": 55, "tipo": "roca", "subtipo": "lucha"},
            {"nombre": "Tyrantrum", "nivel": 50, "tipo": "roca", "subtipo": "dragon"},
        ]
    },
    {
        "nombre": "Gary", "torneos": 1, "perdidas": 30, "ganadas": 50,
        "pokemons": [
            {"nombre": "Blastoise", "nivel": 52, "tipo": "agua", "subtipo": "-"},
            {"nombre": "Exeggutor", "nivel": 48, "tipo": "planta", "subtipo": "psiquico"},
            {"nombre": "Ninetales", "nivel": 47, "tipo": "fuego", "subtipo": "planta"},
        ]
    },
]


# Funciones

# a. cantidad de Pokemons de un entrenador
def cantidad_pokemons(entrenadores, nombre):
    pos = entrenadores.search(nombre, 'trainer_name')
    if pos is not None:
        print(f'{nombre} tiene {entrenadores[pos].pokemons.size()} pokemons')
    else:
        print(f'{nombre} no esta en la lista')


# b. entrenadores que ganaron mas de tres torneos
def mas_de_tres_torneos(entrenadores):
    for entrenador in entrenadores:
        if entrenador.tournaments > 3:
            print(entrenador)


# c. Pokemon de mayor nivel del entrenador con mas torneos ganados
def pokemon_mayor_nivel_del_campeon(entrenadores):
    if entrenadores.size() == 0:
        print('no hay entrenadores')
        return

    campeon = entrenadores[0]
    for entrenador in entrenadores:
        if entrenador.tournaments > campeon.tournaments:
            campeon = entrenador

    if campeon.pokemons.size() == 0:
        print(f'{campeon.name} no tiene pokemons')
        return

    mayor = campeon.pokemons[0]
    for pokemon in campeon.pokemons:
        if pokemon.level > mayor.level:
            mayor = pokemon

    print(f'entrenador con mas torneos: {campeon.name} ({campeon.tournaments})')
    print(f'su pokemon de mayor nivel: {mayor}')


# d. todos los datos de un entrenador y sus Pokemons
def mostrar_entrenador(entrenadores, nombre):
    pos = entrenadores.search(nombre, 'trainer_name')
    if pos is not None:
        print(entrenadores[pos])
        entrenadores[pos].pokemons.show()
    else:
        print(f'{nombre} no esta en la lista')


# e. entrenadores con porcentaje de batallas ganadas mayor al 79 %
def porcentaje_mayor_a(entrenadores, porcentaje):
    for entrenador in entrenadores:
        total = entrenador.won + entrenador.lost
        if total > 0 and entrenador.won * 100 / total > porcentaje:
            print(f'{entrenador.name} - {entrenador.won * 100 / total:.1f} %')


# f. entrenadores con Pokemons tipo fuego/planta o agua/volador (tipo/subtipo)
def tipos_fuego_planta_o_agua_volador(entrenadores):
    for entrenador in entrenadores:
        cumple = False
        for pokemon in entrenador.pokemons:
            if pokemon.type == 'fuego' and pokemon.subtype == 'planta':
                cumple = True
            elif pokemon.type == 'agua' and pokemon.subtype == 'volador':
                cumple = True
        if cumple:
            print(entrenador)


# g. promedio de nivel de los Pokemons de un entrenador
def promedio_nivel(entrenadores, nombre):
    pos = entrenadores.search(nombre, 'trainer_name')
    if pos is None:
        print(f'{nombre} no esta en la lista')
    elif entrenadores[pos].pokemons.size() == 0:
        print(f'{nombre} no tiene pokemons')
    else:
        suma = 0
        for pokemon in entrenadores[pos].pokemons:
            suma += pokemon.level
        print(f'promedio de nivel de {nombre}: {suma / entrenadores[pos].pokemons.size():.1f}')


# h. cuantos entrenadores tienen un determinado Pokemon
def contar_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    cantidad = 0
    for entrenador in entrenadores:
        if entrenador.pokemons.search(nombre_pokemon, 'pokemon_name') is not None:
            cantidad += 1
    print(f'{cantidad} entrenadores tienen a {nombre_pokemon}')


# i. entrenadores que tienen Pokemons repetidos
def con_pokemons_repetidos(entrenadores):
    for entrenador in entrenadores:
        entrenador.pokemons.sort_by_criterion('pokemon_name')
        repetido = False
        for i in range(1, entrenador.pokemons.size()):
            if entrenador.pokemons[i].name == entrenador.pokemons[i - 1].name:
                repetido = True
        if repetido:
            print(entrenador)


# j. entrenadores que tengan alguno de los Pokemons indicados
def con_alguno_de(entrenadores, nombres_pokemon):
    for entrenador in entrenadores:
        tiene = False
        for nombre in nombres_pokemon:
            if entrenador.pokemons.search(nombre, 'pokemon_name') is not None:
                tiene = True
        if tiene:
            print(entrenador)


# k. determinar si el entrenador X tiene al Pokemon Y
def tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    pos = entrenadores.search(nombre_entrenador, 'trainer_name')
    if pos is None:
        print(f'{nombre_entrenador} no esta en la lista')
        return

    entrenador = entrenadores[pos]
    pos_pokemon = entrenador.pokemons.search(nombre_pokemon, 'pokemon_name')
    if pos_pokemon is not None:
        print(f'{nombre_entrenador} SI tiene a {nombre_pokemon}')
        print(entrenador)
        print(entrenador.pokemons[pos_pokemon])
    else:
        print(f'{nombre_entrenador} NO tiene a {nombre_pokemon}')



lista_entrenadores = List()
lista_entrenadores.add_criterion('trainer_name', by_trainer_name)
lista_entrenadores.add_criterion('tournaments', by_tournaments)
lista_entrenadores.add_criterion('pokemon_name', by_pokemon_name)
lista_entrenadores.add_criterion('level', by_level)

for datos in entrenadores_datos:
    entrenador = Entrenador(datos['nombre'], datos['torneos'], datos['perdidas'], datos['ganadas'])
    for p in datos['pokemons']:
        entrenador.pokemons.append(Pokemon(p['nombre'], p['nivel'], p['tipo'], p['subtipo']))
    lista_entrenadores.append(entrenador)

print('a) cantidad de pokemons de Ash')
cantidad_pokemons(lista_entrenadores, 'Ash')

print('\nb) entrenadores con mas de tres torneos')
mas_de_tres_torneos(lista_entrenadores)

print('\nc) pokemon de mayor nivel del entrenador con mas torneos')
pokemon_mayor_nivel_del_campeon(lista_entrenadores)

print('\nd) datos de Brock y sus pokemons')
mostrar_entrenador(lista_entrenadores, 'Brock')

print('\ne) porcentaje de batallas ganadas mayor al 79 %')
porcentaje_mayor_a(lista_entrenadores, 79)

print('\nf) pokemons fuego/planta o agua/volador')
tipos_fuego_planta_o_agua_volador(lista_entrenadores)

print('\ng) promedio de nivel de Ash')
promedio_nivel(lista_entrenadores, 'Ash')

print('\nh) cuantos entrenadores tienen a Pikachu')
contar_entrenadores_con_pokemon(lista_entrenadores, 'Pikachu')

print('\ni) entrenadores con pokemons repetidos')
con_pokemons_repetidos(lista_entrenadores)

print('\nj) entrenadores con Tyrantrum, Terrakion o Wingull')
con_alguno_de(lista_entrenadores, ('Tyrantrum', 'Terrakion', 'Wingull'))

print('\nk) Brock tiene a Onix?')
tiene_pokemon(lista_entrenadores, 'Brock', 'Onix')