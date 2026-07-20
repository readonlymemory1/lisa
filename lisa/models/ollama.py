from .base import BaseModel


class OllamaModel(BaseModel):
    def generate(self, prompt: str) -> str:
        return f"Ollama 응답: {prompt}"
