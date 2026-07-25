import json
import os
from urllib import error, request

from .base import BaseModel


class OllamaModel(BaseModel):
    def __init__(self, base_url: str | None = None, model: str | None = None) -> None:
        self.base_url = (base_url or os.getenv("OLLAMA_BASE_URL") or "http://127.0.0.1:11434").rstrip("/")
        self.model = model or os.getenv("OLLAMA_MODEL") or "llama3.2"

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        req = request.Request(
            f"{self.base_url}/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with request.urlopen(req, timeout=15) as response:
                data = json.load(response)
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"Ollama 모델 호출이 실패했습니다: {detail}") from exc
        except error.URLError as exc:
            raise RuntimeError(f"Ollama 서버에 연결할 수 없습니다: {exc.reason}") from exc
        except json.JSONDecodeError as exc:
            raise RuntimeError("Ollama 응답 형식이 올바르지 않습니다.") from exc

        response_text = (data.get("response") or "").strip()
        if not response_text:
            raise RuntimeError("Ollama로부터 빈 응답을 받았습니다.")
        return response_text
