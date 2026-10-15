from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)
schema = [
    ResponseSchema(name ='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name ='fact_2',description='fact 2 about the topic'),
    ResponseSchema(name ='fact_3',description='fact 3 about the topic')
    
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give three fact about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic' : 'black hole'})
print(result)

# prompt = template.invoke({'topic':'black hole'})
# result =model.invoke(prompt)
# final = parser.parse(result.text)

# print(final)

# python structuredoutputparser.py 