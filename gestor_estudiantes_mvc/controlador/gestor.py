"""
Módulo controlador del proyecto Gestor de Estudiantes.
Coordina la interacción entre la vista (interfaz de usuario)
y el modelo (acceso a datos).
"""

from modelo import estudiante as modelo


class GestorEstudiantes:
    """
    Clase que centraliza la lógica de negocio del sistema.
    No accede directamente a la base de datos,
    sino que utiliza las funciones definidas en el módulo 'modelo.estudiante'.
    """

    def __init__(self, nombre_bd: str = "estudiantes.db"):
        """Inicializa el gestor con la base de datos a usar."""
        self.nombre_bd = nombre_bd
        modelo.crear_base(nombre_bd)

    def registrar_estudiante(self, nombre: str, correo: str, nota: float) -> None:
        """Agrega un nuevo estudiante a la base de datos."""
        modelo.insertar_estudiante(nombre, correo, nota, self.nombre_bd)

    def mostrar_estudiantes(self) -> list:
        """Retorna la lista completa de estudiantes registrados."""
        return modelo.listar_estudiantes(self.nombre_bd)

    def actualizar_nota(self, correo: str, nueva_nota: float) -> None:
        """Actualiza la nota de un estudiante identificado por su correo."""
        modelo.actualizar_nota(correo, nueva_nota, self.nombre_bd)

    def eliminar_estudiante(self, correo: str) -> None:
        """Elimina un estudiante de la base de datos."""
        modelo.eliminar_estudiante(correo, self.nombre_bd)

    def consultar_por_nota(self, umbral: float) -> list:
        """Devuelve una lista de estudiantes con nota mayor o igual al umbral."""
        return modelo.consultar_por_nota(umbral, self.nombre_bd)

    def eliminar_por_nota(self, limite: float) -> None:
        """
        Elimina todos los estudiantes cuya nota sea menor al valor especificado.

        Utiliza:
        DELETE FROM estudiantes WHERE nota < ?
        """
        modelo.eliminar_por_nota(limite, self.nombre_bd)

    def listar_ordenados_por_nota(self) -> list:
        """
        Retorna los estudiantes ordenados de forma descendente por nota.

        Utiliza:
        SELECT * FROM estudiantes ORDER BY nota DESC
        """
        return modelo.listar_ordenados_por_nota(self.nombre_bd)

    def buscar_por_nombre(self, parte_nombre: str) -> list:
        """
        Busca estudiantes cuyo nombre contenga una cadena parcial.

        Utiliza:
        SELECT * FROM estudiantes WHERE nombre LIKE '%<parte_nombre>%'
        """
        return modelo.buscar_por_nombre(parte_nombre, self.nombre_bd)
