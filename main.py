# A fastAPI project for a student
from fastapi import FastAPI
from uuid import UUID


app = FastAPI()


student_clone = {
    "id": 0,
    "Name": "",
    "Age": 0,
    "Sex": "",
    "Height": 0.0
}

# Inmemory Storage
students: dict = {}

# Home page


@app.get("/")
def home():
    return "Welcome To The Student Resource"


# Get all student
@app.get("/students")
def get_all_students():
    return {"message": "All Students", "data": students}


# Create a student
@app.post("/students")
def create_student(Name: str, Age: int, Sex: str, Height: float):
    new_student = student_clone.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["Name"] = Name
    new_student["Age"] = Age
    new_student["Sex"] = Sex
    new_student["Height"] = Height
    students[new_student["id"]] = new_student
    return {"message": "Student Created Successfully", "data": new_student}


# Get a single student
@app.get("/students/{id}")
def get_student(id: str):
    if id in students:
        single_student = students.get(id)
        return single_student
    else:
        return "Sorry, Student Not Found"


# Update student
@app.put("/students/{id}")
def update_student(id: str, Name: str, Age: int, Sex: str, Height: float):
    student = students.get(id)
    if student:
        student["Name"] = Name
        student["Age"] = Age
        student["Sex"] = Sex
        student["Height"] = Height
        return {"message": "Student updated successfully", "data": student}
    else:
        return {"Update failed, Student Not Found"}


# Delete student
@app.delete("/students/{id}")
def delete_student(id: str):
    student = students.get(id)
    if student:
        del students[id]
        return "Student Deleted Successfully"
    else:
        return "Unsuccessful"
