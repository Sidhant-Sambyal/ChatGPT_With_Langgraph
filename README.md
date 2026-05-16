# ChatGPT_With_Langgraph
Building a conversational AI chatbot using LangGraph to explore stateful workflows, multi-step reasoning, and agent orchestration. The project is focusing on learning how LLM-powered applications manage conversation state, routing, memory, and tool execution using graph-based architectures. Implementing modular nodes, conditional edges, and structured state management to create a scalable and maintainable chatbot workflow.

## Project Structure

```text
backend/
  backend.py      LangGraph state, chat node, checkpointer, and compiled graph

frontend/
  frontend.py     Streamlit chat interface with conversation switching

common/
  utils.py        Thread ID generation and Streamlit session helpers

requirements.txt Python dependencies
.env             Local environment variables
```

## What Has Been Implemented

- Added Streamlit session state for `message_history`, the active `thread_id`, and the list of `chat_threads`.
- Added UUID-based thread creation so every new chat gets its own LangGraph thread.
- Added a sidebar conversation list under `My Conversations`.
- Added `New Chat` support, which creates a fresh thread and clears the current chat window.
- Fixed the sidebar display so each conversation button shows its own thread ID instead of repeating the active thread ID.
- Added conversation loading from LangGraph state when a sidebar thread is clicked.
- Added empty-thread handling so clicking a thread with no saved messages opens a blank chat instead of raising an error.

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
python run.py
```

Then open the local URL shown by Streamlit in your browser.

## Notes

- The backend uses `InMemorySaver`, so conversation state is not persisted after the Python process stops.
- The frontend now creates a unique LangGraph `thread_id` for each new chat and keeps the thread list in Streamlit session state.
- Empty threads are valid. If a thread has no `messages` in LangGraph state yet, the frontend loads it as an empty conversation.
- Keep `.env` out of version control because it contains local secrets.
