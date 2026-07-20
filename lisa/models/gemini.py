from .base import BaseModel


class GeminiModel(BaseModel):
    def generate(self, prompt: str) -> str:
        return f"Gemini 응답: {prompt}"
