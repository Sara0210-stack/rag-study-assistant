import streamlit as st
import tempfile

from loader import load_pdf
from splitter import split_pdf
from faiss_store import create_vectorstores
from llm import get_llm
from rag_chain import generate_response

st.set_page_config(page_title="RAG Study Assistant", layout="wide")
st.title("📚 RAG Study Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    # ✅ Load only once
    if "vectorstore" not in st.session_state:
        docs = load_pdf(file_path)
        chunks = split_pdf(docs)
        st.session_state.vectorstore = create_vectorstores(chunks)

    if "llm" not in st.session_state:
        st.session_state.llm = get_llm()

    vectorstore = st.session_state.vectorstore
    llm = st.session_state.llm

    st.success("✅ PDF processed!")

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg['role']).write(msg['content'])

    query = st.chat_input("Ask a question")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)

        answer, sources = generate_response(vectorstore, llm, query)

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)

        with st.expander("📌 Sources"):
            for i, source in enumerate(sources):
                st.write(f"Chunk {i+1}:")
                st.write(source.page_content[:200] + "...")