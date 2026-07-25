from lisa.models.ollama import OllamaModel


class Chatbot:
    """Ollama 기반 챗봇 인터페이스"""

    def __init__(self, model: str = "default") -> None:
        self.model = model
        self._model_backend = OllamaModel(model=model if model != "default" else None)

    def respond(self, message: str) -> str:
        try:
            return self._model_backend.generate(message)
        except Exception as exc:  # pragma: no cover - UI 안전장치
            return f"Ollama 연결 오류: {exc}"
