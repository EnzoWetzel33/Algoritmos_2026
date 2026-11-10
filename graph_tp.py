# Ejercicio Nº5 de la guia de ejercicios de grafos.

# from graph import Graph

# red = Graph(is_dir=False)

# # a. nombre del equipo y su tipo
# equipos = [
#     ('Manjaro', 'pc'), ('Parrot', 'pc'), ('Fedora', 'pc'), ('Ubuntu', 'pc'), ('Mint', 'pc'),
#     ('Red Hat', 'notebook'), ('Debian', 'notebook'), ('Arch', 'notebook'),
#     ('Guaraní', 'servidor'), ('MongoDB', 'servidor'),
#     ('Router 1', 'router'), ('Router 2', 'router'), ('Router 3', 'router'),
#     ('Switch 1', 'switch'), ('Switch 2', 'switch'),
#     ('Impresora', 'impresora'),
# ]

# # (peso, equipo 1, equipo 2)
# conexiones = [
#     (25, 'Red Hat', 'Router 2'),
#     (9, 'Guaraní', 'Router 2'),
#     (50, 'Router 2', 'Router 3'),
#     (37, 'Router 2', 'Router 1'),
#     (43, 'Router 3', 'Router 1'),
#     (61, 'Router 3', 'Switch 2'),
#     (40, 'Manjaro', 'Switch 2'),
#     (12, 'Parrot', 'Switch 2'),
#     (5, 'MongoDB', 'Switch 2'),
#     (3, 'Fedora', 'Switch 2'),
#     (56, 'Arch', 'Switch 2'),
#     (17, 'Debian', 'Switch 1'),
#     (18, 'Ubuntu', 'Switch 1'),
#     (22, 'Impresora', 'Switch 1'),
#     (80, 'Mint', 'Switch 1'),
#     (29, 'Switch 1', 'Router 1'),
# ]

# for nombre, tipo in equipos:
#     red.add_vertex(nombre, tipo)

# for peso, origen, destino in conexiones:
#     red.add_edge(peso, origen, destino)


# # Funciones

# def nombres_por_tipo(grafo, tipo):
#     nombres = []
#     for vertex in grafo:
#         if vertex.other_values == tipo:
#             nombres.append(vertex.value)
#     return nombres


# def barridos_desde(grafo, origenes):
#     for origen in origenes:
#         print(f'\n--- en profundidad desde {origen} ---')
#         grafo.deep_show(origen)
#         print(f'--- en amplitud desde {origen} ---')
#         grafo.amplitude_show(origen)


# def camino_mas_corto(grafo, origen, destino):
#     # use dijkstra: la pila queda con [vertice, costo, vertice anterior]
#     if not grafo.exist_path(origen, destino):
#         return None, None

#     paths = grafo.dijkstra(origen)
#     buscado = destino
#     costo_total = None
#     camino = []
#     while paths.size() > 0:
#         value = paths.pop()
#         if value[0] == buscado:
#             if costo_total is None:
#                 costo_total = value[1]
#             camino.append(value[0])
#             buscado = value[2]
#     camino.reverse()
#     return camino, costo_total


# def mostrar_camino(grafo, origen, destino):
#     camino, costo = camino_mas_corto(grafo, origen, destino)
#     if camino is None:
#         print(f'no hay camino de {origen} a {destino}')
#     else:
#         print(f'{" -> ".join(camino)} (costo {costo})')


# def arbol_expansion_minima(grafo, origen):
#     arbol = grafo.kruskal(origen)
#     total = 0
#     for arista in arbol.split(';'):
#         a, b, peso = arista.split('|')
#         print(f'{a} - {b}: {peso}')
#         total += int(peso)
#     print(f'peso total: {total}')


# def origen_mas_cercano(grafo, origenes, destino):
#     mejor = None
#     for origen in origenes:
#         camino, costo = camino_mas_corto(grafo, origen, destino)
#         if costo is not None and (mejor is None or costo < mejor[2]):
#             mejor = (origen, camino, costo)
#     return mejor


# def computadoras_del_switch(grafo, nombre_switch):
#     # equipos conectados directamente al switch que son pc o notebook
#     pos = grafo.search(nombre_switch, 'value')
#     computadoras = []
#     for edge in grafo[pos].edges:
#         pos_vecino = grafo.search(edge.destination, 'value')
#         if grafo[pos_vecino].other_values in ('pc', 'notebook'):
#             computadoras.append(edge.destination)
#     return computadoras


