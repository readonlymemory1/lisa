"""Markdown utility for Lisa."""

import re


class MarkdownFormatter:
    """Format and parse markdown content."""

    @staticmethod
    def format_code_block(code: str, language: str = "python") -> str:
        """Format code as markdown code block."""
        return f"```{language}\n{code}\n```"

    @staticmethod
    def strip_markdown(text: str) -> str:
        """Remove markdown formatting from text."""
        # Remove code blocks
        text = re.sub(r"```[\s\S]*?```", "", text)
        # Remove bold
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        # Remove italic
        text = re.sub(r"\*(.*?)\*", r"\1", text)
        # Remove links
        text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
        return text

    @staticmethod
    def is_code_block(text: str) -> bool:
        """Check if text contains code blocks."""
        return "```" in text
