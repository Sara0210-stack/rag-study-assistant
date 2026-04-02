

def generate_response(vectorstore, llm, query):
    # Extract relevant chunks
    docs = vectorstore.similarity_search(query,k=2)

    # combine context
    context = "\n".join([doc.page_content for doc in docs])

    # prompt
    prompt = f"""
    You are a Helpful AI Assistant. 
    
    Answer the question ONLY based on the following context.
    Do NOT include words like "Context" and "Answer" in your response.
    Do NOT repeat the Question in your answer.
    Give a clear and simple answer.

    Context:
    {context}

    Question:
    {query}
    """
    # LLM response
    response = llm.invoke(prompt)
    answer = response.content if hasattr(response, "content") else response
    return answer, docs