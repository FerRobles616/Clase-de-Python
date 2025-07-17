"""
# Ejemplo estructura de control For
"""
for i in range(6):  # Itera desde 0 hasta 5
    print("Contador:", i)  # Imprime el valor actual del contador
print("Fin del bucle for")  # Mensaje al finalizar el bucle

array = ["futbol", "Pc", 18.6, 18, [6, 7, 10, 4], True, False]
array.append("Baloncesto")  # Agrega un nuevo elemento a la lista
for i in range(len(array)):  # Itera sobre cada elemento de la lista
    print("Elemento en la posición", i, ":", array[i])  # Imprime el elemento actual
print("Fin del bucle for sobre lista")  # Mensaje al finalizar el bucle
