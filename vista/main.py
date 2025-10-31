"""
Módulo de vista del Gestor de Estudiantes.
Proporciona una interfaz por consola para interactuar con el sistema.
"""

from controlador.gestor import GestorEstudiantes


def mostrar_menu():
    """Muestra las opciones disponibles al usuario."""
    print("\n=== GESTOR DE ESTUDIANTES ===")
    print("1. Registrar estudiante")
    print("2. Listar estudiantes")
    print("3. Actualizar nota")
    print("4. Eliminar estudiante")
    print("5. Consultar estudiantes con nota >= 4.0")
    print("0. Salir")


def main():
    """Función principal del programa (vista por consola)."""
    gestor = GestorEstudiantes()  # Instancia del controlador

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            nota = float(input("Nota: "))
            gestor.registrar_estudiante(nombre, correo, nota)

        elif opcion == "2":
            estudiantes = gestor.mostrar_estudiantes()
            print("\n[LISTADO DE ESTUDIANTES]")
            for est in estudiantes:
                print(f"{est[1]} | {est[2]} | Nota: {est[3]}")

        elif opcion == "3":
            correo = input("Correo del estudiante: ")
            nueva_nota = float(input("Nueva nota: "))
            gestor.actualizar_nota(correo, nueva_nota)

        elif opcion == "4":
            correo = input("Correo del estudiante a eliminar: ")
            gestor.eliminar_estudiante(correo)

        elif opcion == "5":
            umbral = float(input("Ingrese la nota mínima (ej. 4.0): "))
            destacados = gestor.consultar_por_nota(umbral)
            print("\n[ESTUDIANTES DESTACADOS]")
            for est in destacados:
                print(f"{est[0]} | Nota: {est[1]}")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("[ERROR] Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()
