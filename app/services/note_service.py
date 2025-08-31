import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3:8b")

def generate_summary(text: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"Summarize the following note in 1-2 sentences: {text}. Don't place any new-line symbols.",
        "stream": False
    }
    try:
        response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        return f"Summary failed: {str(e)}"
