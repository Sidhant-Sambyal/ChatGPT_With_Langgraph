# ChatGPT_With_Langgraph
Building a conversational AI chatbot using LangGraph to explore stateful workflows, multi-step reasoning, and agent orchestration. The project is focusing on learning how LLM-powered applications manage conversation state, routing, memory, and tool execution using graph-based architectures. Implementing modular nodes, conditional edges, and structured state management to create a scalable and maintainable chatbot workflow.

## Project Structure

```text
backend/
  backend.py      LangGraph state, chat node, checkpointer, and compiled graph

frontend/
  frontend.py     Streamlit chat interface

requirements.txt Python dependencies
.env             Local environment variables
```

## Requirements

- Python 3.11+
- A Gemini API key from Google AI Studio

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Add your Gemini API key to `.env`:

```env
GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

## Run

Start the Streamlit app from the project root:

```powershell
streamlit run frontend/frontend.py
```

Then open the local URL shown by Streamlit in your browser.

## Notes

- The backend uses `InMemorySaver`, so conversation state is not persisted after the Python process stops.
- The current frontend uses a fixed LangGraph `thread_id`, which is fine for local learning but should be changed before using the app with multiple users.
- Keep `.env` out of version control because it contains local secrets.
