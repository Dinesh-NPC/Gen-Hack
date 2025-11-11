# Ninaivugal - Advanced Living Memory Vault

🧠 **Ninaivugal** (Memories in Tamil) is an AI-powered memory vault that allows you to upload and relive your cherished memories through creative AI interactions. Store text documents, photos, and audio recordings, then engage with them through intelligent chat, poem generation, dialogue creation, and narrative summaries.

## ✨ Features

- **Multimodal Memory Storage**: Upload and process text (PDF, DOCX, TXT), images (JPG, PNG, etc.), and audio files (MP3, WAV, etc.)
- **AI-Powered Interactions**: Chat with your memories, generate poems, create dialogues, and get narrative summaries
- **Vector Search**: Advanced semantic search using OpenAI embeddings for relevant memory retrieval
- **Persistent Storage**: Local ChromaDB vector database for reliable memory storage
- **Creative Responses**: GPT-4 powered responses that interpret and reimagine your memories
- **Modern Web Interface**: Clean Streamlit UI with intuitive tabs for different interaction modes

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key (for embeddings and LLM)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ninaivugal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   # OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 📖 Usage

### Uploading Memories

1. Use the sidebar to upload your memory files
2. Supported formats:
   - **Text**: PDF, DOCX, TXT files
   - **Images**: JPG, JPEG, PNG, BMP, TIFF
   - **Audio**: MP3, WAV, FLAC, M4A
3. Click "Process & Store Memories" to add them to your vault

### Interacting with Memories

#### 💬 Chat with Memories
- Ask questions about your stored memories
- Get creative interpretations and connections between different memories

#### 📝 Generate Poem
- Enter a theme or memory reference
- AI generates a beautiful poem inspired by your memories

#### 🎭 Create Dialogue
- Specify a theme from your memories
- AI creates an engaging dialogue between characters based on your content

#### 📖 Summarize Memories
- Request summaries of specific memories or themes
- Get cohesive narratives connecting multiple memories

## 🏗️ Project Structure

```
ninaivugal/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration and settings
├── vector_store.py        # ChromaDB vector store management
├── rag_pipeline.py        # RAG implementation with LangChain
├── utils.py               # File processing utilities
├── requirement.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
├── chroma_db/            # Persistent vector database
├── uploaded_memories/    # Sample uploaded files
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `CHROMA_DB_PATH`: Path for ChromaDB storage (default: "./chroma_db")

### Model Settings

- **Embedding Model**: text-embedding-3-large
- **LLM Model**: gpt-4o
- **Whisper Model**: base (for audio transcription)
- **Image Models**: CLIP-ViT-B-32, BLIP (for image processing)

## 📋 Requirements

- streamlit
- langchain
- openai
- chromadb
- pypdf
- python-docx
- sentence-transformers
- pillow
- openai-whisper
- gtts
- moviepy
- opencv-python
- torch
- transformers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source. Please check the license file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/)
- Vector storage with [ChromaDB](https://www.trychroma.com/)
- RAG implementation using [LangChain](https://www.langchain.com/)

---

**Relive your memories, reimagine your stories.** 🧠✨
