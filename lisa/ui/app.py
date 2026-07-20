from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header

from .chat_view import ChatView
from .input_bar import InputBar
from .sidebar import Sidebar


class LisaApp(App):
    """Textual 기반 Lisa 채팅 앱"""

    CSS_PATH = "theme.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Sidebar()
            with Vertical():
                yield ChatView()
                yield InputBar()
        yield Footer()
