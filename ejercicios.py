"""Proyecto de lógica: Katas de Python.
Soluciones recopiladas del cuaderno de trabajo.
Nota: el enunciado del ejercicio 35 no aparece en el cuaderno original.
"""
from functools import reduce

# EJERCICIO 1
# Enunciado:
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    """ Devuelve un diccionario {letra: frecuencia en el texto}, ignorando espacios.


    Args:
        texto (str): el texto introducido

    Returns:
        dict: frecuencia de cada letra en el texto en modo diccionario. 
    """
    frecuencias = {}
    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] =1
    return frecuencias

texto = "data analytics"
resultado = frecuencia_letras(texto)
print(resultado)

# EJERCICIO 2
# Enunciado:
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros = [1, 2, 3, 4, 5]

def doble (numeros):
    return numeros*2

# Devuelve una lista con el doble de cada número, utiizando list
# map aplica la lambda a cada elemento; list() convierte el resultado en lista

lista_dobles = list(map(doble, numeros))
print(lista_dobles)

# EJERCICIO 3
# Enunciado:
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    lista_palabra_objetivo = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            lista_palabra_objetivo.append(palabra)
    
    return lista_palabra_objetivo

lista_palabras = ["farmacia", "farmacologia", "oncologia", "farmaceutica"]
palabra_objetivo = "farma"
print (filtrar_palabras(lista_palabras, palabra_objetivo ))

# EJERCICIO 4
# Enunciado:
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencia (lista_a, lista_b):
    diferencia = list(map(lambda a, b: a-b, lista_a, lista_b))
    return diferencia

lista_a = [10, 20, 30]
lista_b = [1, 5, 10]

print(calcular_diferencia(lista_a, lista_b))

# EJERCICIO 5
# Enunciado:
# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.

