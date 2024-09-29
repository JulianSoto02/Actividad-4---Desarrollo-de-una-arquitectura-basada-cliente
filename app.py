from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)

def init_db():
    """Inicializa la base de datos SQLite y crea la tabla de tareas si no existe."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT NOT NULL,
                  completed INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    """Sirve el archivo index.html."""
    return send_from_directory('static', 'index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """API para obtener todas las tareas."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = [{'id': row[0], 'task': row[1], 'completed': bool(row[2])} for row in c.fetchall()]
    conn.close()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """API para añadir una nueva tarea."""
    task = request.json['task']
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    task_id = c.lastrowid
    conn.commit()
    conn.close()
    return jsonify({"id": task_id, "task": task, "completed": False})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """API para actualizar el estado de una tarea."""
    completed = request.json['completed']
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarea actualizada exitosamente"})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """API para eliminar una tarea."""
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarea eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True)
