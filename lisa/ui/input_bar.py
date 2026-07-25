from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Input


class InputBar(Horizontal):
    """메시지 입력창과 전송 버튼"""

    def compose(self) -> ComposeResult:
        self.message_input = Input(placeholder="메시지를 입력하세요", id="message_input")
        self.send_button = Button("전송", id="send_button")
        yield self.message_input
        yield self.send_button

    def get_message(self) -> str:
        return self.message_input.value.strip()

    def clear(self) -> None:
        self.message_input.value = ""
