import os
from peewee import SqliteDatabase

# This will place the DB file at /app/data/data.db inside the container
DB_PATH = os.path.join(os.getcwd(), "data", "data.db")
db = SqliteDatabase(DB_PATH)
