# 🤖 EZ Smart Research Assistant (Offline Chatbot)

A locally running, AI-powered chatbot that helps users understand and interact with PDF documents. It can summarize, answer questions, and even challenge users with logic-based questions — 
all without requiring an internet connection or paid APIs.

---

## 🚀 Features

- 📄 **PDF Text Extraction** – Upload any PDF and extract clean, readable text.
- ✍️ **Summarization** – Auto-generates concise summaries (≤150 words) using Flan-T5.
- ❓ **Ask Anything** – Ask questions based on the document and get contextual answers using RoBERTa.
- 🧠 **Challenge Me Mode** – Generates reasoning-based questions using GPT-Neo to test your understanding.
- 🧠 **Fully Offline** – Runs completely on your local machine using open-source LLMs.
- ✅ **No API Key Required**
- - 🔍 **Answer Highlighting** – Displays the exact text snippet from the document where the answer was found.


---

## 🛠 Tech Stack

| Layer         | Tool/Library                     |
|---------------|----------------------------------|
| UI            | Streamlit                        |
| PDF Handling  | PyPDF2                           |
| Summarization | `google/flan-t5-small` (Hugging Face) |
| Q&A           | `deepset/roberta-base-squad2`    |
| Question Gen  | `EleutherAI/gpt-neo-1.3B`        |
| Others        | Transformers, Torch, Python 3.10 |

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/f342fe78-057a-4292-b8b6-afacb1702960)

![image](https://github.com/user-attachments/assets/496b9deb-0dba-4108-80f5-0e60475aa10c)

![image](https://github.com/user-attachments/assets/b4897af6-e973-4457-b1f5-d136a3a7fb0a)

![image](https://github.com/user-attachments/assets/a41654fe-356b-4664-8b62-4868aefceac7)

![image](https://github.com/user-attachments/assets/7c3fb284-76bd-40bc-acba-0e6363718a3f)

---

## 🧠 How It Works

1. You upload a PDF file.
2. The app extracts text using `PyPDF2`.
3. A Flan-T5 model generates a short summary.
4. You can:
   - Ask questions → RoBERTa answers them based on the doc.
   - Try “Challenge Me” → GPT-Neo generates logic-based questions.
5. All models are run locally via Hugging Face Transformers — no API key required.

---

## ⚙️ Installation

```bash
git clone https://github.com/HimanshuSoni19/ez-smart-research-assistant.git
cd ez-smart-research-assistant
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
streamlit run app.py
