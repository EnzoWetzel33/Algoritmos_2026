# Crear una clase para representar un Libro de una biblioteca

class Libro:

    def __init__(self,nombre:str,autor:str,paginas:int):
        self.__nombre = nombre
        self.__autor = autor
        self.__paginas = paginas
        self.__prestado = False

    def prestamo (self):
        if not self.__prestado:
            self.__prestado = True
        
    def devolucion (self):
        self.__prestado = False

    def get_prestado (self):
        return self.__prestado
    
    def __str__(self):              #Funcion exclusiva de python para mostrar toda la descripcion de la variable
        return f"Libro: {self.__nombre} - Autor: {self.__autor} - Paginas: {self.__paginas}"

libro1 = Libro('Harry Potter','Tomas C.',50)

libro2 = Libro('Don Quijote','Julio C.',150)

libro3 = Libro('Breaking Bad','Ted C.',100)

print(libro1.get_prestado())

libro1.prestamo()

print(libro1.get_prestado())

libro1.devolucion()

print(libro1.get_prestado())

print(libro1)