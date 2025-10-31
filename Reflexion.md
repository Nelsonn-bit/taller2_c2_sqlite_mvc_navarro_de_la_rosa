# Reflexión sobre la Implementación del Patrón MVC en el Gestor de Estudiantes

## ¿Qué ventajas encontraste al aplicar el patrón MVC en tu proyecto?

El patrón MVC me permitió organizar mejor el código y separar claramente las responsabilidades:
- El **modelo** maneja toda la lógica de base de datos.
- El **controlador** coordina la comunicación entre las capas.
- La **vista** gestiona la interacción con el usuario mediante el menú.

Gracias a esto, el código se volvió más mantenible, fácil de depurar y escalable.  
Por ejemplo, si quisiera cambiar la interfaz a una versión gráfica, no tendría que modificar la lógica de negocio ni las consultas SQL.

---

## ¿Qué dificultades surgieron al separar las responsabilidades entre modelo, vista y controlador?

La principal dificultad fue **entender qué debía ir en cada capa**.  
Al inicio era tentador escribir código SQL directamente en la vista o manejar impresiones desde el modelo.  
Sin embargo, al aplicar los principios SOLID, comprendí la importancia de mantener cada módulo con una sola responsabilidad.

También fue necesario ajustar las rutas de importación entre carpetas (por ejemplo, `from modelo import estudiante`) para que todo funcionara correctamente.

---

## ¿Qué aprendiste sobre la ejecución de sentencias SQL y su relación con la estructura del código?

Aprendí a usar correctamente los comandos:
- `INSERT`, `UPDATE`, `DELETE`, `ORDER BY` y `LIKE`.
- Y a integrarlos de forma controlada en funciones Python usando `sqlite3`.

Entendí cómo cada operación SQL se relaciona con una función del modelo y cómo el controlador decide cuándo ejecutarlas.  
Esto me permitió comprobar que la base de datos se modifica realmente y que los cambios son persistentes incluso al cerrar el programa.

---

## ¿Qué mejorarías si tuvieras que ampliar el sistema?

Si ampliara el proyecto, implementaría:
- Una interfaz gráfica con **Tkinter** o **PyQt**.
- Un sistema de **validación más robusto** (por ejemplo, evitar notas fuera de rango).
- Nuevas funcionalidades como exportar reportes a PDF.
- Y posiblemente integrar un **ORM (como SQLAlchemy)** para manejar la base de datos con clases en lugar de consultas SQL directas.

---
