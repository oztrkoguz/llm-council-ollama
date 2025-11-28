"""Configuration for the LLM Council."""
import os
from dotenv import load_dotenv

load_dotenv()

# Ollama API endpoint (local)
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/chat")

# Council members - list of Ollama model identifiers
COUNCIL_MODELS = [
    "qwen3:4b",
    "mistral:7b",

]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "phi4:latest"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
