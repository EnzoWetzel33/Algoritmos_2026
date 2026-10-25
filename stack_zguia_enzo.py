# # 1. Determinar el número de ocurrencias de un determinado elemento en una pila.

# from random import randint

# from stack_ import Stack

# pila = Stack()

# for i in range(10):
#     pila.push(randint(1, 10))

# print()
# pila.show()
# print()

# buscado = int(input('Ingrese un numero para contar ocurrencias: '))
# contador = 0

# pila_aux = Stack()                      #Creamos una pila auxiliar para no perder los elementos de la pila original

# while pila.size() > 0:
#     valor = pila.pop()
#     if valor == buscado:
#         contador += 1
#     pila_aux.push(valor)                #Guardamos los elementos en la pila auxiliar 

# while pila_aux.size() > 0:              #Devolvemos los elementos a la pila original
#     pila.push(pila_aux.pop())           #La pila original queda igual que al inicio, pero ahora tenemos el contador de ocurrencias del elemento buscado.


# print(f'El numero {buscado} aparece {contador} veces en la pila.')      #Comprobado, funciona y es correcto.


# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.

# from random import randint

# from stack_ import Stack

# pila = Stack()

# for i in range(10):
#     pila.push(randint(1, 10))

# print()
# pila.show()
# print()

# pila_aux = Stack()                      #Creamos una pila auxiliar para no perder los elementos de la pila original

# while pila.size() > 0:
#     valor = pila.pop()
#     if valor % 2 == 0:
#         pila_aux.push(valor)

# while pila_aux.size() > 0:
#     pila.push(pila_aux.pop())

# print()
# pila.show()
# print()

# 3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from random import randint

from stack_ import Stack

pila = Stack()

for i in range(10):
    pila.push(randint(1, 10))

print()
pila.show()
print()

buscado = int(input('Ingrese el numero a reemplazar : '))
nuevo = int(input('Ingrese el nuevo numero : '))

pila_aux = Stack()

while pila.size() > 0:
    valor = pila.pop()
    if valor == buscado:
        pila_aux.push(nuevo)
    else:
        pila_aux.push(valor)

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print ('Pila modificada')
pila.show()