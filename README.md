# 📚 RAG Study Assistant (Local AI)

An AI-powered document assistant that allows users to upload PDFs and ask questions using a Retrieval-Augmented Generation (RAG) pipeline.

## 🚀 Features
- 📄 Upload PDF documents
- 💬 Ask questions about the document
- 🧠 Uses semantic search (FAISS + embeddings)
- 🤖 Local LLM (Phi via LM Studio)
- 📌 Source-based answers (Explainable AI)
- 🧪 Quiz generation & summary

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- LM Studio (Phi model)

## ⚙️ How it Works
1. PDF is loaded and split into chunks  
2. Chunks are converted into embeddings  
3. Stored in FAISS vector database  
4. User query retrieves relevant chunks  
5. LLM generates answer based on context  

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/rag-study-assistant.git
cd rag-study-assistant

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
streamlit run app.py

![My App](assets/screenshot.png)

💡 Author
Sara Shaikh