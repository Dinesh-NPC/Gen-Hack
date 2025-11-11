import streamlit as st
import tempfile
import os
from vector_store import MemoryVaultVectorStore
from rag_pipeline import MemoryVaultRAG
from utils import process_file, create_langchain_documents
from langchain_core.documents import Document
import config

# Page configuration
st.set_page_config(
    page_title="Advanced Living Memory Vault",
    page_icon="🧠",
    layout="wide"
)

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = MemoryVaultVectorStore()

if 'rag_pipeline' not in st.session_state:
    try:
        st.session_state.rag_pipeline = MemoryVaultRAG(st.session_state.vector_store)
    except ValueError as e:
        st.error(str(e))
        st.stop()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def main():
    st.title("🧠 Advanced Living Memory Vault")
    st.markdown("Upload your memories (text, images, audio) and let AI help you relive them creatively!")

    # Sidebar for file uploads
    with st.sidebar:
        st.header("📁 Upload Memories")

        uploaded_files = st.file_uploader(
            "Choose files",
            accept_multiple_files=True,
            type=['pdf', 'docx', 'txt', 'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'mp3', 'wav', 'flac', 'm4a']
        )

        if uploaded_files:
            if st.button("Process & Store Memories"):
                with st.spinner("Processing files..."):
                    process_uploaded_files(uploaded_files)
                st.success("Memories stored successfully!")

        # Display stored memories count
        try:
            memories = st.session_state.vector_store.get_all_memories()
            st.info(f"📚 Stored Memories: {len(memories)}")
        except:
            st.info("📚 Stored Memories: 0")

    # Main content area
    tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat with Memories", "📝 Generate Poem", "🎭 Create Dialogue", "📖 Summarize Memories"])

    with tab1:
        chat_interface()

    with tab2:
        poem_interface()

    with tab3:
        dialogue_interface()

    with tab4:
        summary_interface()

def process_uploaded_files(uploaded_files):
    documents = []
    metadatas = []

    for uploaded_file in uploaded_files:
        # Save uploaded file to temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        try:
            # Determine file type
            file_ext = os.path.splitext(uploaded_file.name)[1].lower()
            if file_ext in ['.pdf', '.docx', '.txt']:
                file_type = 'text'
            elif file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
                file_type = 'image'
            elif file_ext in ['.mp3', '.wav', '.flac', '.m4a']:
                file_type = 'audio'
            else:
                continue

            # Process file
            content, embedding, metadata_type = process_file(tmp_file_path, file_type)

            # Create document
            doc = Document(
                page_content=content,
                metadata={
                    'filename': uploaded_file.name,
                    'type': metadata_type,
                    'file_path': tmp_file_path
                }
            )
            documents.append(doc)
            metadatas.append({'filename': uploaded_file.name, 'type': metadata_type})

        finally:
            # Clean up temp file
            os.unlink(tmp_file_path)

    # Add to vector store
    if documents:
        st.session_state.vector_store.add_memories(documents, metadatas)

def chat_interface():
    st.header("💬 Chat with Your Memories")

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask about your memories..."):
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        # Get response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.rag_pipeline.query_memories(prompt)
            st.write(response)

        # Add assistant response to history
        st.session_state.chat_history.append({"role": "assistant", "content": response})

def poem_interface():
    st.header("📝 Generate Poem from Memories")

    query = st.text_input("Enter a theme or memory to inspire the poem:", key="poem_query")

    if st.button("Generate Poem", key="poem_btn"):
        if query:
            with st.spinner("Crafting poem..."):
                poem = st.session_state.rag_pipeline.generate_poem(query)
            st.text_area("Generated Poem:", value=poem, height=300)
        else:
            st.warning("Please enter a theme or memory.")

def dialogue_interface():
    st.header("🎭 Create Dialogue from Memories")

    query = st.text_input("Enter a theme or memory for the dialogue:", key="dialogue_query")

    if st.button("Create Dialogue", key="dialogue_btn"):
        if query:
            with st.spinner("Creating dialogue..."):
                dialogue = st.session_state.rag_pipeline.create_dialogue(query)
            st.text_area("Generated Dialogue:", value=dialogue, height=300)
        else:
            st.warning("Please enter a theme or memory.")

def summary_interface():
    st.header("📖 Summarize Memories")

    query = st.text_input("Enter what memories to summarize:", key="summary_query")

    if st.button("Generate Summary", key="summary_btn"):
        if query:
            with st.spinner("Summarizing memories..."):
                summary = st.session_state.rag_pipeline.summarize_memories(query)
            st.text_area("Memory Summary:", value=summary, height=300)
        else:
            st.warning("Please enter what memories to summarize.")

if __name__ == "__main__":
    main()
