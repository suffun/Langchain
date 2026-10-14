from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

schema = {
    "title": "Developer",
    "description": "Information about a software developer",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Full name of the developer"
        },
        "age": {
            "type": "integer",
            "description": "Age of the developer"
        },
        "profession": {
            "type": "string",
            "description": "Current profession of the developer"
        },
        "skills": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Programming languages and technologies the developer knows"
        },
        "education": {
            "type": "object",
            "description": "Educational background of the developer",
            "properties": {
                "degree": {
                    "type": "string"
                },
                "university": {
                    "type": "string"
                },
                "graduation_year": {
                    "type": "integer"
                }
            },
            "required": [
                "degree",
                "university",
                "graduation_year"
            ]
        },
        "experience_years": {
            "type": "integer",
            "description": "Total years of professional experience"
        },
        "github": {
            "type": ["string", "null"],
            "description": "GitHub profile URL"
        },
        "current_project": {
            "type": ["string", "null"],
            "description": "Current project of the developer"
        }
    },
    "required": [
        "name",
        "age",
        "profession",
        "skills",
        "education",
        "experience_years"
    ]
}


structured_model = model.with_structured_output(schema)


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

# python with_structured_ouput_json.py   python with_structured_output_json.py