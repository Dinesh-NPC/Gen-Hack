# 🧠 Ninaivugal — Advanced AI Memory Vault

**Ninaivugal** is an AI-driven memory vault designed to store, retrieve, and creatively interpret user memories.  
It supports multimodal data (text, images, and audio) and enables semantic interactions through OpenAI models, embeddings, and vector storage.

---

## ⚙️ Overview

Ninaivugal allows users to upload personal memories — documents, images, or audio recordings — and relive them through AI-powered interactions.  
It integrates **Streamlit**, **OpenAI**, **LangChain**, and **ChromaDB** for retrieval-augmented generation (RAG) and persistent semantic memory management.

---

## 🚀 Installation & Setup

1️⃣ **Clone the repository and install dependencies**  
```bash
git clone https://github.com/Dinesh-NPC/Gen-Hack  
cd ninaivugal  
pip install -r requirement.txt
```

2️⃣ **Configure environment variables**  
```bash
Create a `.env` file and specify the following:  
OPENAI_API_KEY=your_api_key_here  
CHROMA_DB_PATH=./chroma_db
```

3️⃣ **Launch the application**  
```bash
streamlit run app.py  
```
Access the UI at: [http://localhost:8501](http://localhost:8501)

---

## 🧩 Core Features

- **Multimodal Memory Uploads**: Supports text (PDF, DOCX, TXT), images (PNG, JPG), and audio (MP3, WAV).  
- **Vector-Based Retrieval**: Uses `text-embedding-3-large` for semantic search and similarity matching.  
- **AI-Powered Interaction**: Engage through chat, poem creation, dialogue generation, and summaries.  
- **Persistent Storage**: Local ChromaDB instance for scalable memory retention.  
- **Streamlit UI**: Clean interface with tabs for Upload, Chat, Poem, Dialogue, and Summary.  
- **Audio Transcription**: Optional Whisper model for speech-to-text conversion.

---

## 🔧 Models & Tools

- **LLM**: GPT-4o  
- **Embeddings**: text-embedding-3-large  
- **Audio Transcription**: Whisper base  
- **Image Analysis**: CLIP-ViT-B-32, BLIP  
- **Vector Database**: ChromaDB  
- **Frameworks**: Streamlit, LangChain, OpenAI SDK  

---

## 📸 Screenshots
<img width="1920" height="1080" alt="Screenshot (77)" src="https://github.com/user-attachments/assets/d0dcfc48-f06e-4c94-91f3-a77fcee0589d" />


**Chat with Memories:**

<img width="1920" height="1080" alt="Screenshot (78)" src="https://github.com/user-attachments/assets/4a338ea0-abe7-4bff-84d3-3c5fd6e51763" />


**Generate Poem:**

<img width="1920" height="1080" alt="Screenshot (80)" src="https://github.com/user-attachments/assets/c136fab3-0504-4985-ab1a-99a795e9ba82" />


**Create Dialogue:**

<img width="1920" height="1080" alt="Screenshot (83)" src="https://github.com/user-attachments/assets/716e4022-6611-4e9c-9185-97cd5fea486c" />




**Memories Visualizations:**

<img width="1920" height="1080" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/769f76bd-6d6e-420a-87cf-9e7f8de09eee" />


**cross references:**

<img width="1920" height="1080" alt="Screenshot (86)" src="https://github.com/user-attachments/assets/464927f6-81d1-44c9-b4b0-448590c92eba" />



**Voice synthesis:**

<img width="1920" height="1080" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/5a2f607c-cad3-44e3-87c6-7ac98a462a58" />


---

## 🧾 License

This project is open source. Refer to the `LICENSE` file for details.

---

## 👤 Author

Built with ❤️ by [Your Name]  
🔗 LinkedIn: https://www.linkedin.com/in/dinesh-kumar-kct
