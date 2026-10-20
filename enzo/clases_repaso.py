# CLASES 

class MiClase:

    def __init__(self, name: str, size: int = None):
        self.__name = name
        self.__size = size

    def saludar(self):
        print(self)
        print(f'hola, mi nombre es {self.__name}')

    def get_name(self):
        return self.__name

    def set_name(self, new_name:str):
        self.__name = new_name
    

f_1 = MiClase('Pepito')

f_2 = MiClase('Juancito')

f_3 = MiClase('Anita')

f_1.set_name('Sarasa')

#print(f_1.get_name())

# f_1.saludar()
# f_2.saludar()
# f_3.saludar()

# print(f_1 == f_2)
# print(f_1 == f_3)

# print(f_1)
# print(f_2)
# print(f_3)