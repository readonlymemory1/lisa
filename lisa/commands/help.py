"""Help command for Lisa."""


class HelpCommand:
    """Displays help information."""

    def __init__(self):
        self.name = "help"
        self.description = "Show help information"

    def execute(self):
        """Execute help command."""
        help_text = """
        Available Commands:
        - /help    : Show this help message
        - /clear   : Clear chat history
        - /exit    : Exit the application
        """
        return help_text
