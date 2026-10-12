from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict,Annotated,Optional

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# class Person(TypedDict):
#     name: str
#     age: int
#     profession: str
#     skills: list[str]


# structured_model = model.with_structured_output(Person)

# result = structured_model.invoke("""
# My name is Rahul Sharma. I am 23 years old and work as a
# Full Stack Developer. I mainly work with React, Node.js,
# Express, MongoDB and Java. I have been learning DSA for the
# past 6 months.
# """)

# print(result)




model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# Nested structure
class Education(TypedDict):
    degree: str
    university: str
    graduation_year: int


class Developer(TypedDict):
    name: Annotated[str, "Full name of the developer"]
    age: Annotated[int, "Age of the developer"]
    profession: Annotated[str, "Current profession"]
    
    skills: Annotated[
        list[str],
        "Programming languages and technologies the developer knows"
    ]

    education: Annotated[
        Education,
        "Educational background of the developer"
    ]

    experience_years: Annotated[
        int,
        "Total years of professional experience"
    ]

    github: Optional[
        Annotated[str, "GitHub profile URL"]
    ]

    current_project: Optional[
        Annotated[str, "Project the developer is currently working on"]
    ]

structured_model = model.with_structured_output(Developer)

result = structured_model.invoke("""
Rahul Sharma is a 24-year-old software developer.

He currently works as a Full Stack Developer and has 2 years
of professional experience.

His main skills are JavaScript, React, Node.js, Express,
MongoDB and Java.

He completed his B.Tech in Computer Science from Pune University
in 2023.

He is currently working on an AI-powered resume analyzer.

He does not have a GitHub account.
""")
structured_model = model.with_structured_output(Developer)

print(result)

# python with_structured_output_typeddict.py