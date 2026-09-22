# Tipos de dato
str # <- Texto usando doble comillas o comilla simple
int # <- Numeros enteros
float # <- Numeros decimales
bool # <- Guardar un estado en verdadero o falso

# String -> str
mensaje1 = "Hola mundo"
mensaje2 = 'Mi nombre es Sebastian'
# Concatenación
## Juntar 2 valores. Ejemplo:
mensaje_compuesto1 = mensaje1 + " " + mensaje2
### Resultado: 'Hola mundo Mi nombre es Sebastian'
### Explicación: Se adicionan tal y como están.
mensaje_compuesto2 = f"{mensaje1} {mensaje2}"
### Resultado: 'Hola mundo Mi nombre es Sebastian'
### Explicación: f nos permite establecer o inyectar
### valores de manera directa en una String ocupando
### llaves para ingresar el valor explicito dentro de la String.

# Numericos -> int y float
numero_entero = 250
numero_decimal = 1.5
# Los decimales nos pueden dan impresiciones
# a nivel matematico, por ejemplo: 0.6 + 0.7 = 1.29997
# Para resolver este problema
# ocupo la librería decimal de la siguiente manera
from decimal import Decimal
numero_decimal_preciso = Decimal('1.5')

## Operadores matematicos
# + = Suma
# - = Resta
# * = Multiplicacion
# / = Division
# % = MODulo
# ** = Potencia
# () = Parentesis

##############################################
# Desafío 1: ¿Cuál es el resultado?          #
operacion_matematica = (5 + 10) * 2 ** 1
print("Desafío 1. Resultado: ", operacion_matematica)
##############################################

# Booleano: 2 estados.
verdad = True # 1 = Existe
falso = False # 0 = None

# ¿Cómo pregunto el tipo de dato de una variable?
type( "Hola" ) # str
type( 250 ) # int
type( 1.5 ) # float
type( Decimal("1.5") ) # decimal
type( False ) # bool