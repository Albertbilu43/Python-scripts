# Databricks notebook source
# MAGIC %md
# MAGIC --------------------------------------------------------------
# MAGIC ### Unpacking (splat operator)
# MAGIC --------------------------------------------------------------
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC --------------------------------------------------------------
# MAGIC #### How it works
# MAGIC
# MAGIC El operador de desempaquetado * en Python (a menudo llamado operador splat) se utiliza para extraer los elementos individuales de un objeto iterable como una lista, tupla o cadena de texto.
# MAGIC Dependiendo del contexto en el que escribas *a, su comportamiento cambia drásticamente.
# MAGIC --------------------------------------------------------------
# MAGIC
# MAGIC #### Examples:

# COMMAND ----------

# MAGIC %md
# MAGIC ###### 1. Desempaquetado en argumentos de funciones
# MAGIC
# MAGIC Cuando usas *a al llamar a una función, extraes los elementos del iterable a para pasarlos como argumentos posicionales individuales

# COMMAND ----------

def calcular_volumen(largo, ancho, alto):
    return largo * ancho * alto

dimensiones = [5, 3, 2]

# En lugar de hacer: calcular_volumen(dimensiones[0], dimensiones[1], dimensiones[2])
resultado = calcular_volumen(*dimensiones)
print(resultado)  # Resultado: 30


# COMMAND ----------

# MAGIC %md
# MAGIC ###### 2. Desempaquetado extendido en asignaciones
# MAGIC
# MAGIC Si usas *a en el lado izquierdo de una asignación de variables, este captura todos los elementos sobrantes del iterable y los almacena dentro de una lista
# MAGIC
# MAGIC ##### Example One

# COMMAND ----------

numeros = [1, 2, 3, 4, 5]

# Capturar extremos y dejar el resto al centro
primero, *medio, ultimo = numeros

print(primero)  # Resultado: 1
print(medio)    # Resultado: [2, 3, 4] (siempre devuelve una lista)
print(ultimo)   # Resultado: 5


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Example Two

# COMMAND ----------

nums = [10, 20, 30, 40]
a, *b, c = nums
print(a)
print(b)
print(c)
print('Done')

# COMMAND ----------

# MAGIC %md
# MAGIC ####### The * operator unpacks elements from an itearble.
# MAGIC
# MAGIC - a takes the FIRST element
# MAGIC - c takes the LAST element
# MAGIC - b takes the the REST of the elements 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###### 3. Fusión y creación de colecciones
# MAGIC
# MAGIC Puedes usar *a dentro de nuevos literales de listas, tuplas o conjuntos para combinar colecciones de una manera limpia y legible

# COMMAND ----------

parte_1 = [1, 2, 3]
parte_2 = [4, 5, 6]

# Combinar listas fácilmente
lista_completa = [*parte_1, *parte_2, 7, 8]
print(lista_completa)  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8]


# COMMAND ----------

# MAGIC %md
# MAGIC ###### 4. Desempaquetado rápido con print()
# MAGIC Una alternativa muy común para imprimir los elementos de un iterable separados por espacios, sin necesidad de usar un bucle for

# COMMAND ----------

letras = ['P', 'y', 't', 'h', 'o', 'n']
print(*letras)  # Resultado: P y t h o n
