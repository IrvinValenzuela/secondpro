tareas = []
while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("Opción: ")
    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append(tarea)
        print("✅ Agregada")
    elif opcion == "2":
        for i, t in enumerate(tareas, 1):
            print(f" {i}. {t}")
    elif opcion == "3":
        idx = int(input("# a eliminar: "))
        tareas.pop(idx - 1)
    elif opcion == "4":
        break