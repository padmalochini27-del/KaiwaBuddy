# 🌸 KaiwaBuddy — Your Local AI Japanese Conversation Partner

**Learn Japanese through conversation, grammar explanations, and practice — powered by local AI.**

KaiwaBuddy is a beginner-friendly Japanese learning assistant built with Python, Streamlit, Ollama, and Gemma 3 1B. It helps learners practise basic Japanese, explore vocabulary and grammar, and interact with a locally running AI model.

The project focuses on making Japanese learning approachable while exploring the possibilities of running AI locally on your own computer.

## ✨ Features

- 💬 **Japanese Conversation Practice** — Practise beginner-level Japanese with an AI conversation partner.
- 📘 **Grammar Explanations** — Explore basic Japanese sentence patterns and grammar.
- 🔤 **Vocabulary Learning** — Review beginner vocabulary with built-in learning activities.
- 📝 **Practice Mode** — Test your understanding through practice questions.
- 🇯🇵 **Romaji and English Support** — Get pronunciation and meaning support where available.
- 🧠 **Rule-Based Japanese Checks** — Uses predefined grammar patterns, vocabulary, and known sentences to handle supported examples.
- 🖥️ **Local AI Integration** — Uses Ollama to run Gemma 3 1B locally, avoiding the need for a hosted LLM API for model inference.
- 🌿 **Calm, Beginner-Friendly Interface** — A warm cream, sage green, and sakura-inspired design.

> **Note:** Japanese correction coverage is limited to the rules and examples implemented in the project. AI-generated responses may contain mistakes and should be checked against trusted learning materials.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| Ollama | Local language-model runtime |
| Gemma 3 1B | Local AI conversation model |
| Git and GitHub | Version control and source code hosting |

## ⚙️ Getting Started

### Prerequisites

Install the following before running KaiwaBuddy:

- Python
- Git
- [Ollama](https://ollama.com/)
- A computer capable of running the selected Ollama model

### 1. Clone the repository

```bash
git clone https://github.com/padmalochini27-del/KaiwaBuddy.git
cd KaiwaBuddy
```

### 2. Create a virtual environment

**Windows — Command Prompt:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

If the repository contains `requirements.txt`, run:

```cmd
pip install -r requirements.txt
```

Otherwise, install the packages required by the project:

```cmd
pip install streamlit ollama
```

### 4. Install and start the local AI model

Install Ollama from its official website, then run:

```cmd
ollama pull gemma3:1b
```

Make sure the Ollama application or service is running so that KaiwaBuddy can communicate with the model.

### 5. Launch KaiwaBuddy

```cmd
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## 📂 Project Structure

```text
KaiwaBuddy/
├── app.py             # Streamlit application and interface
├── japanese_n5.py     # Japanese vocabulary and grammar logic
├── requirements.txt   # Python dependencies
└── README.md           # Project documentation
```

Your local development folder may also contain `.venv/` and other generated files. These should not be committed to GitHub.

## 🎯 Who Is It For?

- Beginners starting to learn Japanese.
- Learners practising basic conversations and sentence structures.
- Students exploring local AI and open-source tools.
- Developers interested in combining deterministic rules with a locally running language model.

## 🔐 Privacy and Limitations

KaiwaBuddy uses a locally running Ollama model for AI inference. This can reduce reliance on external AI APIs and keep prompts on the local machine when the application and its integrations are configured to operate locally.

- Local execution does not automatically guarantee that every application component operates offline.
- Model responses may be inaccurate, especially for Japanese grammar.
- Rule-based checks cover only the patterns implemented in the code.
- Performance depends on your hardware and the model being used.

Avoid entering sensitive personal information into the application.

## 🚀 Future Improvements

Potential improvements include:

- More thoroughly validated Japanese N5 grammar and correction rules.
- Persistent learning progress and quiz history.
- Personalized vocabulary revision.
- Improved handling of ambiguous Japanese sentences.
- Automated tests for grammar checks and AI responses.
- Additional lessons and conversation scenarios.

These are planned improvements, not claims about currently implemented functionality.

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them.
4. Submit a pull request with a clear description of your contribution.

## 👩‍💻 Author

**Padma Lochini**

- GitHub: [@padmalochini27-del](https://github.com/padmalochini27-del)
- Project repository: [KaiwaBuddy](https://github.com/padmalochini27-del/KaiwaBuddy)
- Development story: [KaiwaBuddy on DEV Community](https://dev.to/padma_lochini_30f5da896a1/kaiwabuddy-i-built-a-local-ai-japanese-conversation-partner-for-my-friend-4o7j)

---

*Built with curiosity, local AI, and a love for learning Japanese.* 🌸
