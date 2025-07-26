# 🤖 AI Research Agent

A modular, LLM-powered autonomous agent system designed for research, analysis, and knowledge extraction. Built with extensibility and API integration in mind, this project leverages large language models (LLMs) like Groq, and features agents that can browse, analyze, and report on diverse tasks.

---

## 🚀 Features

- 🔎 Web browsing agent for research and link extraction
- 🧠 Knowledge aggregation and summarization
- 🧾 Analyst agent for structured report generation
- 📂 Environment-configured via `.env` for secure API usage
- 🧩 Modular and extensible design

---

## 📁 Project Structure

aiAgents/
├── agents/ # Core agent logic and behaviors
├── task/ # given task logic
├── main.py # Entry point to run the agent system
├── .env # Environment variables (API keys, etc.)
├── .gitignore
└── README.md

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nikhil2027/ai_research_agent.git
cd ai_research_agent
2. Install dependencies
pip install -r requirements.txt

3. Create your .env file
# .env
GROQ_API_KEY=your_actual_key_here
SERPER_API_KEY=your_actual_key_here
RESEARCH_AGENT_LLM=groq/llama-3.3-70b-versatile
⚠️ Do NOT commit this file.

4. Run the main agent
python main.py
🧠 Agents Overview
ResearchAgent: Uses LLM and web search to gather contextual information

AnalystAgent: Summarizes and structures content

MemoryManager: Embedding and retrieval of prior information

🛠️ Technologies Used
Python 3.11+

Groq API (LLMs)

Serper.dev or other search APIs

LangChain (optional)

dotenv

🧪 Example Use Case
Ask the agent:
“Compare Nvidia and AMD’s latest GPU architecture advancements.”

And it will:

Search trusted sources

Summarize differences

Generate a well-structured report
