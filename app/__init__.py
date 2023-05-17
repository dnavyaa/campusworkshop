"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi85el269vf5qbest50-a.oregon-postgres.render.com",
        database="todo_gguq",
        user="root",
        password="xyk9mRUPOh8m3jnJTZ6ZsRKdJY6fcKH2")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
