import os
from langchain_groq import ChatGroq

class ChatGroqLLM:
    def __init__(self, model_name: str = "mixtral-8x7b-32768", temperature: float = 0.7):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set in environment variables.")
        self.model_name = model_name
        self.temperature = temperature
        self.client = ChatGroq(model=self.model_name, temperature=self.temperature, groq_api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.client.invoke(prompt)
            return response.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return ""
