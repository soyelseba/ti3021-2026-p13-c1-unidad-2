# Operadores condicionales
# ==    # ¿Es igual?
# >     # ¿Es mayor que?
# <     # ¿Es menor que?
# >=    # ¿Es mayor o igual que?
# <=    # ¿Es menor o igual que?
# !=    # ¿Es distinto de? / ¿Es diferente de?
# NOT   # No es
# and   # Y es
# or    # O es

# True es similar a 1 y False es similar a 0.
print( "0 == False es =: ", 0 == False ) # Resultado:
print( "1 == True es =: ", 1 == True ) # Resultado:

# Calcular si un numero es par o impar.
numero = int(input("Inserta un numero: "))
if (numero % 2) == 1:
    print(f"El numero {numero} es impar")
elif (numero % 2) == 0:
    print(f"El numero {numero} es par")


# Comparaciones numericas
print(5 == 5.0) # 1. Es verdadero
print(5 > 5.0)  # 2. Es falso
print(5 < 5.0)  # 3. Es falso
print(5 >= 5.0) # 4. Es verdadero
print(5 <= 5.0) # 5. Es verdadero
print(5 != 5.0) # 6. Es falso

# Comparaciones de texto
print( "Hola" == "hola" ) # 1. Es falso
print( "hola".upper() == "HOLA" ) # 2. Es verdadero
print( "hola" == "HOLA".lower() ) # 3. Es verdadero
print( "holacomoestas" == "hola como estas".strip()) # 4.