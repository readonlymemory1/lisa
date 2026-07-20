from pathlib import Path


class Memory:
    """대화 기록을 저장하는 간단한 메모리"""

    def __init__(self, storage_path: str | None = None) -> None:
        self.storage_path = Path(storage_path or "data/chats")
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def save(self, text: str) -> None:
        with self.storage_path.joinpath("conversation.txt").open("a", encoding="utf-8") as f:
            f.write(text + "\n")
