# Encapsulamiento
# Proteger el acceso a los atributos y metodos
# de cada clase dentro y fuera de este.

# getter() -> Obtener dato
# setter(nuevo_dato) -> Modificar o establecer dato


"""
Mascota
-------
- nombre: str
- edad: str
- especie: str
- raza: str
- peso: float
- sexo: str
- fallecido: bool
-------
+ obtener_nombre(): str
+ obtener_edad(): str
+ obtener_especie(): str
+ obtener_raza(): str
+ obtener_peso(): float
+ obtener_sexo(): str
+ obtener_fallecido(): bool
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

    def obtener_nombre(self) -> str : return self.__nombre
    def obtener_edad(self) -> str : return self.__edad
    def obtener_especie(self) -> str : return self.__especie
    def obtener_raza(self) -> str : return self.__raza
    def obtener_peso(self) -> float : return self.__peso
    def obtener_sexo(self) -> str : return self.__sexo
    def obtener_fallecido(self) -> bool : return self.__fallecido

    def __str__(self):
        return f"""
                Nombre: {self.__nombre}
                Edad: {self.__edad}
                Especie: {self.__especie}
                Raza: {self.__raza}
                Peso: {self.__peso}
                Sexo: {self.__sexo}
                Fallecido: {self.__fallecido}
                """

mascota_1 = Mascota(
    nombre="Cachupin",
    edad="1 año y 5 meses",
    especie="Canino Domestico",
    raza="Pitbull",
    peso=18.5, # Kilogramos
    sexo="Macho",
    fallecido=False,
)

print(mascota_1)


