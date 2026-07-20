class Session:
    """현재 세션 상태를 관리"""

    def __init__(self) -> None:
        self.history: list[str] = []

    def add_message(self, message: str) -> None:
        self.history.append(message)
