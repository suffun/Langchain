
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt  

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash"
)


st.title("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
# Prompt Template
template = PromptTemplate(
    template="""
You are an expert AI research assistant.

Your task is to explain the following research paper:

Research Paper:
{paper_input}

Explanation Style:
{style_input}

Explanation Length:
{length_input}

Please provide a clear and accurate explanation of the research paper.

Follow these instructions:

1. Start with a simple introduction to the paper.
2. Explain the main problem the paper is trying to solve.
3. Explain the key idea or methodology used in the paper.
4. Explain the important results or findings.
5. Explain why this paper is important.
6. Adjust the explanation according to the selected style:
   - Beginner-Friendly: Use simple language and real-world analogies.
   - Technical: Explain technical concepts, architecture, and terminology in detail.
   - Code-Oriented: Focus on implementation ideas, pseudocode, and practical examples.
   - Mathematical: Focus on equations, mathematical intuition, and derivations.
7. Adjust the depth according to the selected length.

Do not make up information that is not supported by the paper.
""",
input_variables=["paper_input", "style_input", "length_input"]
)


if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.text)