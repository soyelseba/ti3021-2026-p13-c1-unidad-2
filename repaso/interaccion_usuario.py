# Entrada y Salida de datos
print() # -> Salida de datos
input() # <- Ingreso de datos

# 1. Imprimir hola mundo
print("Hola mundo")

# 2. Imprimir concatenado
print("Hola mundo", "Soy el Seba") # -> "Hola mundo Soy el Seba"
print(f"Hola mundo Soy el Seba") # -> "Hola mundo Soy el Seba"
print("Hola mundo" + " " + "Soy el Seba") # -> "Hola mundo Soy el Seba"

# 3. Triple comillas
print(
    """
    =============================================
    |***Puedo escribir**************************|
    |               Texto en 3                  |
    |                        Dimensiones        |
    =============================================
    """
      )

# 4. Recibir dato del usuario + mensaje
print( input("Inserta un dato aquí: ") )
# Resultado: Muestra mensaje y acompaña sólo en la escritura
# el valor final es sólo lo que ingresa el usuario.

# 5. Recibir sólo números del usuario
numero = int( input("Dame un número: ") )
# Explicación: el input recibe el dato y la función int
# intenta transformar el dato ingreso a int.
# Me da error si intento ingresar algo que no pueda ser int
# cómo letras o un numero decimal.