# 📚 RAG Study Assistant (Local AI)

An AI-powered assistant that allows users to upload PDF documents and ask questions using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Features

- 📄 Upload PDF documents
- 💬 Ask questions based on document
- 🧠 Semantic search using FAISS
- 🤖 Local LLM (Phi via LM Studio)
- 📌 Source-based answers
- 💬 Chat history (like ChatGPT)
- 📄 Summary & Quiz generation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- LM Studio (Phi model)

---

## ⚙️ How It Works

1. Upload PDF  
2. Text is extracted and split into chunks  
3. Chunks are converted into embeddings  
4. Stored in FAISS vector database  
5. Query retrieves relevant chunks  
6. LLM generates context-based answer  

---

## 📸 Screenshots

![RAG App](assets/Screenshot.png)

---

## ▶️ Run Locally

```bash
git clone https://github.com/Sara0210-stack/rag-study-assistant.git
cd rag-study-assistant

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py