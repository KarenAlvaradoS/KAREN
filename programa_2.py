# Programa 2: Ordenación de Arreglo Multidimensional
def ordenar_fila(matriz, fila):
    matriz[fila].sort()

# Matriz de ejemplo
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Fila a ordenar (índice)
fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
