# Abstraccion
# La capacidad de reconocer las partes más
# importantes para un sistema informático. 

# Clase -> Plantilla
# Visibilidad Atributo: Tipo de dato
# Visibilidad Metodo(Argumentos): Tipo de dato que devuelve

# Definir una Mascota
# **** LOS NOMBRES DE LAS CLASES VAN EN SINGULAR
# ------> Mascota : OK
# ------> Mascotas : MALO
"""
------------------------------------------
|               Mascota                  |
|----------------------------------------|
| + nombre: str                          |
| + edad: str                            |
| + especie: str                         |
| + raza: str                            |
| + peso: float                          |
| + sexo: str                            |
| + fallecido: bool                      |
|----------------------------------------|
|                                        |
------------------------------------------
"""

class Mascota:
    def __init__(self, nombre: str, edad: str, especie: str, raza: str, peso: float, sexo: str, fallecido: bool):
        self.nombre: str = nombre
        self.edad: str = edad
        self.especie: str = especie
        self.raza: str = raza
        self.peso: float = peso
        self.sexo: str = sexo
        self.fallecido: bool = fallecido
