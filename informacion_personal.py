# Crear un diccionario llamado informacion_personal con información ficticia
informacion_personal = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ciudad A",
}

# Imprimir el diccionario original
print("Diccionario original:")
print(informacion_personal)

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ciudad B"

# Agregar una nueva clave-valor al diccionario para representar la profesión de la persona
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "555-1234"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)
