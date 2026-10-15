# Encapsulamiento
# Mecanismo de proteccion de acceso
# a los atributos y metodos de una clase.

# Getter()
# Obtenedores de informacion

# Setter()
# Modificadores de informacion

"""
------------------------------------------
|               Mascota                  |
|----------------------------------------|
| - nombre: str                          |
| - edad: str                            |
| - especie: str                         |
| - raza: str                            |
| - peso: float                          |
| - sexo: str                            |
| - fallecido: bool                      |
|----------------------------------------|
| + obtenerNombre(): str                 |
| + obtenerEdad(): str                   |
| + obtenerEspecie(): str                |
| + obtenerRaza(): str                   |
| + obtenerPeso(): float                 |
| + obtenerSexo(): str                   |
| + obtenerFallecido(): bool             |
------------------------------------------
"""

class Mascota:
    def __init__(self, nombre: str, edad: str, especie: str, raza: str, peso: float, sexo: str, fallecido: bool):
        self.__nombre: str = nombre
        self.__edad: str = edad
        self.__especie: str = especie
        self.__raza: str = raza
        self.__peso: float = peso
        self.__sexo: str = sexo
        self.__fallecido: bool = fallecido

    def obtenerNombre(self) -> str: return self.__nombre
    def obtenerEdad(self) -> str: return self.__edad
    def obtenerEspecie(self) -> str: return self.__especie
    def obtenerRaza(self) -> str: return self.__raza
    def obtenerPeso(self) -> float: return self.__peso
    def obtenerSexo(self) -> str: return self.__sexo
    def obtenerFallecido(self) -> bool: return self.__fallecido

    def modificarPeso(self, nuevo_peso: float) -> None:
        if nuevo_peso <= 0: return print("Peso incorrecto, no puede ser menor o igual a 0.")
        else:
            self.__peso = nuevo_peso
        print("Nuevo peso establecido en la Mascota")    

    
