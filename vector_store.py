import chromadb
from chromadb.config import Settings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from typing import List, Dict, Any
import config

class MemoryVaultVectorStore:
    def __init__(self):
        if not config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is required. Please set the OPENAI_API_KEY environment variable.")

        self.client = chromadb.PersistentClient(path=config.CHROMA_DB_PATH)
        self.collection_name = "memory_vault"
        self.embedding_function = OpenAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            openai_api_key=config.OPENAI_API_KEY
        )
        self.vectorstore = None
        self._initialize_collection()

    def _initialize_collection(self):
        """Initialize or get existing ChromaDB collection."""
        try:
            self.collection = self.client.get_collection(name=self.collection_name)
        except Exception:
            self.collection = self.client.create_collection(name=self.collection_name)

        # Initialize LangChain Chroma vectorstore
        self.vectorstore = Chroma(
            client=self.client,
            collection_name=self.collection_name,
            embedding_function=self.embedding_function,
        )

    def add_memories(self, documents: List[Document], metadatas: List[Dict[str, Any]] = None):
        """Add memories to the vector store."""
        if metadatas is None:
            metadatas = [{}] * len(documents)

        # Add to ChromaDB collection with multimodal embeddings
        ids = [f"doc_{i}" for i in range(len(documents))]
        texts = [doc.page_content for doc in documents]
        embeddings = []

        for doc in documents:
            # For multimodal, we might need custom embeddings
            # For now, use OpenAI embeddings for text
            embedding = self.embedding_function.embed_query(doc.page_content)
            embeddings.append(embedding)

        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )

        # Update LangChain vectorstore
        self.vectorstore.add_documents(documents, metadatas=metadatas)

    def search_memories(self, query: str, k: int = 5) -> List[Document]:
        """Search for relevant memories."""
        return self.vectorstore.similarity_search(query, k=k)

    def get_all_memories(self) -> List[Document]:
        """Get all stored memories."""
        return self.vectorstore.get()

    def delete_memory(self, doc_id: str):
        """Delete a memory by ID."""
        self.collection.delete(ids=[doc_id])
        # Note: LangChain Chroma doesn't have direct delete, so we recreate
        self._initialize_collection()

    def clear_all_memories(self):
        """Clear all memories."""
        self.client.delete_collection(name=self.collection_name)
        self._initialize_collection()
