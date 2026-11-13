STOCK_MAXIMO = 25
equipos_disponibles = STOCK_MAXIMO
historial_usos = 0

print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Equipos disponibles.")
    print("2.- Asignar equipo.")
    print("3.- Liberar equipo.")
    print("4.- Historial de usos.")
    print("5.- Salir.")
    
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        print(f"\nCantidad actual de equipos disponibles: {equipos_disponibles}")

    elif opcion == "2":
        entrada = input("Ingresa la cantidad de equipos a asignar: ")
        if entrada.isdigit():
            cantidad = int(entrada)
            if cantidad <= 0:
                print("Error: La cantidad a asignar debe ser mayor a 0.")
            elif cantidad > equipos_disponibles:
                print(f"Error: No hay suficientes equipos disponibles. Stock actual: {equipos_disponibles}.")
            else:
                equipos_disponibles -= cantidad
                historial_usos += cantidad
                print(f"Se han asignado {cantidad} equipo(s) correctamente.")
        else:
            print("Error: Por favor, ingresa un número entero válido.")
            
    elif opcion == "3":
        entrada = input("Ingresa la cantidad de equipos a liberar: ")
        if entrada.isdigit():
            cantidad = int(entrada)
            if cantidad <= 0:
                print("Error: La cantidad a liberar debe ser mayor a 0.")
            elif equipos_disponibles + cantidad > STOCK_MAXIMO:
                print(f"Error: No se puede superar la capacidad máxima del laboratorio ({STOCK_MAXIMO} equipos).")
            else:
                equipos_disponibles += cantidad
                historial_usos -= cantidad
                print(f"Se han liberado {cantidad} equipo(s) correctamente.")
        else:
            print("Error: Por favor, ingresa un número entero válido.")
        
    elif opcion == "4":
        print(f"\nHistorial de usos (equipos actualmente asignados en la sesión): {historial_usos}")
        
    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
        
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 5.")