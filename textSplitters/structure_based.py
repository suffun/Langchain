from langchain_text_splitters import RecursiveCharacterTextSplitter

text = '''
Cricket is a popular sport.
It is played between two teams.

Each team has eleven players.
The objective is to score runs.
Players can bat, bowl and field
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)
result = splitter.split_text(text)
print(result)

# python structure_based.py