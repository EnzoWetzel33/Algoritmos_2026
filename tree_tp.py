# Ejercicio Nº 5 de la guia de ejercicios de arboles del libro.

# from super_heroes_data import superheroes
# from tree_ import BinaryTree


# # Funciones

# def listar_villanos(arbol):
#     # inorden: recorre en orden alfabetico y muestra solo los villanos
#     def __listar_villanos(root):
#         if root is not None:
#             __listar_villanos(root.left)
#             if root.other_values['is_villain']:
#                 print(root.value)
#             __listar_villanos(root.right)

#     __listar_villanos(arbol.root)


# def modificar_nombre(arbol, nombre_actual, nombre_nuevo):
#     node = arbol.search(nombre_actual)
#     if node is not None:
#         valor, otros_valores = arbol.delete_node(node.value)
#         otros_valores['name'] = nombre_nuevo
#         arbol.insert_node(nombre_nuevo, otros_valores)
#     else:
#         print(f'{nombre_actual} no esta en el arbol')


# def contar_nodos(arbol):
#     def __contar_nodos(root):
#         if root is None:
#             return 0
#         return __contar_nodos(root.left) + 1 + __contar_nodos(root.right)

#     return __contar_nodos(arbol.root)


# def generar_bosque(arbol):
#     # Aca hice 2 arboles, uno para heroes y otro para villanos, y los lleno con los nodos del arbol base
#     arbol_heroes = BinaryTree()
#     arbol_villanos = BinaryTree()

#     def __cargar(root):
#         if root is not None:
#             __cargar(root.left)
#             if root.other_values['is_villain']:
#                 arbol_villanos.insert_node(root.value, root.other_values)
#             else:
#                 arbol_heroes.insert_node(root.value, root.other_values)
#             __cargar(root.right)

#     __cargar(arbol.root)
#     return arbol_heroes, arbol_villanos


# def listar_inorden(arbol):
#     def __listar(root):
#         if root is not None:
#             __listar(root.left)
#             print(root.value)
#             __listar(root.right)

#     __listar(arbol.root)


# # a. se carga el arbol con el nombre y el campo is_villain en cada nodo
# arbol_mcu = BinaryTree()
# for personaje in superheroes:
#     arbol_mcu.insert_node(personaje['name'], other_value=personaje)

# print('b) villanos ordenados alfabeticamente')
# listar_villanos(arbol_mcu)

# print('\nc) superheroes que empiezan con C')
# arbol_mcu.inorden_hero_star_with('C')

# print(f'\nd) cantidad de superheroes: {arbol_mcu.count_heroes()}')

# print('\ne) busqueda por proximidad de Doctor Strange')
# arbol_mcu.proxy_search('stran')
# modificar_nombre(arbol_mcu, 'Dr Strannnnnge', 'Doctor Strange')
# print('despues de modificar:')
# arbol_mcu.proxy_search('strange')

# print('\nf) superheroes ordenados de manera descendente')
# arbol_mcu.postorden_hero()

# print('\ng) bosque: un arbol de superheroes y otro de villanos')
# arbol_heroes, arbol_villanos = generar_bosque(arbol_mcu)

# print(f'I. nodos del arbol de superheroes: {contar_nodos(arbol_heroes)}')
# print(f'   nodos del arbol de villanos: {contar_nodos(arbol_villanos)}')

# print('\nII. superheroes (orden alfabetico)')
# listar_inorden(arbol_heroes)
# print('\nII. villanos (orden alfabetico)')
# listar_inorden(arbol_villanos)

# Ejercicio Nº 23 de la guia de ejercicios de arboles del libro.

from tree_ import BinaryTree


# En cada nodo: value = nombre de la criatura, other_values = diccionario con
#   'defeated_by': quien la derroto (None si no fue derrotada)
#   'description': breve descripcion (vacia hasta que se carga)
#   'captured_by': quien la capturo (None si nadie)

# (criatura, derrotado por) segun la tabla del libro; None equivale a "-"
criaturas = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"), ("Dino", None),
    ("Pefredo", None), ("Enio", None), ("Escila", None), ("Caribdis", None),
    ("Euríale", None), ("Esteno", None), ("Medusa", "Perseo"), ("Ladón", "Heracles"),
    ("Águila del Cáucaso", None), ("Quimera", "Belerofonte"), ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"), ("Esfinge", "Edipo"), ("Dragón de la Cólquida", None),
    ("Cerbero", None), ("Cerda de Cromión", "Teseo"), ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"), ("Jabalí de Calidón", "Atalanta"), ("Carcinos", None),
    ("Gerión", "Heracles"), ("Cloto", None), ("Láquesis", None), ("Átropos", None),
    ("Minotauro de Creta", "Teseo"), ("Harpías", None), ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None), ("Talos", "Medea"), ("Sirenas", None),
    ("Pitón", "Apolo"), ("Cierva de Cerinea", None), ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]


# Funciones

def listar_si(arbol, condicion):
    def __listar_si(root):
        if root is not None:
            __listar_si(root.left)
            if condicion(root):
                print(root.value)
            __listar_si(root.right)

    __listar_si(arbol.root)


# a. listado inorden de las criaturas y quienes las derrotaron
def listar_inorden(arbol):
    def __listar(root):
        if root is not None:
            __listar(root.left)
            derrotado_por = root.other_values['defeated_by']
            print(f"{root.value} - derrotada por: {derrotado_por if derrotado_por else 'nadie'}")
            __listar(root.right)

    __listar(arbol.root)


