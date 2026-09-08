# Tipos de datos
variable_string: str = "Hola mundo"
variable_numero_entero: int = 2026
variable_numero_decimal: float = 1.5
variable_booleano_falso: bool = False
variable_booleano_verdadero: bool = True

# Colecciones
variable_lista: list = ["Manzana", "Pera", "Naranja", "Mandarina"]
variable_tupla: tuple = (5, 2.5, 1, 0.5, 4, 4.5)
variable_diccionarios: dict = {"nombre": "Sebastian", "color": "Azul"}

# Funciones
def suma(a: int, b: int) -> int:
    return a + b

# Bucles
condicion: bool = True
while condicion == True:
    print("Hola")

    if input("¿Quieres salir?: ") == "Si":
        condicion = False

while True:
    print("Hola")

    if input("¿Quieres salir?: ") == "Si":
        break

# Iteración
lista_de_personas: list = ["Gabriel", "Jose", "Alejandro", "Javiera"]
for persona in lista_de_personas:
    print(persona)

palabra: str = "Diccionario"
for letra in palabra:
    print(letra)

for i in range(5):
    print(i)

# Estructuras de decision
palabra_secreta = "123pormi"
adivinacion = input("Adivina la palabra secreta: ")
if palabra_secreta == adivinacion:
    print("Adivinaste la palabra secreta 😁")
elif adivinacion == "":
    print("Oye, al menos esfuerzate 😒")
else:
    print("No adivinaste 🤣")