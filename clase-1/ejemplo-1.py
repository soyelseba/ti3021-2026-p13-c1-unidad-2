# Un docente necesita clasificar el 
# rendimiento de un estudiante a partir 
# de tres calificaciones en escala de 1,0 a 7,0.

"""
------------------------------------------
|               Estudiante               |
|----------------------------------------|
| - nombre: str                          |
| - notas: list<<float>>                 |
| - / promedio: float                    |
| - / clasificacion: str                 |
|----------------------------------------|
| - calcularPromedio(notas): float       |
| - calcularClasificacion(promedio): str |
| + mostrarResumen(): void               |
------------------------------------------
"""

class Estudiante:
    def __init__(self, nombre: str, notas: list[float]):
        self.__nombre: str = nombre
        self.__notas: list[float] = notas
        self.__promedio: float = self.__calcularPromedio(self.__notas)
        self.__clasificacion: str = self.__calcularClasificacion(self.__promedio)

    def __calcularPromedio(self, notas: list[float]) -> float:
        return sum(notas) / len(notas)

    def __calcularClasificacion(self, promedio: float) -> str:
        if promedio < 4.0: return "Reprobado"
        elif promedio >= 4.0 and promedio <= 4.99: return "Aprobado"
        elif promedio >= 5.0 and promedio <= 5.99: return "Buen rendimiento"
        elif promedio >= 6.0 and promedio <= 7.0: return "Rendimiento destacado"

    def mostrarResumen(self) -> None:
        print(f"Estudiante: {self.__nombre}")
        print(f"Promedio: {self.__promedio}")
        print(f"Clasificacion: {self.__clasificacion}")
