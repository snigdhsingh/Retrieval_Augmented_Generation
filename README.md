# Welcome to Vector Search Applications with LLMs
Best practices culminating in a demo Retrieval Augmented Generation (RAG) application. Learn all of the components of a RAG system to include data preprocessing, embedding creation, vector database selection, indexing, retrieval systems, reranking, retrieval evaluation, question answering through an LLM and UI implementation through Streamlit.  


# Setup

1. Create a python virtual environment using your library of choice.  Here's an example using [`conda`](https://docs.conda.io/projects/miniconda/en/latest/):  
```
conda create --name impactenv -y python=3.10
```
2. Once the environment is created, activate the environment and install dependencies.
```
conda activate impactenv

pip install -r requirements.txt
```
3. Last but not least create a `.env` text file .  At a minimum, add the following environment variables:
```
OPENAI_API_KEY= "your OpenAI account API Key"
HF_TOKEN= "your HuggingFace account token"  <--- Optional: not required if using OpenAI
WEAVIATE_API_KEY= "your Weaviate cluster API Key"   <--- you will get this on Day One of the course
WEAVIATE_ENDPOINT= "your Weaviate cluster endpoint"  <--- you will get this on Day One of the course
```
4. Enjoy the process!
<img src="assets/getsome.jpg" alt="jocko" width="500" height="auto">
