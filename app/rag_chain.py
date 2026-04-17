from langchain_community.chat_models import ChatOllama

def create_rag_chain(vectorstore):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatOllama(model="tinyllama")

    def rag_pipeline(question):

        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])
        sources = [doc.metadata.get("source") for doc in docs]

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": sources
        }

    return rag_pipeline