# print('b) barrido en profundidad y amplitud desde las notebook')
# barridos_desde(red, ['Red Hat', 'Debian', 'Arch'])

# print('\nc) camino mas corto hasta la impresora')
# for origen in ('Manjaro', 'Red Hat', 'Fedora'):
#     mostrar_camino(red, origen, 'Impresora')

# print('\nd) arbol de expansion minima')
# arbol_expansion_minima(red, 'Red Hat')

# print('\ne) pc (no notebook) con el camino mas corto a Guaraní')
# mejor = origen_mas_cercano(red, nombres_por_tipo(red, 'pc'), 'Guaraní')
# print(f'{mejor[0]}: {" -> ".join(mejor[1])} (costo {mejor[2]})')

# print('\nf) computadora del Switch 1 con el camino mas corto a MongoDB')
# mejor = origen_mas_cercano(red, computadoras_del_switch(red, 'Switch 1'), 'MongoDB')
# print(f'{mejor[0]}: {" -> ".join(mejor[1])} (costo {mejor[2]})')

# print('\ng) la impresora pasa a conectarse al Router 2 y se repite el punto b')
# red.delete_edge('Impresora', 'Switch 1')
# red.add_edge(22, 'Impresora', 'Router 2') 
# barridos_desde(red, ['Red Hat', 'Debian', 'Arch'])

# Ejercicio Nº14 de la guia de ejercicios de grafos.

from graph import Graph


# Grafo NO dirigido

casa = Graph(is_dir=False)

# a. ambientes
ambientes = [
    'cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
    'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio',
]

for ambiente in ambientes:
    casa.add_vertex(ambiente)

# b. (metros, ambiente 1, ambiente 2)
# Invente los datos: cada ambiente tiene al menos 3 aristas y 'sala de estar' y 'patio' tienen 5

distancias = [
    (4, 'sala de estar', 'comedor'),
    (6, 'sala de estar', 'cocina'),
    (9, 'sala de estar', 'habitación 1'),
    (5, 'sala de estar', 'baño 1'),
    (9, 'sala de estar', 'terraza'),
    (5, 'patio', 'terraza'),
    (7, 'patio', 'quincho'),
    (8, 'patio', 'cochera'),
    (10, 'patio', 'cocina'),
    (12, 'patio', 'comedor'),
    (3, 'cocina', 'comedor'),
    (3, 'habitación 1', 'baño 1'),
    (6, 'habitación 1', 'habitación 2'),
    (3, 'habitación 2', 'baño 2'),
    (7, 'habitación 2', 'baño 1'),
    (5, 'baño 2', 'habitación 1'),
    (4, 'baño 2', 'baño 1'),
    (6, 'quincho', 'cochera'),
    (8, 'quincho', 'terraza'),
    (9, 'cochera', 'cocina'),
]

for metros, origen, destino in distancias:
    casa.add_edge(metros, origen, destino)


# Funciones

def mostrar_cantidad_de_aristas(grafo):
    for vertex in grafo:
        print(f'{vertex.value}: {len(vertex.edges)} aristas')


def arbol_expansion_minima(grafo, origen):
    # kruskal devuelve un texto con las aristas 'a|b|peso' separadas por ;
    arbol = grafo.kruskal(origen)
    total = 0
    for arista in arbol.split(';'):
        a, b, metros = arista.split('|')
        print(f'{a} - {b}: {metros} m')
        total += int(metros)
    return total


def camino_mas_corto(grafo, origen, destino):
    # use dijkstra: la pila queda con [vertice, costo, vertice anterior]
    if not grafo.exist_path(origen, destino):
        return None, None

    paths = grafo.dijkstra(origen)
    buscado = destino
    costo_total = None
    camino = []
    while paths.size() > 0:
        value = paths.pop()
        if value[0] == buscado:
            if costo_total is None:
                costo_total = value[1]
            camino.append(value[0])
            buscado = value[2]
    camino.reverse()
    return camino, costo_total


print('b) cantidad de aristas de cada ambiente')
mostrar_cantidad_de_aristas(casa)

print('\nc) arbol de expansion minima')
metros_cable = arbol_expansion_minima(casa, 'cocina')
print(f'metros de cable necesarios para conectar todos los ambientes: {metros_cable} m')

print('\nd) camino mas corto de habitación 1 a sala de estar')
camino, metros = camino_mas_corto(casa, 'habitación 1', 'sala de estar')
if camino is not None:
    print(' -> '.join(camino))
    print(f'metros de cable de red entre el router y el Smart TV: {metros} m')
else:
    print('no hay camino')