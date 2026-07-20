from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input, Button


class InputBar(Horizontal):
    """메시지 입력창과 전송 버튼"""

    def compose(self) -> ComposeResult:
        yield Input(placeholder="메시지를 입력하세요", id="message_input")
        yield Button("전송", id="send_button")
