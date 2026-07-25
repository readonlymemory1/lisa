from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Input

from ..core.chatbot import Chatbot
from ..core.config import Config
from .chat_view import ChatView
from .input_bar import InputBar
from .sidebar import Sidebar


class LisaApp(App):
    """Textual 기반 Lisa 채팅 앱"""

    CSS_PATH = "theme.tcss"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config = Config()
        self.chatbot = Chatbot(model=self.config.model)

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Sidebar()
            with Vertical():
                self.chat_view = ChatView()
                yield self.chat_view
                self.input_bar = InputBar()
                yield self.input_bar
        yield Footer()

    def on_mount(self) -> None:
        self.chat_view.add_message("Lisa가 Ollama에 연결 준비를 마쳤습니다. 메시지를 입력해 보세요.", role="assistant")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "send_button":
            self._submit_message()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "message_input":
            self._submit_message()

    def _submit_message(self) -> None:
        message = self.input_bar.get_message()
        if not message:
            return

        self.chat_view.add_message(message, role="user")
        self.input_bar.clear()
        response = self.chatbot.respond(message)
        self.chat_view.add_message(response, role="assistant")
