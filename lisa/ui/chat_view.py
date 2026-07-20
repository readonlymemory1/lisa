from textual.widgets import RichLog


class ChatView(RichLog):
    """채팅 메시지를 표시하는 영역"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.border_title = "Chat"

    def add_message(self, text: str, role: str = "user") -> None:
        prefix = "You" if role == "user" else "Lisa"
        self.write(f"[{prefix}] {text}")
