from pathlib import Path

OPEN_AI_API_TOKEN = (Path.home() / ".ssh/openai").read_text().strip()
