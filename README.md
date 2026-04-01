# 📖 AI Story Weaver

**AI-powered collaborative storytelling app** built with Streamlit and OpenAI. Users can write stories together with AI, maintain story consistency, explore branching choices, and adjust creativity.

---

## ⚡ Features

* Start a story with a **title, genre, and hook**
* AI continues the story with vivid, consistent narrative
* **Add your own sentences** anywhere in the story
* **Branching choices** to explore multiple story paths
* **Undo last AI/User input**
* **Creativity slider** to control AI imagination
* Clean and intuitive **Streamlit UI**

---

## 🛠️ Tech Stack

* **Python 3.14+**
* **Streamlit** – Frontend UI
* **OpenAI 1.x API** – LLM backend
* **dotenv** – Load API keys securely

---

## 📂 Project Structure

```text
ai-story-weaver/
├── app.py            # Streamlit UI
├── engine.py         # AI engine handling story memory & prompts
├── requirements.txt  # Python dependencies
├── .env              # Your OpenAI API key
└── README.md         # This file
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd ai-story-weaver
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows PowerShell: venv\Scripts\Activate.ps1
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API key**

Create a `.env` file (or copy `.env.example`) and add:

```env
OPENAI_API_KEY=sk-your-openai-key
```

5. **Run the app**

```bash
streamlit run app.py
```

Open the URL printed by Streamlit (usually `http://localhost:8501`).

---

## 💡 Usage

1. Enter your **story title** and select a **genre**
2. Write your **initial hook**
3. Click **Start Story** to let AI generate the opening
4. Scroll through the **full story** so far
5. Add your own sentences and click **Continue with AI**
6. Or explore **branching choices** and select one
7. Use **Undo Last** to remove the last AI/User addition
8. Adjust **Creativity slider** to control AI imagination

---

## 🔑 System Prompt (used in engine.py)

```
You are a master collaborative storyteller.
Rules:
- Stay strictly in <genre> genre
- Maintain consistency with all previous events and characters
- Never contradict earlier story
- Write vivid, engaging narrative
```

---

## ✅ Memory & Consistency Strategy

* **Story stored in memory** (`engine.story`)
* **Full story sent to LLM** for each API call
* **Branching choices** generated separately to maintain consistency
* **Undo feature** allows safe story editing

---

## 🚀 Bonus Features Ideas

* **Genre remix**: rewrite last section in a different genre
* **Character tracker**: automatically extract characters with descriptions
* **Markdown export**: download full story
* **Visualization prompts**: generate prompts for DALL·E or other image generators

---

## ⚠️ Notes

* Requires **OpenAI API key**
* Works best with **GPT-3.5-turbo** or **GPT-4**
* Handles rate limits gracefully with Streamlit errors

