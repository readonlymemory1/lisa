from abc import ABC, abstractmethod


class BaseModel(ABC):
    """모든 모델 구현체가 따라야 할 기본 인터페이스"""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
