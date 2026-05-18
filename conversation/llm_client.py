import os

import requests


OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434",
)
OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "gemma3:1b",
)
OLLAMA_TIMEOUT = int(
    os.getenv("OLLAMA_TIMEOUT", "60")
)


def get_llm_response(prompt: str) -> str:
    """
    Send a prompt to an Ollama model and return the response text

    Configuration is controlled through environment variables:
      - OLLAMA_HOST
      - OLLAMA_MODEL
      - OLLAMA_TIMEOUT
    """
    url = f"{OLLAMA_HOST}/api/generate"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(
        url,
        json=payload,
        timeout=OLLAMA_TIMEOUT,
    )
    response.raise_for_status()

    result = response.json()

    return result["response"].strip()