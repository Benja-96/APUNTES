investigadores_principales = 0
investigadores_asistentes = 0

while True:
    entrada_cantidad = input("Ingresa la cantidad de científicos que deseas registrar: ")

    if entrada_cantidad.isdigit() and int(entrada_cantidad) > 0:
        cantidad_cientificos = int(entrada_cantidad)
        break
    else:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

for i in range(1, cantidad_cientificos + 1):
    print(f"\n--- Registro del científico {i} de {cantidad_cientificos} ---")
    
    while True:
        id_cientifico = input("Ingresa el ID del científico: ")
        if len(id_cientifico) >= 12 and " " not in id_cientifico:
            break
        else:
            print("ID inválido. Debe tener al menos 12 caracteres y no contener espacios.")
            
    while True:
        entrada_publicaciones = input("Ingresa el número de publicaciones del científico: ")
        if entrada_publicaciones.isdigit() and int(entrada_publicaciones) > 0:
            publicaciones = int(entrada_publicaciones)
            break
        else:
            print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
            
    if publicaciones > 12:
        investigadores_principales += 1
        print(f"Científico {id_cientifico} clasificado como: Investigador Principal.")
    else:
        investigadores_asistentes += 1
        print(f"Científico {id_cientifico} clasificado como: Investigador Asistente.")

print(f"\n¡El instituto cuenta con {investigadores_principales} Investigadores Principales y {investigadores_asistentes} Investigadores Asistentes! ¡Ciencia en marcha!")