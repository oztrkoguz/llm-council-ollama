# LLM Council

![llmcouncil](header.jpg)

The idea of this repo is that instead of asking a question to a single LLM (e.g. Llama, Qwen, Mistral, Gemma, etc.), you can group them into your "LLM Council". This repo is a simple, local web app that essentially looks like ChatGPT except it uses Ollama to send your query to multiple local LLMs, it then asks them to review and rank each other's work, and finally a Chairman LLM produces the final response.

In a bit more detail, here is what happens when you submit a query:
1. **Stage 1: First opinions.** The user query is given to all LLMs individually, and the responses are collected. The individual responses are shown in a "tab view", so that the user can inspect them all one by one.
2. **Stage 2: Review.** Each individual LLM is given the responses of the other LLMs. Under the hood, the LLM identities are anonymized so that the LLM can't play favorites when judging their outputs. The LLM is asked to rank them in accuracy and insight.
3. **Stage 3: Final response.** The designated Chairman of the LLM Council takes all of the model's responses and compiles them into a single final answer that is presented to the user.

### Why Ollama?
This fork uses Ollama instead of OpenRouter, which means:
- ✅ **Completely free** - no API costs
- ✅ **100% local** - your data never leaves your machine
- ✅ **Privacy-first** - no external service dependencies
- ✅ **Offline capable** - works without internet connection
- ✅ **Fast responses** - no network latency

## Setup

### 1. Install Dependencies

The project uses [uv](https://docs.astral.sh/uv/) for project management.

**Backend:**
```bash
uv sync
```

**Frontend:**
```bash
cd frontend
npm install
cd ..
```

### 2. Configure Ollama

Make sure Ollama is installed and running on your system.

**Install Ollama:**
- Download from [ollama.ai](https://ollama.ai/)
- Or install via command line:
```bash
  # Linux/Mac
  curl -fsSL https://ollama.ai/install.sh | sh
  
  # Windows
  # Download installer from ollama.ai
```

**Pull required models:**
```bash
ollama pull phi4:latest
ollama pull qwen3:4b
ollama pull mistral:7b
```

**Start Ollama service:**
```bash
ollama serve
```

The application will connect to Ollama at `http://localhost:11434` by default.

**Note:** You can use any models available in Ollama. Just update the model names in the code to match your installed models.

### 3. Configure Models (Optional)

Edit `backend/config.py` to customize the council:

```python
COUNCIL_MODELS = [
    "qwen3:4b",
    "mistral:7b",

]

CHAIRMAN_MODEL = "phi4:latest"
```

## Running the Application

**Option 1: Use the start script**
```bash
./start.sh
```

**Option 2: Run manually**

Terminal 1 (Backend):
```bash
uv run python -m backend.main
```

Terminal 2 (Frontend):
```bash
cd frontend
npm run dev
```

Then open http://localhost:5173 in your browser.

## Tech Stack

- **Backend:** FastAPI (Python 3.10+), async httpx, OpenRouter API
- **Frontend:** React + Vite, react-markdown for rendering
- **Storage:** JSON files in `data/conversations/`
- **Package Management:** uv for Python, npm for JavaScript
