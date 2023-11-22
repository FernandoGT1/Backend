from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Se define el CORs origins
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplázalo con la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Ruta GET
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to FastAPI!"}


todos = [
    {"id": "1", "item": "Read Stephen King's Duma Key!"},
    {"id": "2", "item": "Go for shopping"},
    {"id": "3", "item": "Work out"},
    {"id": "4", "item": "Cook dinner"}
]

@app.get("/Todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.post("/Todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data":{"Todo se ha agregado algo!"}
    }

@app.put("/Todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {"data": f"Todo with id {id} has been updated!"}

    return {"data": f"Todo with this {id} number has not been found!"}


# Delete Route
@app.delete("/Todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {"data": f"Todo with id {id} is removed!"}

    return {"data": f"Todo with id {id} is not found!"}
