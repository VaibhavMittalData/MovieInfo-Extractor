import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

st.set_page_config(page_title="Movie Info Extractor", layout="centered")

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
Extract movie information from the paragraph.
{format_instructions}
"""),
    ("human", "{paragraph}")
])

st.title("Movie Info Extractor")

paragraph = st.text_area("Enter paragraph")

if st.button("Extract"):
    final_prompt = prompt.invoke({
        "paragraph": paragraph,
        "format_instructions": parser.get_format_instructions()
    })

    response = model.invoke(final_prompt)
    movie = parser.parse(response.content)

    st.write(movie)

st.write("Enter a paragraph and click Extract")