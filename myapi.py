from  fastapi import FastAPI, Path

app =  FastAPI()

students = {
    1: {
        "name" : "Muhammad",
        "age" : 17,
        "class" : "Year 12",
    },
    2: {
        "name" : "Adeleke",
        "age" : 12,
        "class" : "Year 6",
    }
}

@app.get("/")
def index():
    return {"api" : "fast api is running"}

@app.get("/students")
def index():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., description = "The student Id", gt=0, le = 2)):
    return students[student_id]




