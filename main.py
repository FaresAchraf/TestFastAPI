from fastapi import FastAPI, Path
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {
        "name": "achraf",
        "Age": "23"
    }
}

class Student(BaseModel):
    name:str
    Age:int


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/square')
async def square(num: int):
    result = num ** 2
    return {"square": result}

@app.get('/students/{index}')
async def get_student(index: int=Path(None,description="get one student Info",gt=0,lt=2)):
    return students[index]


@app.post('/create_student/{student_id}')
def create_student(student_id:int, student:Student):
    if student_id in students :
       return {"Error":"student exists"}

    students[student_id] = student
    return students[student_id]


