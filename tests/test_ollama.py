from src.llm.ollama_client import OllamaClient

llm = OllamaClient().get_llm()

response = llm.invoke("What is machine learning?")

print(response)