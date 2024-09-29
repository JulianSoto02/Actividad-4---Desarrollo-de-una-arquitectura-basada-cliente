Explicación:

Servidor (app.py):


Utiliza Flask para crear un servidor web en Python.
Implementa una API RESTful con las siguientes rutas:

- GET /api/tasks: Obtiene todas las tareas.
- POST /api/tasks: Añade una nueva tarea.
- PUT /api/tasks/`<id>`: Actualiza el estado de una tarea.
- DELETE /api/tasks/`<id>`: Elimina una tarea.

Utiliza SQLite para almacenar las tareas con un campo adicional para el estado de completado.

Cliente (index.html):

Implementa una Single Page Application (SPA) utilizando JavaScript puro.
Mantiene un estado local de las tareas y se sincroniza con el servidor.
Funciones principales:

- renderTasks(): Actualiza la interfaz de usuario basada en el estado local.
- fetchTasks(): Obtiene las tareas del servidor y actualiza el estado local.
- addTask(): Añade una nueva tarea al servidor y al estado local.
- toggleTask(): Cambia el estado de completado de una tarea.
- deleteTask(): Elimina una tarea del servidor y del estado local.

Montaje y herramientas utilizadas:

Montaje:
a. Preparación del entorno:

- Instalar Python (versión 3.7 o superior).
- Crear un entorno virtual: `python -m venv venv`
- Activar el entorno virtual.
b. Instalación de dependencias:
- Instalar Flask: `pip install flask`
c. Estructura del proyecto:

todo_app/
├── app.py
├── tasks.db
└── static/
    └── index.html


d. Ejecución:

- Ejecutar `python app.py`
- Acceder a `http://localhost:5000` en el navegador.

Herramientas utilizadas:

- Python con Flask: Para el backend y la API.
- SQLite: Para la persistencia de datos.
- HTML, CSS, y JavaScript: Para la interfaz de usuario y la lógica del cliente.
- Fetch API: Para la comunicación asíncrona con el servidor.

Aplicación y objetivo del ejercicio:

1. Aplicación:

1. Lista de tareas interactiva con operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
2. Interfaz de usuario dinámica que se actualiza sin recargar la página.

2 Objetivo del ejercicio:

a. Demostrar una arquitectura basada en el cliente:

- La lógica de la aplicación se ejecuta principalmente en el navegador.
- El servidor actúa como una API para operaciones de datos.
b. Ilustrar los principios de una Single Page Application (SPA):
- Actualización dinámica de la interfaz sin recargas de página.
- Gestión del estado de la aplicación en el cliente.
c. Mostrar la interacción entre el frontend y el backend:
- Uso de API RESTful para la comunicación.
- Manejo de operaciones asíncronas en el cliente.
d. Introducir conceptos de desarrollo web moderno:
- Separación de preocupaciones entre cliente y servidor.
- Manipulación dinámica del DOM.
- Gestión de estado en el cliente.

Ventajas de usar la arquitectura propuesta:

1. Mejor experiencia de usuario: Las interacciones son más rápidas y fluidas.
2. Reducción de carga en el servidor: La lógica de presentación se ejecuta en el cliente.
3. Flexibilidad: Facilita la implementación de nuevas características en el frontend.
4. Escalabilidad: Permite escalar el backend y frontend de forma independiente.
5. Offline capabilities: Potencial para funcionar offline con almacenamiento local.
