# Abstraccion
# La aptidud de identificar los atributos
# más importantes para el sistema informatico.

# Definir Mascota

"""
Mascota
-------
+ nombre: str
+ edad: str
+ especie: str
+ raza: str
+ peso: float
+ sexo: str
+ fallecido: bool
-------
"""

class Mascota:
    def __init__(self, 
        nombre: str, 
        edad: str, 
        especie: str, 
        raza: str, 
        peso: float, 
        sexo: str, 
        fallecido: bool
    ):
        self.nombre: str = nombre
        self.edad: str = edad
        self.especie: str = especie
        self.raza: str = raza
        self.peso: float = peso
        self.sexo: str = sexo
        self.fallecido: bool = fallecido

