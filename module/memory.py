import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

def save_to_memory(mood, feedback, suggestion):
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "mood": mood,
        "feedback": feedback,
        "suggestion": suggestion
    }

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            try:
                memory = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                memory = []

    memory.append(new_entry)

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=2)

# Load past memory
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            past_logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        past_logs = []
    return past_logs

def format_memory(logs):
    return "\n".join(
        [f"- Mood: {log['mood']}, Feedback: {log['feedback']}, Suggestion: {log['suggestion']}" for log in logs]
    )

# summarize the memory
def summarize_memory():
    if not os.path.exists(MEMORY_FILE):
        return "No significant past interactions yet."

    try:
        with open(MEMORY_FILE, "r") as f:
            logs = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return "No usable memory yet."

    summaries = []
    for entry in logs[-5:]:  # last 5 entries only for brevity
        mood = entry.get("mood", "unknown")
        feedback = entry.get("feedback", "").strip()
        ai_reply = entry.get("ai_reply", "").strip()
        summary = f"User felt {mood}, said: '{feedback}'. Yaaro replied: '{ai_reply}'."
        summaries.append(summary)

    return "\n".join(summaries)
