#import subprocess
import schedule
import time
from datetime import datetime
from module.memory import save_to_memory, summarize_memory
from module.voice import speak
from module.emotion import detect_emotion
from module.chat import ask_llama
from module.goal_manager import add_goal, view_goals, mark_goal_complete

## identify the situation based on time
def get_time():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"

# Check the goal and update its status
def toadys_goal_sttus():
    now_str = datetime.now().strftime('%H:%M')

    today_goals = view_goals(datetime.now().date().isoformat())
    pending = [
        g for g in today_goals
        if g["status"] == "pending" and g.get("end_time") and g["end_time"] <= now_str and g.get("remind_me")
    ]

    if pending:
        print("\n⏰ It's time to check your goals:")
        for g in pending:
            print(f"⬜ {g['title']} (Due: {g['end_time']})")

        done_goal = input("Have you completed any of these? (type the title or 'no'): ").strip()
        if done_goal.lower() != "no": # this has improv bit more logical
            mark_goal_complete(done_goal)

# start the conversation
def start_conversation():
    global conversation_in_progress

    time_of_day = get_time()
    conversation_in_progress = True
    # Step 1: Detect Emotion
    emotion = detect_emotion()

    # Step 2.0: get days goal
    if time_of_day == 'morning':
        set_goal = input("\nGood morning! Would you like to set a goal for today? (yes/no): ").strip().lower()
        if set_goal == "yes":
            goal_title = input("What's your goal?: ").strip()
            goal_category = input("Category (optional): ").strip() or "General"
            start_time = input("When will you start? (HH:MM): ").strip()
            end_time = input("When is it due? (HH:MM): ").strip()
            remind_me = input("Would you like a reminder later? (yes/no): ").strip().lower() == "yes"
            add_goal(goal_title, goal_category, start_time, end_time, remind_me)

    # Step 2.1: load past memory if any
    memory_prompt = summarize_memory()

    # Step 3: Prepare system prompt
    opening_prompt = f"""You are a very supportive AI friend named Yaaro.
    The person in front of you looks {emotion} and it is currently {time_of_day}. 
    Start a warm conversation to help the user feel better, be productive, and enjoy their day ahead.
    Here are pst memories: {memory_prompt if memory_prompt else '-no past memory yet.'}
    Respond briefly in 1-2 sentence unless it is required in technical aspects."""

    # Step 4: Start conversation
    response = ask_llama(opening_prompt)
    speak(response)
    last_ai_reply = response  # keep updating the last AI message

    place_context = None
    interaction_count = 0
    # Step 5: Continue Conversation
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['exit', 'quit', 'bye', 'done']:
            if time_of_day == 'night':
                toadys_goal_sttus()

            mood_now = input("How do you feel now?: ")
            feedback = input("What helped you most?: ")
            save_to_memory(mood_now, feedback, last_ai_reply)
            speak("Goodbye! Take care 😊")
            break

        # Ask for place naturally once
        interaction_count += 1
        if interaction_count == 2 and not place_context:
            place_context = input("Can I ask — are you at work, home, or somewhere else? ").strip().lower()

        # Add place context if known
        prompt = user_input
        if place_context:
            prompt += f"\n(Note: The user is currently at {place_context}.)"
            
        response = ask_llama(prompt)
        speak(response)
        last_ai_reply = response  # keep updating the last AI message

    conversation_in_progress = False

def main():
    start_conversation()
    # --- 📅 Scheduling block: place this at the bottom of your script ---
    # schedule.every(3).hours.do(start_conversation)
    # Use this for testing (e.g. once a minute)
    schedule.every(1).minutes.do(start_conversation)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()