from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import mysql.connector
import os

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    
@app.get("/api/lizards")
def get_lizards():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM lizards")
    return cursor.fetchall()

@app.get("/")
def home():
    return{"message":"Witaj świecie!"}