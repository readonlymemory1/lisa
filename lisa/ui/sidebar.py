from textual.widgets import ListItem, ListView, Static


class Sidebar(ListView):
    """대화 목록을 보여주는 사이드바"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.border_title = "Conversations"

    def build_items(self) -> None:
        self.clear()
        self.append(ListItem(Static("새 대화")))
