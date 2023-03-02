import shemas
import database

from fastapi import FastAPI
from database import engine, Base, ToDo
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")

async def root():
    return {"TODO APP"}

# ADD TODO
@app.post("/add_todo")

async def add_todo(todo: shemas.ToDo):
    session = Session(bind=engine, expire_on_commit = False)()
    todoDB = ToDo(title = todo.title, description = todo.description)
    session.add(todoDB)
    session.commit()
    id = todoDB.id
    session.close()
    return {"TODO ADDED with id: {id}"}

# GET TODO by ID
@app.get("/get_todo/{id}")

async def get_todo(id: int):
    return {"TODO LIST"}

# UPDATE TODO by ID
@app.put("/update_todo/{id}")

async def update_todo(id: int):
    return {"TODO UPDATED"}

# DELETE TODO by ID
@app.delete("/delete_todo/{id}")

async def delete_todo(id: int):
    return {"TODO DELETED"}

# LIST ALL TODO
@app.get("/list_todo")

async def list_todo():
    return {"TODO LIST"}
