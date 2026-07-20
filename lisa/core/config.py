from dataclasses import dataclass


@dataclass
class Config:
    model: str = "ollama"
    provider: str = "ollama"
