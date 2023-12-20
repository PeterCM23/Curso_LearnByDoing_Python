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
                           FOREIGN KEY (publicacion)
                       ))