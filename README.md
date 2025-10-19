# 🤖 Ollama RAG — Document Question Answering App

This project is a simple **Retrieval-Augmented Generation (RAG)** system built with **LangChain**, **Ollama**, and **FAISS**.  
It allows users to upload a PDF file 📄 and ask natural language questions 💬 — the app retrieves relevant document chunks and generates intelligent answers using a local LLM.

---

## 🚀 Features
✅ Upload any PDF file  
✅ Ask questions about its content  
✅ Uses local **Ollama LLM** (`llama3:instruct`)  
✅ Performs semantic retrieval with **FAISS**  
✅ Clean and simple **Streamlit UI**

---

## 🧩 Tech Stack
| Component | Description |
|------------|--------------|
| 🧠 **Ollama** | Local Large Language Model (LLM) |
| 🧾 **LangChain** | Manages document splitting, retrieval, and chaining |
| 💬 **Streamlit** | Frontend interface |
| 🔍 **FAISS** | Vector similarity search |
| 🧩 **HuggingFace Embeddings** | Text embedding model |
| 📄 **Unstructured** | Document loader for PDF/Text |

---

## ⚙️ Project Structure

ollama-rag/
│
├── app.py # Streamlit UI
├── doc_chat_utility.py # RAG logic (retrieval + generation)
├── requirements.txt # Python dependencies
└── README.md # Project description


---

## 🧠 How It Works
1. **Upload a file** (PDF or text-based).  
2. The app splits the document into small chunks.  
3. Each chunk is embedded using **HuggingFace embeddings**.  
4. **FAISS** stores and retrieves the most relevant chunks based on the query.  
5. **Ollama (llama3:instruct)** generates a natural language answer.

---

## 🖥️ Installation & Running Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<moustafaaaaaa>/ollama-rag.git
cd ollama-rag

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Make sure Ollama is running locally

Download Ollama and run the LLaMA 3 model:

ollama run llama3:instruct

5️⃣ Run the app
streamlit run app.py


Then open your browser and go to 👉 http://localhost:8501
