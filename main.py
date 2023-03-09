import shemas
import database

from fastapi import FastAPI
from database import engine, Base, ToDo
from sqlalchemy.orm import Session
from fastapi_versioning import VersionedFastAPI, version

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
@version(1)

async def root():
    return {"TODO APP"}

# ADD TODO
@app.post("/add_todo")
@version(1)

async def add_todo(todo: shemas.ToDo):
    session = Session(bind=engine, expire_on_commit = False)
    todoDB = ToDo(title = todo.title, description = todo.description)
    session.add(todoDB)
    session.commit()
    id = todoDB.id
    session.close()
    return f"TODO ADDED with id: {id}"

# GET TODO by ID
@app.get("/get_todo/{id}")
@version(1)

async def get_todo(id: int):
    session = Session(bind=engine, expire_on_commit = False)
    todo_note = session.query(ToDo).filter(ToDo.id == id).first()
    session.close()

    return todo_note

# UPDATE TODO by ID 
@app.put(f"/update_todo/{id}")
@version(1)

async def update_todo(id: int):
    session = Session(bind=engine, expire_on_commit = False)
    todo_note = session.query(ToDo).filter(ToDo.id == id).first()
    if todo_note:
        todo_note.task = task
        session.commit()
    session.close()
    
    return {"TODO UPDATED"}

# DELETE TODO by ID
@app.delete(f"/delete_todo/{id}")
@version(1)

async def delete_todo(id: int):
    return {"TODO DELETED"}

# LIST ALL TODO
@app.get("/list_todo")
@version(1)

async def list_todo():
    return {"TODO LIST"}

app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}')    