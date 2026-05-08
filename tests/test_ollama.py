from src.llm.ollama_client import GroqClient

llm = GroqClient().get_llm()

response = llm.invoke("What is machine learning?")

print(response)