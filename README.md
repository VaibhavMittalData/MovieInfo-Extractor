🎬 Movie Information Extractor (Generative AI)
📌 Overview

This project is a Movie Information Extractor built using Generative AI, designed to transform unstructured movie-related text into structured data. It leverages Large Language Models (LLMs) to automatically extract key details such as movie title, genre, cast, rating, and summary.

The project demonstrates practical application of AI/ML concepts, focusing on prompt engineering, structured output parsing, and real-time AI integration.

🚀 Features

🔍 Extracts structured information from unstructured text

🎭 Identifies:

Title

Genre

Cast

Rating

Summary

⚡ Real-time processing using LLMs

🧠 Uses prompt engineering for accurate extraction

📊 Structured output using Pydantic models

🌐 Interactive UI built with Streamlit

🛠️ Tech Stack

Python

LangChain

Groq API (LLaMA-3.3-70B model)

Pydantic (for data validation & parsing)

Streamlit (for UI)

⚙️ How It Works

User inputs unstructured movie text (e.g., description, review, or paragraph)

A carefully designed prompt is sent to the LLM via LangChain

The model processes the text and extracts relevant fields

Output is structured using a Pydantic schema

Results are displayed in a clean UI using Streamlit
