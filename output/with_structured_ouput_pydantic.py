from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


# Nested structure
class Education(BaseModel):
    degree: str = Field(description="Degree completed by the developer")
    university: str = Field(description="University where the developer studied")
    graduation_year: int = Field(description="Year the developer graduated")


class Developer(BaseModel):
    name: str = Field(description="Full name of the developer")
    age: int = Field(description="Age of the developer")
    profession: str = Field(description="Current profession of the developer")

    skills: list[str] = Field(
        description="Programming languages and technologies the developer knows"
    )

    education: Education = Field(
        description="Educational background of the developer"
    )

    experience_years: int = Field(
        description="Total years of professional experience"
    )

    github: Optional[str] = Field(
        default=None,
        description="GitHub profile URL"
    )

    current_project: Optional[str] = Field(
        default=None,
        description="Project the developer is currently working on"
    )


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


print(result)

# python with_structured_ouput_pydantic.py