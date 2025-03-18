from langchain.embeddings import ChatGroqEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Initialize embeddings
embedding_model = ChatGroqEmbeddings(model="chatgpt-3.5-turbo")

# Create or load FAISS vector store
def create_vector_store(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(docs)
    vector_store = FAISS.from_documents(texts, embedding_model)
    return vector_store

def save_vector_store(vector_store, path="vectorstore/faiss_index"):
    vector_store.save_local(path)

def load_vector_store(path="vectorstore/faiss_index"):
    return FAISS.load_local(path, embedding_model)

def query_vector_store(query, vector_store, k=5):
    return vector_store.similarity_search(query, k=k)

def add_website_to_vector_store(url, vector_store):
    loader = WebBaseLoader(url)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(docs)
    vector_store.add_documents(texts)
    return vector_store

# Example usage
if __name__ == "__main__":
    vector_store = load_vector_store() if os.path.exists("vectorstore/faiss_index") else None
    if not vector_store:
        print("No vector store found. Creating a new one.")
        vector_store = create_vector_store([])
    
    url = input("Enter website URL to add to the vector store: ")
    vector_store = add_website_to_vector_store(url, vector_store)
    save_vector_store(vector_store)
    print(f"Content from {url} added to the vector store.")

    query = input("Enter query: ")
    results = query_vector_store(query, vector_store)
    for i, res in enumerate(results, 1):
        print(f"Result {i}: {res.page_content}\n")