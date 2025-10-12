from  fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app =  FastAPI()

students = {
    1: {
        "name" : "Muhammad",
        "age" : 17,
        "year" : "Year 12",
    },
    2: {
        "name" : "Adeleke",
        "age" : 12,
        "year" : "Year 6",
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None



# GET
@app.get("/")
def index():
    return {"api" : "fast api is running"}

@app.get("/students")
def index():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., description = "The student Id", gt=0, le = 2)):
    if student_id not in students:
        return {"Error" : "Student does not exits"}
    return students[student_id]

@app.get("/get-by-name")
# python does not support having an optional query parameter before a required parameter so you can add "*" to bypass it 
def get_student(*, name: str, student_id: Optional[int] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id] 
    return {"Data": "Not found"}

# POST
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error" : "Student exits"}

    students[student_id] = student

    return students[student_id]


# PUT
@app.put("students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exits"}
    
    if student.name != None:
        students[student_id]["name"] = student.name
    
    if student.age != None:
        students[student_id]["age"]= student.age

    if student.year != None:
        students[student_id]["year"] = student.year    

    return students[student_id]


# DELETE
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error" : "Student does not exits"}   
    
    del students[student_id]

    return {"message": "Student deleted successfully"}