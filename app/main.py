# from dotenv import load_dotenv
# load_dotenv()

from app.web_loader import load_urls
from app.document_splitter import split_documents
from app.vector_store import create_vector_store
from app.rag_chain import create_rag_chain


def main():

    print("Loading documentation from URLs...")
    documents = load_urls("data/urls.txt")

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Creating vector store...")
    vectorstore = create_vector_store(chunks)

    print("Initializing RAG system...")
    rag = create_rag_chain(vectorstore)

    print("\n Ready! Ask questions (type 'exit' to quit)\n")

    while True:
        query = input("Question: ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        result = rag(query)

        print("\n Answer:")
        print(result["answer"])

        print("\n Sources:")
        for src in result["sources"]:
            print("-", src)

        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()