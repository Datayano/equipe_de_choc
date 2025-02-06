# agent_logic/deepseek_llm.py
import requests
from config import OLLAMA_API_URL

# Simule la classe OllamaFunctions
class OllamaFunctions:
    def __init__(self, model: str, format: str = "json"):
        self.model = model
        self.format = format
        self.tools = []
    
    def bind_tools(self, tools):
        self.tools = tools
    
    def generate(self, prompt: str):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "format": self.format
        }
        url = f"{OLLAMA_API_URL}/v1/chat/completions"
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Error from Ollama: {response.text}")
        result = response.json()
        # On suppose que la réponse est de la forme {"choices": [{"message": {"content": "..."}}]}
        return result["choices"][0]["message"]["content"]

class DeepSeekLLM:
    def __init__(self, model: str, format: str = "json"):
        self.llm = OllamaFunctions(model=model, format=format)
    
    def bind_tools(self, tools):
        self.llm.bind_tools(tools)
        return self
    
    def with_structured_output(self, output_cls, include_raw: bool = True):
        # Pour simplifier, nous ne traitons pas ici la sortie structurée
        return self
    
    def generate(self, prompt: str) -> str:
        return self.llm.generate(prompt)
