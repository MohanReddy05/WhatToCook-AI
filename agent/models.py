from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL")

model = ChatOpenAI(
    model=model,
    api_key =api_key ,
    base_url = base_url,
    temperature = 0.7
)

# response = model.invoke("What is the capital of India?")

# print(response.content)