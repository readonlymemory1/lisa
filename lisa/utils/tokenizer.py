"""Tokenizer utility for Lisa."""


class Tokenizer:
    """Simple tokenizer for text processing."""

    @staticmethod
    def count_tokens(text: str) -> int:
        """Estimate token count (simplified)."""
        # Simple estimation: split by spaces
        return len(text.split())

    @staticmethod
    def truncate_text(text: str, max_tokens: int) -> str:
        """Truncate text to max tokens."""
        tokens = text.split()
        if len(tokens) <= max_tokens:
            return text
        return " ".join(tokens[:max_tokens])
