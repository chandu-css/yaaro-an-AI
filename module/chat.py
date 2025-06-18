import requests

# method to start prompt
conversation = []
def ask_llama(prompt):
    conversation.append({"role": "user", "content": prompt})

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "phi3",
                "messages": conversation,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 80
                }
            }
        )

        if response.status_code != 200:
            return "Sorry, I couldn't get a response."

        reply = response.json()['message']['content']
        conversation.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        return "Oops! Something went wrong while contacting the AI."
