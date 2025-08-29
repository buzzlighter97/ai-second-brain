import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:8b")

def response_on_prompt(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": {prompt},
        "stream": False
    }
    try:
        response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        return f"Prompt result failed: {str(e)}"
