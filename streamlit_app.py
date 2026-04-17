import streamlit as st
from app.web_loader import load_urls
from app.document_splitter import split_documents
from app.vector_store import create_vector_store
from app.rag_chain import create_rag_chain

st.title("Smart Documentation Assistant")

@st.cache_resource
def setup_rag():
    documents = load_urls("data/urls.txt")
    chunks = split_documents(documents)
    vectorstore = create_vector_store(chunks)
    rag = create_rag_chain(vectorstore)
    return rag

rag = setup_rag()

query = st.text_input("Ask a question:")

if query:
    result = rag(query)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    for src in result["sources"]:
        st.write(src)