import json
from datetime import datetime

GOAL_FILE = "goals.json"

# load the goals
def load_goals():
    try:
        with open(GOAL_FILE, 'r') as file:
            return json.load(file)["goals"]
    except FileNotFoundError:
        return []

# Save the goals
def save_goals(goals):
    with open(GOAL_FILE, 'w') as file:
        json.dump({"goals": goals}, file, indent=4)

# Add the goal
def add_goal(title, category="General", start_time=None, end_time=None, remind_me=False):
    goals = load_goals()
    goal = {
        "title": title,
        "category": category,
        "date": datetime.now().date().isoformat(),
        "status": "pending",
        "start_time": start_time,
        "end_time": end_time,
        "remind_me": remind_me
    }
    goals.append(goal)
    save_goals(goals)

# View the goals
def view_goals(filter_date=None):
    goals = load_goals()
    if filter_date:
        goals = [g for g in goals if g["due_date"] == filter_date]
    return goals

# Update the goal completion status
def mark_goal_complete(title):
    goals = load_goals()
    for goal in goals:
        if goal["title"].lower() == title.lower():
            goal["status"] = "complete"
            print(f"✅ Marked goal as complete: {title}")
            break
    else:
        print("❌ Goal not found.")
    save_goals(goals)

