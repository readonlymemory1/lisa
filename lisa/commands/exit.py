"""Exit command for Lisa."""


class ExitCommand:
    """Exits the application."""

    def __init__(self):
        self.name = "exit"
        self.description = "Exit the application"

    def execute(self):
        """Execute exit command."""
        return "exit"
