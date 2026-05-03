from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import mysql.connector
import os

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Witaj świecie!"}