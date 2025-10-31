"""
Módulo del modelo: estudiante.py
Responsable de la persistencia de datos (crear base, insertar, listar, actualizar y eliminar registros).
Cumple el principio de Responsabilidad Única (S).
"""

import sqlite3
from pathlib import Path


NOMBRE_BD = "estudiantes.db"


def crear_base(nombre_bd: str = NOMBRE_BD) -> None:
    """Crea una base de datos SQLite con la tabla 'estudiantes'."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            nota REAL
        )
    """)
    conn.commit()
    conn.close()
    print(f"[OK] Base de datos '{nombre_bd}' lista para uso.")


def insertar_estudiante(nombre: str, correo: str, nota: float, nombre_bd: str = NOMBRE_BD) -> None:
    """Inserta un nuevo registro de estudiante en la base de datos."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)",
                    (nombre, correo, nota))
        conn.commit()
        print(f"[OK] Estudiante '{nombre}' agregado correctamente.")
    except sqlite3.IntegrityError:
        print(f"[ERROR] Ya existe un estudiante con el correo: {correo}")
    finally:
        conn.close()


def listar_estudiantes(nombre_bd: str = NOMBRE_BD) -> list:
    """Devuelve una lista con todos los estudiantes registrados."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, correo, nota FROM estudiantes")
    registros = cur.fetchall()
    conn.close()
    return registros


def actualizar_nota(correo: str, nueva_nota: float, nombre_bd: str = NOMBRE_BD) -> None:
    """Actualiza la nota de un estudiante según su correo."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("UPDATE estudiantes SET nota = ? WHERE correo = ?", (nueva_nota, correo))
    conn.commit()
    if cur.rowcount:
        print(f"[OK] Nota actualizada para {correo}.")
    else:
        print(f"[ADVERTENCIA] No se encontró estudiante con correo {correo}.")
    conn.close()


def eliminar_estudiante(correo: str, nombre_bd: str = NOMBRE_BD) -> None:
    """Elimina un estudiante de la base de datos por su correo."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("DELETE FROM estudiantes WHERE correo = ?", (correo,))
    conn.commit()
    if cur.rowcount:
        print(f"[OK] Estudiante con correo {correo} eliminado.")
    else:
        print(f"[ADVERTENCIA] No existe estudiante con correo {correo}.")
    conn.close()


def consultar_por_nota(umbral: float = 4.0, nombre_bd: str = NOMBRE_BD) -> list:
    """Retorna los estudiantes con nota mayor o igual al umbral."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()
    cur.execute("SELECT nombre, nota FROM estudiantes WHERE nota >= ?", (umbral,))
    resultados = cur.fetchall()
    conn.close()
    return resultados
