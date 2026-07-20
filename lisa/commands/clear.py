"""Clear command for Lisa."""


class ClearCommand:
    """Clears chat history."""

    def __init__(self):
        self.name = "clear"
        self.description = "Clear chat history"

    def execute(self, session):
        """Execute clear command."""
        session.clear()
        return "Chat history cleared."
