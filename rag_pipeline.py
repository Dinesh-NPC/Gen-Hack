from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from vector_store import MemoryVaultVectorStore
import config

class MemoryVaultRAG:
    def __init__(self, vector_store: MemoryVaultVectorStore):
        if not config.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is required. Please set the OPENAI_API_KEY environment variable.")

        self.vector_store = vector_store
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=0.7,
            openai_api_key=config.OPENAI_API_KEY
        )

        # Custom prompt for creative memory retrieval
        self.prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""
You are a creative memory assistant that helps users relive and reinterpret their stored memories.
Based on the following memories from the user's vault:

{context}

Answer the user's question in a creative and engaging way. You can:
- Generate poems about the memories
- Create dialogues based on the content
- Summarize memories in narrative form
- Suggest connections between different memories
- Provide imaginative interpretations

Question: {question}

Creative Response:
"""
        )

        # Build RAG chain using LCEL
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.rag_chain = (
            {"context": self.vector_store.vectorstore.as_retriever(search_kwargs={"k": 5}) | format_docs, "question": RunnablePassthrough()}
            | self.prompt_template
            | self.llm
            | StrOutputParser()
        )

    def query_memories(self, query: str) -> str:
        """Query the memory vault and get a creative response."""
        try:
            result = self.rag_chain.invoke(query)
            return result
        except Exception as e:
            return f"Error querying memories: {str(e)}"

    def generate_poem(self, query: str) -> str:
        """Generate a poem based on relevant memories."""
        memories = self.vector_store.search_memories(query, k=3)
        context = "\n".join([doc.page_content for doc in memories])

        poem_prompt = f"""
Based on these memories:
{context}

Write a beautiful poem that captures the essence of these memories.
"""

        return self.llm.invoke(poem_prompt).content

    def create_dialogue(self, query: str) -> str:
        """Create a dialogue based on memories."""
        memories = self.vector_store.search_memories(query, k=3)
        context = "\n".join([doc.page_content for doc in memories])

        dialogue_prompt = f"""
Based on these memories:
{context}

Create an engaging dialogue between two characters inspired by these memories.
"""

        return self.llm.invoke(dialogue_prompt).content

    def summarize_memories(self, query: str) -> str:
        """Summarize relevant memories."""
        memories = self.vector_store.search_memories(query, k=5)
        context = "\n".join([doc.page_content for doc in memories])

        summary_prompt = f"""
Summarize the following memories in a cohesive narrative:
{context}

Provide a narrative summary that connects these memories.
"""

        return self.llm.invoke(summary_prompt).content
