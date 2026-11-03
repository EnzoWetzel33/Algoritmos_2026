# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos,
#              debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de
#              manera eficiente a los datos contemplando lo siguiente:
#               los índices de cada uno de los árboles deben ser nombre, número y tipo;
#               mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último,
#               la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#               mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
#               realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
#               mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
#               mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
#               determinar cuantos Pokémons tienen megaevolucion.
#               determinar cuantos Pokémons tiene forma gigamax.
#               cargue al menos 100 Pokémons.

import json
from random import choice
from tree_ import BinaryTree


def mostrar_pokemon(pokemon):
    print(f"Número: {pokemon['numero']} | Nombre: {pokemon['nombre']}")
    print(f"  Tipos: {', '.join(pokemon['tipos'])}")
    print(f"  Debilidades: {', '.join(pokemon['debilidades'])}")
    print(f"  Mega evolución: {pokemon['mega']} | Gigamax: {pokemon['gigamax']}")


def buscar_por_proximidad(arbol, texto):

    def __buscar_por_proximidad(root, texto):
        if root.left is not None:
            __buscar_por_proximidad(root.left, texto)
        if texto in root.value.lower():
            mostrar_pokemon(root.other_values)
        if root.right is not None:
            __buscar_por_proximidad(root.right, texto)

    if arbol.root is not None:
        __buscar_por_proximidad(arbol.root, texto.lower())


def listar_numero_nombre(arbol):

    def __listar(root):
        if root.left is not None:
            __listar(root.left)
        pokemon = root.other_values
        print(f"{pokemon['numero']} - {pokemon['nombre']}")
        if root.right is not None:
            __listar(root.right)

    if arbol.root is not None:
        __listar(arbol.root)


def mostrar_debiles_frente_a(arbol, tipos):

    def __mostrar_debiles(root, tipos):
        if root.left is not None:
            __mostrar_debiles(root.left, tipos)
        es_debil = False
        for tipo in tipos:
            if tipo in root.other_values['debilidades']:
                es_debil = True
        if es_debil:
            print(root.value)
        if root.right is not None:
            __mostrar_debiles(root.right, tipos)

    if arbol.root is not None:
        __mostrar_debiles(arbol.root, tipos)


def contar_por_tipo(arbol):

    def __contar_por_tipo(root):
        if root.left is not None:
            __contar_por_tipo(root.left)
        print(f"{root.value}: {len(root.other_values)}")
        if root.right is not None:
            __contar_por_tipo(root.right)

    if arbol.root is not None:
        __contar_por_tipo(arbol.root)


def contar_verdaderos(arbol, campo):

    def __contar_verdaderos(root):
        count = 0
        if root is not None:
            count += __contar_verdaderos(root.left)
            if root.other_values[campo]:
                count += 1
            count += __contar_verdaderos(root.right)
        return count

    return __contar_verdaderos(arbol.root)


CANTIDAD = 100  # cantidad de pokemons a cargar en los arboles

# cargar el pokedex
with open('pokedex.json', encoding='utf-8') as archivo:
    pokedex = json.load(archivo)

# los tres que pide el enunciado se cargan siempre, el resto al azar
cargados = []
for pokemon in pokedex:
    if pokemon['nombre'] in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
        cargados.append(pokemon)

while len(cargados) < CANTIDAD:
    pokemon = choice(pokedex)
    if pokemon not in cargados:
        cargados.append(pokemon)

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in cargados:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)

    for tipo in pokemon['tipos']:
        nodo = arbol_tipo.search(tipo)
        if nodo is None:
            arbol_tipo.insert_node(tipo, [pokemon])
        else:
            nodo.other_values.append(pokemon)

print(f"Pokémons cargados: {len(cargados)}")


print("\n--- Búsqueda por número ---")
numero_buscado = int(input("Ingrese el número de Pokémon a buscar: "))
nodo = arbol_numero.search(numero_buscado)
if nodo is not None:
    mostrar_pokemon(nodo.other_values)
else:
    print("No se encontró un Pokémon con ese número")


print("\n--- Búsqueda por proximidad de nombre ---")
nombre_buscado = input("Ingrese el nombre (o parte del nombre) a buscar: ")
buscar_por_proximidad(arbol_nombre, nombre_buscado)


