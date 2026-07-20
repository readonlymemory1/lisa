class Chatbot:
    """AI 챗봇 인터페이스의 기본 틀"""

    def __init__(self, model: str = "default") -> None:
        self.model = model

    def respond(self, message: str) -> str:
        return f"[{self.model}] {message}에 대한 답변"
