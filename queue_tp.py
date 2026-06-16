# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue
from stack_ import Stack

def eliminar_facebook(cola_notificaciones: Queue):
    for i in range(cola_notificaciones.size()):
        notificacion = cola_notificaciones.on_front()
        if notificacion.app == 'Facebook':
            cola_notificaciones.attention()
        else:
            cola_notificaciones.move_to_end()

def mostrar_twitter_python(cola_notificaciones: Queue):
    for i in range(cola_notificaciones.size()):
        notificacion = cola_notificaciones.on_front()
        if notificacion.app == 'Twitter' and 'Python' in notificacion.mensaje:
            print(f"Hora: {notificacion.hora} - Mensaje: {notificacion.mensaje}")
        cola_notificaciones.move_to_end()

def filtrar_por_horario(cola_notificaciones: Queue):
    pila_temporal = Stack()
    for i in range(cola_notificaciones.size()):
        notificacion = cola_notificaciones.on_front()
        if "11:43" <= notificacion.hora <= "15:57":
            pila_temporal.push(notificacion)
        cola_notificaciones.move_to_end()
        
    cantidad = pila_temporal.size()
    print(f"Cantidad de notificaciones en el rango: {cantidad}")


# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe
# y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-manoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

from queue_ import Queue

class PersonajeMCU:
    def __init__(self, nombre: str, heroe: str, genero: str):
        self.nombre = nombre
        self.heroe = heroe
        self.genero = genero  # "M" o "F"

def personaje_capitana_marvel(cola_personajes: Queue):
    for i in range(cola_personajes.size()):
        p = cola_personajes.on_front()
        if p.heroe == "Capitana Marvel":
            print(f"El personaje de Capitana Marvel es: {p.nombre}")
        cola_personajes.move_to_end()

def mostrar_superheroes_femeninos(cola_personajes: Queue):
    print("--- Superhéroes Femeninos ---")
    for i in range(cola_personajes.size()):
        p = cola_personajes.on_front()
        if p.genero == "F":
            print(p.heroe)
        cola_personajes.move_to_end()

def mostrar_personajes_masculinos(cola_personajes: Queue):
    print("--- Personajes Masculinos ---")
    for i in range(cola_personajes.size()):
        p = cola_personajes.on_front()
        if p.genero == "M":
            print(p.nombre)
        cola_personajes.move_to_end()

def heroe_scott_lang(cola_personajes: Queue):
    for i in range(cola_personajes.size()):
        p = cola_personajes.on_front()
        if p.nombre == "Scott Lang":
            print(f"El superhéroe de Scott Lang es: {p.heroe}")
        cola_personajes.move_to_end()

def mostrar_datos_con_s(cola_personajes: Queue):
    print("--- Personajes o Héroes que empiezan con S ---")
    for i in range(cola_personajes.size()):
        p = cola_personajes.on_front()
        if p.nombre[0] == "S" or p.heroe[0] == "S":
            print(f"Personaje: {p.nombre} | Héroe: {p.heroe} | Género: {p.genero}")
        cola_personajes.move_to_end()

def buscar_carol_danvers(cola_personajes: Queue):
    encontrado = False
    heroe_nombre = ""
    for i in range(cola_personajes.size()):
        p = cola_personajes.on_front()
        if p.nombre == "Carol Danvers":
            encontrado = True
            heroe_nombre = p.heroe
        cola_personajes.move_to_end()
        
    if encontrado:
        print(f"Carol Danvers está en la cola. Su héroe es: {heroe_nombre}")
    else:
        print("Carol Danvers no está en la cola.")

cola_mcu = Queue()

cola_mcu.arrive(PersonajeMCU("Tony Stark", "Iron Man", "M"))
cola_mcu.arrive(PersonajeMCU("Steve Rogers", "Capitán América", "M"))
cola_mcu.arrive(PersonajeMCU("Natasha Romanoff", "Black Widow", "F"))
cola_mcu.arrive(PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"))
cola_mcu.arrive(PersonajeMCU("Scott Lang", "Ant-Man", "M"))

personaje_capitana_marvel(cola_mcu)
print()
mostrar_superheroes_femeninos(cola_mcu)
print()
mostrar_personajes_masculinos(cola_mcu)
print()
heroe_scott_lang(cola_mcu)
print()
mostrar_datos_con_s(cola_mcu)
print()
buscar_carol_danvers(cola_mcu)