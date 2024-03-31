# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    # Escribir notas personales en el archivo
    file.write("Nota 1: PREPARAR PAPILLA PARA LUIS JHOAN A LAS 7:00 am.\n")
    file.write("Nota 2: ALIMENTAR A LUIS JHOAN CON LA PAPILLA A LAS 7:45 am.\n")
    file.write("Nota 3: BAÑAR A LUIS JHOAN A LAS 9:45 am.\n")
    file.write("Nota 4: VESTIR A LUIS JHOAN A LAS 10:30 am.")
    file.write("Nota 5: AMAMANTAR A LUIS jHOAN A LAS 10:40 am.\n")
    file.write("Nota 6: PONER EN LA CUNA A LUIS JHOAN A LAS 11:10 am.\n")

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file.readlines():
        # Mostrar cada línea en la consola
        print(line.strip())

# Cierre de Archivo
file.close()

