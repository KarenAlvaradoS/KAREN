#Programa 1: Búsqueda en Arreglo Multidimensional
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, None, None

# Matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_buscado = 5

# Buscar el valor en la matriz
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if encontrado:
    print(f"El valor {valor_buscado} se encontró en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
