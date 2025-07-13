from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import uvicorn
from pydantic import BaseModel
from pathlib import Path
from data_cleaning import DataCleaning

app = FastAPI()

class InitData(BaseModel):
    data_file: str
    target_column: str



@app.get("/")
def load_data():
    return {"message": " uvicorn"}

list_users = []

class User(BaseModel):
    username: str
    age: int

@app.post("/user")
def add_user(user: User):
    list_users.append(user)
    return {"message": f"User {user.username} added successfully!"}


@app.get("/user")
def print_users():
    return  list_users

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