print("\n--- Nombres de Pokémons por tipo ---")
for tipo in ['Fantasma', 'Fuego', 'Acero', 'Eléctrico']:
    print(f"\nTipo {tipo}:")
    nodo = arbol_tipo.search(tipo)
    if nodo is not None:
        for pokemon in nodo.other_values:
            print(pokemon['nombre'])


print("\n--- Listado ascendente por número ---")
listar_numero_nombre(arbol_numero)

print("\n--- Listado ascendente por nombre ---")
listar_numero_nombre(arbol_nombre)

print("\n--- Listado por nivel por nombre ---")
arbol_nombre.by_level()


print("\n--- Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum ---")
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    nodo = arbol_nombre.search(nombre)
    if nodo is not None:
        tipos = nodo.other_values['tipos']
        print(f"\nDébiles frente a {nombre} (tipos: {', '.join(tipos)}):")
        mostrar_debiles_frente_a(arbol_nombre, tipos)


print("\n--- Cantidad de Pokémons por tipo ---")
contar_por_tipo(arbol_tipo)


print("\n--- Mega evolución y Gigamax ---")
print(f"Pokémons con megaevolución: {contar_verdaderos(arbol_nombre, 'mega')}")
print(f"Pokémons con forma gigamax: {contar_verdaderos(arbol_nombre, 'gigamax')}");


# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
#     Cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
#     Hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
#     Determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
#     Cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
#     Calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
#     Indicar qué personajes aparecieron en los nueve episodios de la saga.

# from graph import Graph
 
# def mostrar_arbol_expansion(grafo, origen):
#     min_tree = grafo.kruskal(origen)
#     peso_total = 0
#     for edge in min_tree.split(';'):
#         origin, destination, weight = edge.split('|')
#         print(f'origin {origin} destination {destination} episodios {weight}')
#         peso_total += int(weight)
#     print(f'peso total: {peso_total}')
 
# def camino_mas_corto(grafo, origen, destino):
#     if grafo.exist_path(origen, destino):
#         paths = grafo.dijkstra(origen)
 
#         buscado = destino
#         peso_total = None
#         camino_completo = []
 
#         while paths.size() > 0:
#             value = paths.pop()
#             if value[0] == buscado:
#                 if peso_total is None:
#                     peso_total = value[1]
#                 camino_completo.append(value[0])
#                 buscado = value[2]
#         camino_completo.reverse()
#         print(f'el camino mas corto de {origen} a {destino} es: {" -> ".join(camino_completo)} con un costo de {peso_total}')
#     else:
#         print(f'no existe camino de {origen} a {destino}')
 
 
# g = Graph(is_dir=False)
 
