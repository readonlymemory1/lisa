from dataclasses import dataclass


@dataclass
class Config:
    model: str = "gemma3:4b"
    provider: str = "ollama"
    base_url: str = "http://127.0.0.1:11434"
