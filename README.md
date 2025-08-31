# AI Second Brain

ИИ-ассистент, автоматически резюмирующий заметки.
Стек: FastAPI, Celery, PostgreSQL, Redis и интеграцией LLaMA 3 через Ollama. 

## Установка

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Установка Ollama и LLaMA 3

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3:8b
ollama run llama3:8b
```

### 3. Запуск приложения

```bash
uvicorn app.main:app --reload
```

### 4. Установка и запуск Redis

**Redis требуется для работы очереди Celery.**

#### ▶️ A. Локальный запуск на Linux/macOS

Установка Redis:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install redis

# macOS (Homebrew)
brew install redis
```

Запуск Redis сервер:

```bash
redis-server
```

Проверка соединения:

```bash
redis-cli ping
# → PONG
```

#### 🐳 B. Через Docker (удобно для Windows)

Если уже установлен Docker Desktop:

```bash
docker run -d --name redis -p 6379:6379 redis
```

Проверка связи:

```bash
docker exec -it redis redis-cli ping
# → PONG
```

> Переменная `CELERY_BROKER_URL` в окружении должна указывать на `redis://localhost:6379/0`, если Redis работает на локальной машине и порт проброшен.

### 5. Запуск Celery worker

```bash
celery -A app.tasks.scheduler.celery_app worker --loglevel=info
```

## Пример запроса

POST /api/summarize

```json
{
  "text": "Despite growing tensions within the interdisciplinary research team, the final draft of the synthetic neurointerface proposal was completed ahead of schedule. The document outlines an ambitious integration of quantum computing principles with neural pattern recognition systems, aimed at enhancing real-time brain-computer communication for medical and defense applications. Several ethical concerns were raised during the final review process—most notably regarding the potential for cognitive manipulation and surveillance. However, the lead researcher argued that with sufficient regulatory oversight and transparency, the technology could revolutionize cognitive prosthetics and remote neural diagnostics. Pending approval by the international bioethics council, the team plans to initiate Phase 1 clinical trials by Q2 of next year."
}

```

## Ответ

```json
{
  "summary": "Summary: A research team completed a proposal to merge quantum computing with neural interfaces, aiming to improve brain-computer communication. Ethical concerns were raised, but the team plans clinical trials next year pending approval."
}
```
## ВАЖНО! В силу ограничений llama3 приложение работает только на английском языке!

## Настройки через `.env`

```ini
OLLAMA_MODEL=llama3:8b
OLLAMA_URL=http://localhost:11434
```
