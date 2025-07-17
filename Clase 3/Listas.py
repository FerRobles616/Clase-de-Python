"""
Ejemplo de uso de listas en Python.
"""

array= ["futbol","Pc",18.6, 18, [6,7,10,4], True, False]

print(array)  # Imprime el contenido de la lista

# Acceso a un elemento de la lista
print(array[0])  # Imprime el primer elemento de la lista
print(array[4])  # Imprime el quinto elemento de la lista, que es otra lista
print(array[4][2])  # Imprime el tercer elemento de la lista anidada dentro de 'array'
print(len(array))  # Imprime la longitud de la lista 'array'
array.append(66)  # Agrega un nuevo elemento al final de la lista
print(array)  # Imprime la lista actualizada
array.insert(1, "Baloncesto")  # Inserta un nuevo elemento en la posición 1
print(array)  # Imprime la lista actualizada
array.remove("Pc")  # Elimina el primer elemento que coincide con "Pc"
print(array)  # Imprime la lista actualizada
array.pop()  # Elimina el último elemento de la lista
print(array)  # Imprime la lista actualizada
array.pop(2)  # Elimina el elemento en la posición 2
print(array)  # Imprime la lista actualizada
array.clear()  # Elimina todos los elementos de la lista
print(array)  # Imprime la lista vacía
array = ["futbol", "Pc", 18.6, 18, [6, 7, 10, 4], True, False]
array2 = ["Baloncesto", "Tenis", "Bollebol"]
array3 = array + array2  # Combina dos listas
print(array3)  # Imprime la lista combinada
print(array3.count("Pc"))  # Cuenta cuántas veces aparece "Pc" en la lista
print(array3.index("Pc"))  # Encuentra el índice del primer elemento "Pc" en la lista
array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array4.reverse()  # Invierte el orden de los elementos en la lista
print(array4)  # Imprime la lista invertida
array5 = [3, 5, 1, 4, 2, 6, 8, 7, 9, 10]
array5.sort()  # Ordena los elementos de la lista en orden ascendente
print(array5)  # Imprime la lista ordenada