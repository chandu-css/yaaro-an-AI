import json
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Load memory logs
def load_memory(file_path='memory/log.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("No memory data found.")
        return []

# Plot mood trends
def plot_mood_trends(logs):
    dates = []
    moods = []

    for log in logs:
        date = datetime.fromisoformat(log['timestamp']).date()
        mood = log.get('mood', 'unknown')
        dates.append(date)
        moods.append(mood)

    plt.figure(figsize=(10, 4))
    plt.plot(dates, moods, marker='o', linestyle='-', color='purple')
    plt.title("Mood Over Time")
    plt.xlabel("Date")
    plt.ylabel("Mood")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Plot most common moods
def plot_mood_distribution(logs):
    mood_counts = Counter(log.get('mood', 'unknown') for log in logs)

    plt.figure(figsize=(6, 4))
    plt.bar(mood_counts.keys(), mood_counts.values(), color='skyblue')
    plt.title("Mood Distribution")
    plt.xlabel("Mood")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()

# Main execution
if __name__ == "__main__":
    memory_logs = load_memory()

    if memory_logs:
        plot_mood_trends(memory_logs)
        plot_mood_distribution(memory_logs)
    else:
        print("No logs available for analysis.")

