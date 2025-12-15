from langchain_community.chat_models import ChatOllama


def get_llm():
    """
    Return a local Gemma LLM served by Ollama.

    Prerequisites (outside Python):
    - Install Ollama (Windows installer)
    - Run in a terminal:
        ollama pull gemma:2b
    """
    return ChatOllama(
        model="gemma:2b",
        temperature=0,
        num_ctx=4096,
    )