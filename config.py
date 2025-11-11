import os

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required. Please set it in a .env file or your environment.")

# ChromaDB settings
CHROMA_DB_PATH = "./chroma_db"

# Model settings
EMBEDDING_MODEL = "text-embedding-3-large"
LLM_MODEL = "gpt-4o"

# File processing settings
SUPPORTED_TEXT_EXTENSIONS = ['.pdf', '.docx', '.txt']
SUPPORTED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
SUPPORTED_AUDIO_EXTENSIONS = ['.mp3', '.wav', '.flac', '.m4a']
