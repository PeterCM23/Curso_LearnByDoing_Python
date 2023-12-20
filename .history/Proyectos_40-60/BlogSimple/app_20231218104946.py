from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)

DATABASE = 'blog.db'

# Funcion para conectar a la base de datos

def conectar_bd():
    return sqlite3.connect(DATABASE)

# Crear la tabla si no existe

def crear_tabla():
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS publicaciones(
                           id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           titulo TEXT NOT NULL,
                           contenido TEXT NOT NULL
                       )
                       ''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS comentarios(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           publicacion_id INTEGER NOT NULL,
                           contenido TEXT NOT NULL,
                           FOREIGN KEY (publicacion_id) REFERENCES publicaciones (id)
                       )
                       ''')
        conexion.commit()
        
# Ruta para ver las publicaciones

@app.route('/')
def ver_publicaciones():
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM publicaciones ORDER BY id DESC')
        publicaciones = cursor.fetchall()
        return render_template('index.html', publicaciones=publicaciones)
    
# Ruta para ver los detalles de una publicacion

@app.route('/publicacion/<int:publicacion_id>')
def ver_publicacion(publicacion_id):
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM publicaciones WHERE id = ?', (publicacion_id,))
        publicacion = cursor.fetchone()
        
        cursor.execute('SELECT * FROM publicacion_id = ? ORDER BY id', (publicacion_id))
        comentarios = cursor.fetchall()
        
    return render_template('publicacion.html', publicacion=publicacion, comentarios=comentarios)

# Ruta para agregar una nueva publicacion

@app.route('/nueva_publicacion', methods=['GET', 'POST'])
def nueva_publicacion():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        
        with conectar_bd() as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO publicaciones (titulo, contenido) VALUES (?,?)', (titulo, contenido))
            conexion.commit()
        
        return redirect(url_for('ver_publicaciones'))
    return render_template('nueva_publicacion.html')

# Ruta para agregar un comentario a una publicacion
@app.route('/publicacion/<int:publicacion_id>/nuevo_comentario', methods=['POST'])
def nuevo_comentario(publicacion_id):
    contenido = request.form['contenido']
    
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO comentarios (publicacion_id, contenido) VALUES (?,?)', (publicacion_id, contenido))
        conexion.commit()
        
    return redirect(url_for('ver_publicacion', publicacion))
            
        