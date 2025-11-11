# TODO: Advanced Living Memory Vault Implementation

## Core Implementation Steps
- [x] Create config.py: Configuration for API keys and settings.
- [x] Create utils.py: Helper functions for processing files (text extraction, image handling, audio transcription).
- [x] Create vector_store.py: Setup ChromaDB collection, add documents with multimodal embeddings.
- [x] Create rag_pipeline.py: LangChain RAG chain for querying the vector store and generating responses.
- [x] Create app.py: Main Streamlit app with file upload interface, chat UI, and result display.

## Followup Steps
- [x] Verify/install dependencies: `pip install -r requirement.txt`.
- [x] Set up OpenAI API key via environment variable (OPENAI_API_KEY).
- [x] Run the app: `streamlit run app.py`.
- [x] Test uploading files and querying (app is running and ready for manual testing).
- [ ] Optional: Deploy to Streamlit Cloud.