# g.add_vertex('Luke Skywalker')
# g.add_vertex('Darth Vader')
# g.add_vertex('Yoda')
# g.add_vertex('Boba Fett')
# g.add_vertex('C-3PO')
# g.add_vertex('Leia')
# g.add_vertex('Rey')
# g.add_vertex('Kylo Ren')
# g.add_vertex('Chewbacca')
# g.add_vertex('Han Solo')
# g.add_vertex('R2-D2')
# g.add_vertex('BB-8')
# g.add_edge(4, 'Luke Skywalker', 'Darth Vader')
# g.add_edge(4, 'Luke Skywalker', 'Yoda')
# g.add_edge(2, 'Luke Skywalker', 'Boba Fett')
# g.add_edge(7, 'Luke Skywalker', 'C-3PO')
# g.add_edge(7, 'Luke Skywalker', 'Leia')
# g.add_edge(3, 'Luke Skywalker', 'Rey')
# g.add_edge(3, 'Luke Skywalker', 'Kylo Ren')
# g.add_edge(7, 'Luke Skywalker', 'Chewbacca')
# g.add_edge(5, 'Luke Skywalker', 'Han Solo')
# g.add_edge(7, 'Luke Skywalker', 'R2-D2')
# g.add_edge(3, 'Luke Skywalker', 'BB-8')
# g.add_edge(3, 'Darth Vader', 'Yoda')
# g.add_edge(2, 'Darth Vader', 'Boba Fett')
# g.add_edge(4, 'Darth Vader', 'C-3PO')
# g.add_edge(4, 'Darth Vader', 'Leia')
# g.add_edge(4, 'Darth Vader', 'Chewbacca')
# g.add_edge(3, 'Darth Vader', 'Han Solo')
# g.add_edge(4, 'Darth Vader', 'R2-D2')
# g.add_edge(3, 'Yoda', 'Boba Fett')
# g.add_edge(6, 'Yoda', 'C-3PO')
# g.add_edge(4, 'Yoda', 'Leia')
# g.add_edge(1, 'Yoda', 'Rey')
# g.add_edge(1, 'Yoda', 'Kylo Ren')
# g.add_edge(4, 'Yoda', 'Chewbacca')
# g.add_edge(2, 'Yoda', 'Han Solo')
# g.add_edge(6, 'Yoda', 'R2-D2')
# g.add_edge(1, 'Yoda', 'BB-8')
# g.add_edge(3, 'Boba Fett', 'C-3PO')
# g.add_edge(2, 'Boba Fett', 'Leia')
# g.add_edge(2, 'Boba Fett', 'Chewbacca')
# g.add_edge(2, 'Boba Fett', 'Han Solo')
# g.add_edge(3, 'Boba Fett', 'R2-D2')
# g.add_edge(7, 'C-3PO', 'Leia')
# g.add_edge(3, 'C-3PO', 'Rey')
# g.add_edge(3, 'C-3PO', 'Kylo Ren')
# g.add_edge(7, 'C-3PO', 'Chewbacca')
# g.add_edge(5, 'C-3PO', 'Han Solo')
# g.add_edge(9, 'C-3PO', 'R2-D2')
# g.add_edge(3, 'C-3PO', 'BB-8')
# g.add_edge(3, 'Leia', 'Rey')
# g.add_edge(3, 'Leia', 'Kylo Ren')
# g.add_edge(7, 'Leia', 'Chewbacca')
# g.add_edge(5, 'Leia', 'Han Solo')
# g.add_edge(7, 'Leia', 'R2-D2')
# g.add_edge(3, 'Leia', 'BB-8')
# g.add_edge(3, 'Rey', 'Kylo Ren')
# g.add_edge(3, 'Rey', 'Chewbacca')
# g.add_edge(2, 'Rey', 'Han Solo')
# g.add_edge(3, 'Rey', 'R2-D2')
# g.add_edge(3, 'Rey', 'BB-8')
# g.add_edge(3, 'Kylo Ren', 'Chewbacca')
# g.add_edge(2, 'Kylo Ren', 'Han Solo')
# g.add_edge(3, 'Kylo Ren', 'R2-D2')
# g.add_edge(3, 'Kylo Ren', 'BB-8')
# g.add_edge(5, 'Chewbacca', 'Han Solo')
# g.add_edge(7, 'Chewbacca', 'R2-D2')
# g.add_edge(3, 'Chewbacca', 'BB-8')
# g.add_edge(5, 'Han Solo', 'R2-D2')
# g.add_edge(2, 'Han Solo', 'BB-8')
# g.add_edge(3, 'R2-D2', 'BB-8')
 
 
# print('--- Árbol de expansión mínimo ---')
# for personaje in ['C-3PO', 'Yoda', 'Leia']:
#     print(f'\ndesde {personaje}:')
#     mostrar_arbol_expansion(g, personaje)
 
 
# print('\n--- Máximo de episodios compartidos entre dos personajes ---')
# maximo = 0
# for vertex in g:
#     for edge in vertex.edges:
#         if edge.weight > maximo:
#             maximo = edge.weight
# print(f'el número máximo de episodios compartidos es: {maximo}')
# for vertex in g:
#     for edge in vertex.edges:
#         if edge.weight == maximo and vertex.value < edge.destination:
#             print(f'{vertex.value} - {edge.destination}')
 
 
# print('\n--- Camino más corto ---')
# camino_mas_corto(g, 'C-3PO', 'R2-D2')
# camino_mas_corto(g, 'Yoda', 'Darth Vader')
 
 
# print('\n--- Personajes que aparecieron en los nueve episodios ---')
# cantidad_episodios = 9
# for vertex in g:
#     aparece_en_todos = False
#     for edge in vertex.edges:
#         if edge.weight == cantidad_episodios:
#             aparece_en_todos = True
#     if aparece_en_todos:
#         print(vertex.value)