# b. cargar una breve descripcion de una criatura
def cargar_descripcion(arbol, nombre, descripcion):
    node = arbol.search(nombre)
    if node is not None:
        node.other_values['description'] = descripcion
    else:
        print(f'{nombre} no esta en el arbol')


# c. mostrar toda la informacion de una criatura
def mostrar_info(arbol, nombre):
    node = arbol.search(nombre)
    if node is not None:
        print(f'nombre: {node.value}')
        print(f"derrotada por: {node.other_values['defeated_by']}")
        print(f"descripcion: {node.other_values['description']}")
        print(f"capturada por: {node.other_values['captured_by']}")
    else:
        print(f'{nombre} no esta en el arbol')


# d. los 3 heroes o dioses que derrotaron mas criaturas
def contar_derrotas(arbol):
    conteo = {}

    def __contar(root):
        if root is not None:
            __contar(root.left)
            heroe = root.other_values['defeated_by']
            if heroe is not None:
                if heroe in conteo:
                    conteo[heroe] += 1
                else:
                    conteo[heroe] = 1
            __contar(root.right)

    __contar(arbol.root)
    return conteo


def top_tres_derrotas(arbol):
    conteo = contar_derrotas(arbol)
    for i in range(3):
        mayor = None
        for heroe in conteo:
            if mayor is None or conteo[heroe] > conteo[mayor]:
                mayor = heroe
        if mayor is not None:
            print(f'{mayor}: {conteo[mayor]} criaturas derrotadas')
            del conteo[mayor]


# condiciones para listar_si (e, f y n)
def derrotada_por_heracles(node):
    return node.other_values['defeated_by'] == 'Heracles'

def no_derrotada(node):
    return node.other_values['defeated_by'] is None

def capturada_por_heracles(node):
    return node.other_values['captured_by'] == 'Heracles'


# g y h. registrar quien capturo a una criatura
def capturar(arbol, nombre, heroe):
    node = arbol.search(nombre)
    if node is not None:
        node.other_values['captured_by'] = heroe
    else:
        print(f'{nombre} no esta en el arbol')


# k. modificar quien derroto a una criatura
def modificar_derrotada_por(arbol, nombre, heroe, descripcion):
    node = arbol.search(nombre)
    if node is not None:
        node.other_values['defeated_by'] = heroe
        node.other_values['description'] = descripcion
    else:
        print(f'{nombre} no esta en el arbol')


# l. cambiar el nombre (es la clave del arbol: se elimina y se vuelve a insertar)
def modificar_nombre(arbol, nombre_actual, nombre_nuevo):
    node = arbol.search(nombre_actual)
    if node is not None:
        valor, otros_valores = arbol.delete_node(node.value)
        arbol.insert_node(nombre_nuevo, otros_valores)
    else:
        print(f'{nombre_actual} no esta en el arbol')


arbol_criaturas = BinaryTree()
for nombre, derrotado_por in criaturas:
    arbol_criaturas.insert_node(
        nombre,
        {'defeated_by': derrotado_por, 'description': '', 'captured_by': None}
    )

print('a) listado inorden de criaturas y quienes las derrotaron')
listar_inorden(arbol_criaturas)

print('\nb) cargar descripciones (ejemplos)')
cargar_descripcion(arbol_criaturas, 'Talos', 'Gigante de bronce que custodiaba la isla de Creta.')
cargar_descripcion(arbol_criaturas, 'Cerbero', 'Perro de tres cabezas que cuida la entrada al Hades.')
cargar_descripcion(arbol_criaturas, 'Aves del Estínfalo', 'Aves de plumas metalicas que atacaban a las personas.')

print('\nc) informacion de Talos')
mostrar_info(arbol_criaturas, 'Talos')

print('\nd) los 3 heroes o dioses que derrotaron mas criaturas')
top_tres_derrotas(arbol_criaturas)

print('\ne) criaturas derrotadas por Heracles')
listar_si(arbol_criaturas, derrotada_por_heracles)

print('\nf) criaturas que no han sido derrotadas')
listar_si(arbol_criaturas, no_derrotada)

print('\ng y h) Heracles captura a Cerbero, Toro de Creta, Cierva de Cerinea y Jabali de Erimanto')
for nombre in ('Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto'):
    capturar(arbol_criaturas, nombre, 'Heracles')
mostrar_info(arbol_criaturas, 'Cerbero')

print('\ni) busqueda por coincidencia ("cer")')
arbol_criaturas.proxy_search('cer')

print('\nj) eliminar al Basilisco y a las Sirenas')
print(arbol_criaturas.delete_node('Basilisco'))
print(arbol_criaturas.delete_node('Sirenas'))

print('\nk) Heracles derroto a varias Aves del Estinfalo')
modificar_derrotada_por(arbol_criaturas, 'Aves del Estínfalo', 'Heracles',
                        'Aves de plumas metalicas que atacaban a las personas. Heracles derroto a varias.')
mostrar_info(arbol_criaturas, 'Aves del Estínfalo')

print('\nl) Ladon pasa a llamarse Dragon Ladon')
modificar_nombre(arbol_criaturas, 'Ladón', 'Dragón Ladón')
mostrar_info(arbol_criaturas, 'Dragón Ladón')

print('\nm) listado por nivel')
arbol_criaturas.by_level()

print('\nn) criaturas capturadas por Heracles')
listar_si(arbol_criaturas, capturada_por_heracles)