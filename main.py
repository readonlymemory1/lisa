from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, RichLog, Static

class PiApp(App):

    def compose(self):

        with Horizontal():

            with Vertical():
                yield Static("채팅 목록")

            with Vertical():
                yield RichLog()
                yield Input(
                    placeholder="메시지 입력...",
                    id="order"
                )
    def on_input(self, event: Input.Submitted):
        if event.input.id == "order":
            print()


PiApp().run()
