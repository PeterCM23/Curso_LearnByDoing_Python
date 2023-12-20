from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)

DATABASE = 'blog.db'

# Funcion para conectar a la base de datos
def conectar_bd