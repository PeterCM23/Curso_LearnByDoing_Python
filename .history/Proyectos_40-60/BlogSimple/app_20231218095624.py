from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3

app = Flask(__name__)