def calcular_media_estado (notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return media, estado


lista_notas = [6, 5, 8, 7, 3]

resultado_notas = calcular_media_estado(lista_notas)
print(f'Tu nota es: {resultado_notas}')

# EJERCICIO 6
# Enunciado:
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial (n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial (n-1)

resultado_factorial = factorial(5)
print(resultado_factorial)

# EJERCICIO 7
# Enunciado:
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def combierte_tupla_string (tupla_empresas):
    resultado_empresas = list(map(str, tupla_empresas))
    return resultado_empresas

tupla_empresas = ("ULMA", "Fagor", "Erreka", "Athlon")

resultado_empresas = combierte_tupla_string(tupla_empresas)

print(resultado_empresas)
print(type(resultado_empresas))

# EJERCICIO 8
# Enunciado:
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

try:
    """Pide dos numeros e intenta dividir, controlando posibles errores"""
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2

    print("La división se ha realizado correctamente.")
    print("El resultado es:", resultado)

except ValueError:  #Si no es un numero lanza este error y mensaje:
    print("Error: debes introducir valores numéricos.")

except ZeroDivisionError: #Si el numero es 0 lanza este error y mensaje:
    print("Error: no se puede dividir entre cero.")

# EJERCICIO 9
# Enunciado:
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre"
# ,
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente piton", "Cocodrilo", "Oso"]

def mascotas_permitidas (mascota):
    return mascota not in mascotas_prohibidas

def filtrar_mascotas_prohibidas (mascotas):
    lista_mascotas = filter (mascotas_permitidas, mascotas)
    return list (lista_mascotas)

mascotas = ["Perro", "Tigre", "Gato", "Oso", "Conejo"]

mascotas_permitidas = filtrar_mascotas_prohibidas(mascotas)
print(mascotas_permitidas)

# EJERCICIO 10
# Enunciado:
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para listas sin elementos."""


def calcular_promedio(numeros):
    """Devuelve el promedio o lanza ListaVaciaError si la lista está vacía."""
    if not numeros:  # una lista vacía se evalúa como False
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)


# Se prueba con una lista normal y con una vacía
for lista in ([12, 16, 20], []):
    try:
        print(f"Promedio de la lista {lista} es: {calcular_promedio(lista)}")
    except ListaVaciaError as error:
        print(f"Error: {error}")

# EJERCICIO 11
# Enunciado:
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

try:
    edad = int(input("Dime cual es tu edad"))

    if edad <0 or edad >120:  #para fijar el rango entre 0 y 120
        print("No es posible tener esa edad.")
    else:
        print(f'Tu edad es {edad}')

except ValueError:  #si no mete un valor numerico entero saldra esto
    print("Debes introducir un numero entero")

# EJERCICIO 12
# Enunciado:
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras (frase):
    palabras = frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

frase = input("Dime una frase")
longitudes = longitud_palabras(frase)
print(longitudes)

# EJERCICIO 13
# Enunciado:
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def convertir_letra(letra):
    return (letra.upper(), letra.lower())

def convertir_letras(caracteres):
    caracteres_unicos = set(caracteres)
    resultado = list(map(convertir_letra, caracteres_unicos))
    return resultado

caracteres = "amasd"
print(convertir_letras(caracteres))

# EJERCICIO 14
# Enunciado:
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()

""" Imagina que tenemos este conjunto_animales = ["perro", "vaca", "gato", "pajaro", "puma", "pez", "loro"]
y la letra que queremos filtrar es la letra = "p" """

def filtrar_animales_p (animales, letra):
    resultado = filter(lambda palabra: palabra.startswith(letra), animales)
    return list(resultado)
    
conjunto_animales = ["perro", "vaca", "gato", "pajaro", "puma", "pez", "loro"]
print(filtrar_animales_p(conjunto_animales, "p"))

# EJERCICIO 15
# Enunciado:
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

lista_para_sumar = [1, 3, 5, 7]

sumar_tres = lambda x: x+3 

resultado_suma3 = list(map(sumar_tres, lista_para_sumar))

print(resultado_suma3)

# EJERCICIO 16
# Enunciado:
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

def filtrar_palabras (texto, n):
    palabras = texto.split() #Aqui separaremos las palabras del texto por el espacio
    resultado = filter(lambda palabra: len(palabra)>n, palabras) 
    return list(resultado)

texto = "me esta gustando mucho el master de data analytics"
n = 5
print(filtrar_palabras(texto, n))

# EJERCICIO 17
# Enunciado:
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

#para utilizar reduce() hay que importar primero:

from functools import reduce

#multiplicaremos el numero que llevamos acumulado por 10 y le sumaremos el siguiente digito

def convertir_numero (digitos):
    numero = reduce(lambda acumulado, digito: acumulado *10 +digito, digitos)
    return numero

digitos = [5, 7, 2]
numero_acumulado = convertir_numero(digitos)
print(f'El numero es: {numero_acumulado}')

# EJERCICIO 18
# Enunciado:
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [{"nombre": "maddi", "edad": 20, "calificacion": 95},
               {"nombre": "jon", "edad": 22, "calificacion": 50},
               {"nombre": "leire", "edad": 26, "calificacion": 91},
               {"nombre": "mikel", "edad": 24, "calificacion": 70}, 
               {"nombre": "julen", "edad": 26, "calificacion":90}]

def filtrar_estudiantes (estudiantes):
    sobresalientes = filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)
    return list(sobresalientes)

sobresalientes = filtrar_estudiantes(estudiantes)
print("Estudiantes con sobresaliente son:")
print(sobresalientes)

# EJERCICIO 19
# Enunciado:
# 19. Crea una función lambda que filtre los números impares de una lista dada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = filter (lambda numero: numero %2 != 0, numeros)
numeros_impares = list(impares)
print(f'Los numeros impares son: {numeros_impares}')

# EJERCICIO 20
# Enunciado:
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

lista_elementos = ["hola", 3, "Python", "5", 10, 20,]

solo_int = filter(lambda elemento: isinstance(elemento, int), lista_elementos)

enteros = list(solo_int)
print(f'La lista con los valores int es la siguiente: {enteros}')

# EJERCICIO 21
# Enunciado:
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo (numero):
    cubo = lambda numero: numero **3
    return cubo (numero)

n = 3
resultado_cubo = calcular_cubo(n)
print(f'El resultado del cubo del {n} es {resultado_cubo}')

"""Tambien podría ser asi:
cubo = lambda x: x ** 3

print(cubo(3))"""

# EJERCICIO 22
# Enunciado:
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

from functools import reduce

def producto_total(numeros):
    producto = reduce(lambda acumulado, numero: acumulado * numero, numeros)
    return producto

lista = [1, 2, 3, 4]
resultado_producto = producto_total(lista)
print(f'El resultado del producto es {resultado_producto}')

# EJERCICIO 23
# Enunciado:
# 23. Concatena una lista de palabras.Usa la función reduce().

from functools import reduce

def conectar_lista (lista_pal):
    unioin_palabras = reduce(lambda acumulado, palabra: acumulado + " " + palabra, lista_pal) #He utilizado " " para poner un espacio sobre las palabras
    return unioin_palabras

lista_pal = ["hola", "mi", "nombre", "es", "maddi"]
union_palabras = conectar_lista(lista_pal)
print(f'La union es: {union_palabras}')

# EJERCICIO 24
# Enunciado:
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

def calcular_diferencia (lista_valores):
    diferencia = reduce(lambda acumulado, valor: acumulado - valor, lista_valores)
    return diferencia

lista_valores = [10, 3, 2]
diferencia = calcular_diferencia(lista_valores)
print(f'La diferencia de los valores de la lista es: {diferencia}')

# EJERCICIO 25
# Enunciado:
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres (cadena_texto):
    return len(cadena_texto)

cadena_texto = "hola mi nombre es maddi"
longitud_cadena = contar_caracteres(cadena_texto)
print(f'La longitud de la cadena de texto es: {longitud_cadena}')

# EJERCICIO 26
# Enunciado:
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

def calcular_resto_division (num_1, num_2):
    resto = lambda num_1, num_2: num_1 % num_2 
    return resto (num_1, num_2)

num_1 = 6
num_2 = 2
resto = calcular_resto_division (num_1, num_2)
print(f'El resto de la division es: {resto}')

# EJERCICIO 27
# Enunciado:
# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio (lista_calculo_promedio):
    promedio = sum(lista_calculo_promedio) / len(lista_calculo_promedio)
    return promedio

lista_calculo_promedio = [1, 2, 3, 4, 5]
promedio_lista = calcular_promedio(lista_calculo_promedio)
print(f'El promedio de la lista es: {promedio_lista}')

# EJERCICIO 28
# Enunciado:
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def buscar_duplicado (lista_duplicado):
    vistos = set() #Utilizaremos set porque en los sets no pueden estar elementos repetidos

    for numero in lista_duplicado:
        if numero in vistos:
            return numero
        else:
            vistos.add(numero)
    return None

lista_duplicado = [2, 5, 7, 3, 5]
duplicado = buscar_duplicado(lista_duplicado)
print(f'El numero duplicado de la lista es: {duplicado}')

# EJERCICIO 29
# Enunciado:
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro

def enmascarar (variable_enmascarar):
    texto = str(variable_enmascarar)
    cantidad_caracteres_sustituir = max(0, len(texto) -4) #utilizamos max para frases con menos de 4 caracteres, para que no sea negativa
    conversion = "#" * cantidad_caracteres_sustituir + texto[-4:]
    return conversion

variable_enmascarar = "hola mi nombre es maddi"
resultado_enmascaramiento = enmascarar(variable_enmascarar)
print(f'El resultado del enmascaramiento es: {resultado_enamscaramiento}')

# EJERCICIO 30
# Enunciado:
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def anagramas (palabra1, palabra2):
    if sorted (palabra1) == sorted (palabra2): #sorted ordena caracteres de una cadena
        print("Las dos palabras son anagramas")
    else:
        print("Estas dos palabras no son anagramas")

palabra1= "amor"
palabra2= "roma"
resultado_anagrama = anagramas(palabra1, palabra2)

# EJERCICIO 31
# Enunciado:
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

nombres = input("Dime una lista de nombres separada por comas").split(",")
nombres = [nombre.strip() for nombre in nombres] #para eliminar espacios vacios que ponemos en el input detras de las comas

buscar_nombre = input("Dime que nombre quieres buscar en la lista")

if buscar_nombre in nombres:
    print(f'{buscar_nombre} esta en la lista')
else:
    raise ValueError(f'{buscar_nombre} no está en la lista')

# EJERCICIO 32
# Enunciado:
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

empleados_bar = [{"nombre": "maddi garcia", "puesto": "camarera"},
                 {"nombre": "miren uriarte", "puesto": "camarera"},
                 {"nombre": "june uriarte", "puesto": "encargada"},
                 {"nombre": "luka garcia", "puesto": "contable"},
                 {"nombre": "manex garcia", "puesto": "cocinero"}]


def buscar_empleado (nombre_completo, empleados_bar):
    for empleado in empleados_bar:
        if empleado ["nombre"]==nombre_completo:
            return empleado["puesto"]
    
    return "Esa persona no trabaja aqui"


buscar_nombre = input("Que empleado quieres que busque?").lower()
resultado_busqueda = buscar_empleado(buscar_nombre, empleados_bar)
print(resultado_busqueda)

# EJERCICIO 33
# Enunciado:
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def sumar_elementos_listas (primera_lista, segunda_lista):
    suma = list(map(lambda a, b: a+b, primera_lista, segunda_lista))
    return suma

primera_lista = [1, 2, 3]
segunda_lista = [4, 5, 6]

suma = sumar_elementos_listas(primera_lista, segunda_lista)
print(f'El resultado de la lista suma es: {suma}')

# EJERCICIO 34
# Enunciado:
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer tronco , nueva rama , crece ramas , quitar rama e info arbol.

class Arbol:
    """Árbol con un tronco (su longitud) y una lista de ramas (la longitud de cada una)."""

    def __init__(self):
        self.tronco = 1   # longitud inicial del tronco
        self.ramas = []   # lista vacía: cada elemento será la longitud de una rama

    def crecer_tronco(self):
        """Aumenta el tronco una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Añade una rama nueva de longitud 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta una unidad la longitud de todas las ramas."""
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama de la posición indicada (empezando a contar en 0)."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError(f"No existe ninguna rama en la posición {posicion}.")

    def info_arbol(self):
        """Devuelve la longitud del tronco, el número de ramas y la longitud de cada una."""
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas,
        }



arbol = Arbol()            # Crear un árbol
arbol.crecer_tronco()      # Tronco: 2
arbol.nueva_rama()         # Ramas: [1]
arbol.crecer_ramas()       # Ramas: [2]
arbol.nueva_rama()         # Dos ramas nuevas: [2, 1, 1]
arbol.nueva_rama()
arbol.quitar_rama(2)       # Se retira la rama de la posición 2: [2, 1]
print(arbol.info_arbol())  # Información del árbol

# EJERCICIO 35
# AVISO: el ejercicio 35 no está incluido en el cuaderno original.
# Añade aquí el enunciado y la solución antes de entregar el proyecto.

# EJERCICIO 36
# Enunciado:
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.

class UsuarioBanco:
    
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente #valor booleriano, true si lo tiene, false si no lo tiene
    
    def agregar_dinero (self, cantidad): #Sumar dinero al saldo 
        self.saldo += cantidad

    def retirar_dinero (self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            raise ValueError ("No tiene saldo para sacar esa cantidad de dinero")
        
    def transferir_dinero (self, destinatario, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            destinatario.saldo += cantidad
        else:
            raise ValueError ("No tiene saldo para transferir esa cantidad de dinero")
        



alicia = UsuarioBanco ("alicia", 100, True)
bob = UsuarioBanco ("bob", 50, True)


bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)  # Ejemplo: requiere saldo suficientealueError porque tiene menos de 80 ud
alicia.retirar_dinero(50)

print(f'El saldo de bob es:', bob.saldo)
print(f'El saldo de alicia es de:', alicia.saldo)

# EJERCICIO 37
# Enunciado:
# 37. Crea una función llamada procesar texto que procesa un texto según la opción especificada: contar palabras, reemplazar palabras , eliminar palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar texto.

def contar_palabras (texto):
    texto_recortado = texto.split()
    contador_palabras ={}

    for palabra in texto_recortado:
        if palabra in contador_palabras:
            contador_palabras [palabra] += 1
        else:
            contador_palabras[palabra] = 1
    
    return contador_palabras
   
def reemplazar_palabras (texto, palabra_original, palabra_nueva):
    texto_modificado = texto.replace(palabra_original, palabra_nueva)
    return texto_modificado

def eliminar_palabra (texto, palabra_original):
    texto_reducido = texto.replace(palabra_original, "")
    return texto_reducido

def procesar_texto (texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args [0], args [1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError ("opcion no valida")
    



texto = "hola yo soy maddi hola"

# 1. para contar la frecuencia de cada palabra:
frecuencia_palabras = contar_palabras(texto)
print(frecuencia_palabras)

# 2. reemplazamos la palabra "maddi" por "june"
texto_remplazado = reemplazar_palabras(texto, "maddi", "june")
print(f' El texto reemplazado es: "{texto_remplazado}"')

# 3. eliminamos la palabra hola del texto
texto_reducido = eliminar_palabra(texto, "hola")
print(f'La frase con la palabra eliminada es: "{texto_reducido}"')

# 4. funcion de procesar texto: 
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "hola", "adios"))
print(procesar_texto(texto, "eliminar", "hola"))

# EJERCICIO 38
# Enunciado:
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora = int(input("Introduce la hora (0-23):"))

if hora <0 or hora >23:
    print("Hora no valida")
elif hora >=7 and hora <13:
    print("Es de dia")
elif hora >=13 and hora <21:
    print ("Es de tarde")
else:
    print("Es de noche")

# EJERCICIO 39
# Enunciado:
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

nota = int(input("Que nota has sacado?"))

if nota >=0 and nota < 70:
    print(f'{nota}: insuficiente')
elif nota >=70 and nota <80:
    print(f'{nota}:bien')
elif nota >=80 and nota <90:
    print (f'{nota}: muy bien')
elif nota >=90 and nota <=100:
    print(f'{nota}: excelente')
else:
    print("No puedes sacar esa nota, debes tener entre 0 y 100")

# EJERCICIO 40
# Enunciado:
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo"
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math 
#Utilizaremos math basicamente para calcular la area del circulo, porque tenemos que utilizar el pi

def calcular_area_figura (figura, medidas):
    if figura == "rectangulo":
        b, h = medidas
        area_rectangulo = b * h
        return area_rectangulo
    elif figura == "triangulo":
        b, h = medidas
        area_triangulo = (b*h)/2
        return area_triangulo
    elif figura == "circulo":
        radio = medidas [0]
        area_circulo = math.pi * radio**2
        return area_circulo

    else:
        print("Figura no valida")

print(calcular_area_figura("rectangulo", (5, 6)))
print(calcular_area_figura("triangulo", (5, 8)))
print(calcular_area_figura("circulo", (6,)))

# EJERCICIO 41
# Enunciado:
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# - 1. Solicita al usuario que ingrese el precio original de un artículo.
# - 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# - 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# - 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# - 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# - 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.

precio_original = int(input("Cual es el precio original del articulo?"))

cupon_descuento = input("Tienes cupon de descuento?")

if cupon_descuento == "si":
    #Usaremos float en el descuento si hay numeros con decimal
    valor_descuento = float(input("Cual es el valor del vale de descuento?"))
    if valor_descuento >0:
        precio_final = precio_original - valor_descuento 
        print(f'El precio final con el descuento es: {precio_final}')
        print(f'El precio sin el descuento seria {precio_original}')
    elif valor_descuento <= 0:
        print("Ese cupon no es valido, tiene que ser mayor que 0")
        print(f'El precio final sin descuento es: {precio_original}')
elif cupon_descuento == "no":
    print(f'El precio del articulo es: {precio_original}')
else:
    raise ValueError ("La respuesta tiene que ser si o no")
