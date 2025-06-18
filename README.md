# 🤖 Yaaro – Your AI Friend

**Yaaro** is a personalized AI buddy that:
- Detects your emotion using your facial expression
- Initiates warm, meaningful conversations using the Phi-3 LLM
- Remembers past interactions
- Helps you track your goals
- Reminds you based on schedule and time
- Shows you mood trends with a dashboard

---

## 🛠️ Setup Instructions (Local Machine)

### 🧩 1. Prerequisites
- Python 3.10+
- 16GB RAM recommended
- A working webcam
- Git (optional, for cloning)

---

### 🚀 2. Install Ollama & Run Phi-3 Model

#### ✅ Step 2.1: Install [Ollama](https://ollama.com/download)
- Download and install for your OS (Windows, Mac, Linux)
- After install, **run this in terminal**:

```bash
ollama run phi3
```

This will:
- Download the Phi-3 model
- Start the Ollama server at `http://localhost:11434`

You must keep this running while using Yaaro.

---

### 🐍 3. Clone or Download This Project

```bash
git clone https://github.com/your-username/yaaro-an-ai.git
cd yaaro-an-ai
```

If you're not using Git, just download the ZIP from GitHub and extract it.

---

### 🔧 4. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate.bat    # Windows
```

---

### 📦 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can use this:

```txt
requests
opencv-python
deepface
schedule
matplotlib
```

---

### 🎬 6. Run the Application

Run Yaaro using:

```bash
python yaaro.py
```

- It will detect your face emotion
- Ask questions
- Remember your mood and helpful replies
- Manage goals and remind you
- Automatically check-in periodically if enabled

---

## 📁 Folder Structure

```
yaaro-an-ai/
│
├── yaaro.py              # Main chat application
├── emotion.py            # Emotion detection using webcam
├── memory.py             # Past memory saving/loading
├── goal_manager.py       # Goal creation, status tracking
├── dashboard.py          # Mood analytics with graphs
├── schedule_agent.py     # Scheduled periodic check-ins
├── data/
│   ├── memory.json
│   ├── goals.json
├── README.md
```

---

## 🧠 Features

| Feature                  | Description |
|--------------------------|-------------|
| 🤗 Emotion Detection     | Uses webcam + DeepFace to detect emotion (happy, sad, angry, etc.) |
| 💬 LLM Chat              | Sends messages to Phi-3 LLM via Ollama |
| 🧠 Memory Injection      | Remembers helpful replies and moods |
| 📅 Goal Setting          | Ask goals in the morning, remind later |
| 📈 Mood Dashboard        | Visualize your mood over time |
| ⏰ Scheduled Check-ins   | Yaaro will talk to you every few hours |

---

## ⚠️ Troubleshooting

- **Ollama not responding?**
  - Make sure you run: `ollama run phi3`
  - Or restart with: `ollama start`

- **Webcam not detected?**
  - Make sure camera permissions are granted
  - You can test using `emotion.py` standalone

- **Slow LLM response?**
  - Try reducing the `num_predict` tokens in `ask_llama()`
  - Use memory simplification to shorten prompt

---

## ✅ Future Improvements
- GUI using Streamlit or React
- Mobile App Version
- More emotion models
- Long-term memory summarization
- Better goal analytics and reminders

---

## 👨‍💻 Built With

- Python 🐍
- OpenCV + DeepFace
- Ollama + Phi-3 LLM
- Schedule + Matplotlib

---

## 📬 Contact / Feedback

If you'd like to contribute, have questions, or need help:

📧 Email: chandracsse@gmail.com  
🐙 GitHub: [your-github-profile](https://github.com/chandu-css)

---

> "Yaaro is not just an assistant – it's your friend who cares."
