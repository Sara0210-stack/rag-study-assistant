from langchain_openai import OpenAI
def get_llm():
    return OpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="Lm-studio",
        model="local model",
        max_tokens=200
    )