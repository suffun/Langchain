from langchain_text_splitters import CharacterTextSplitter

text = '''
Cricket is a popular sport.
It is played between two teams.
Each team has eleven players.
The objective is to score runs.
Players can bat, bowl and field
'''

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator="\n"
)
result = splitter.split_text(text)
print(result)

# python length_based.py