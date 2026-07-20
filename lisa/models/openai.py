from .base import BaseModel


class OpenAIModel(BaseModel):
    def generate(self, prompt: str) -> str:
        return f"OpenAI 응답: {prompt}"
