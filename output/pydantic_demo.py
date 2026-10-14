from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel) :
    name : str = 'sufiyan khan'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 3, lt =10 )

new_student = {'name' : 'sufiyan','age':69,'email' :'1@gmail.com','cgpa':8.7}

student = Student(**new_student)
student_dict = dict(student)
print(student_dict)
student_json = student.model_dump_json()
print(student_json)

# python pydantic_demo.py