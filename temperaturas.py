# Crear una matriz 3D para representar los datos de temperaturas diarias
# Supongamos que tenemos 3 ciudades, 7 días de la semana y 4 semanas
temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [25, 26, 24, 27, 26, 28, 23],
        # Semana 2
        [22, 21, 23, 24, 25, 26, 27],
        # Semana 3
        [28, 29, 30, 31, 32, 33, 34],
        # Semana 4
        [20, 21, 22, 23, 24, 25, 26]
    ],
    # Ciudad 2
    [
        # Semana 1
        [28, 29, 30, 31, 32, 33, 34],
        # Semana 2
        [25, 26, 27, 28, 29, 30, 31],
        # Semana 3
        [22, 21, 22, 23, 24, 25, 26],
        # Semana 4
        [27, 26, 25, 24, 23, 22, 21]
    ],
    # Ciudad 3
    [
        # Semana 1
        [20, 21, 22, 23, 24, 25, 26],
        # Semana 2
        [28, 29, 30, 31, 32, 33, 34],
        # Semana 3
        [25, 26, 27, 28, 29, 30, 31],
        # Semana 4
        [22, 21, 22, 23, 24, 25, 26]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad, semana_ciudad in enumerate(temperaturas, start=1):
    for semana, dias_semana in enumerate(semana_ciudad, start=1):
        promedio = sum(dias_semana) / len(dias_semana)
        print(f"Promedio de temperaturas para ciudad {ciudad}, Semana {semana}: {promedio:.2f}")
