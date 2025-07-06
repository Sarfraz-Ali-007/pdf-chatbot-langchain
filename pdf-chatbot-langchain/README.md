# 📚 AI-Powered Multi-PDF Conversational Reader

This project is an **AI-powered Streamlit app** that lets you **chat with multiple PDF documents** using a **LangChain Retrieval-Augmented Generation (RAG)** pipeline.
Upload your PDFs, ask questions, and get instant, context-aware answers — all in one simple interface!

---

## 🚀 **Features**

✅ Extract text from multiple PDF files with **PyPDF2**

✅ Split text into smart, overlapping chunks with **LangChain’s `CharacterTextSplitter`**

✅ Generate embeddings using **Cohere Embeddings**

✅ Store and search vectors efficiently with **FAISS**

✅ Use **Groq’s Llama 3.1 8B Instant LLM** for fast, accurate answers

✅ Maintain conversational context with **ConversationBufferMemory**

✅ Orchestrate everything with **LangChain’s `ConversationalRetrievalChain`**

✅ Clean, interactive frontend built with **Streamlit**

---

## 🛠️ **Tech Stack**

* **Python**
* **Streamlit**
* **LangChain**
* **Groq LLM**
* **Cohere Embeddings**
* **FAISS**
* **PyPDF2**
* **dotenv**

---

## ⚡ **How It Works**

1. 📄 **Upload PDFs**
   Upload one or more PDF files via the sidebar.

2. 🧩 **Text Chunking**
   The app extracts text and splits it into chunks for better semantic search.

3. 🔎 **Embeddings + Vector Store**
   Text chunks are embedded with Cohere and stored in FAISS for efficient similarity search.

4. 🤖 **Conversational Retrieval**
   User questions are answered by the Groq LLM using `ConversationalRetrievalChain` — so answers are relevant and conversational.

5. 🗨️ **Chat UI**
   Interact with your documents through a Streamlit chat interface with full conversational memory.

---

## 💡 **Pro Tips**

* Use well-formatted PDFs for better text extraction.
* Adjust `chunk_size` and `chunk_overlap` to tune retrieval quality.
* Store your `.env` file with your API keys securely.

---

## 🚀 **Run Locally**

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your API keys
touch .env
# Add your keys:
# COHERE_API_KEY=your_cohere_key
# GROQ_API_KEY=your_groq_key

# Run the app
streamlit run app.py
```

---

## 🌐 **Try it Online**

✅ **Live Demo on Hugging Face Spaces:** \[Add your Hugging Face Space URL here]

---

## 📂 **Project Structure**

```
.
├── app.py               # Main Streamlit app
├── htmlTemplates.py     # Custom CSS and HTML templates for chat UI
├── requirements.txt     # Python dependencies
├── .env.example         # Example env file for API keys
└── README.md            # Project readme
```

## 🤝 **Contributing**

Contributions, ideas, and improvements are always welcome!
Feel free to fork this repo, open an issue, or submit a pull request.

---

## 📢 **Connect**

If you try it out, I’d love to hear your feedback!
Let’s make working with large PDFs more intelligent and conversational. 🚀

---

**Happy chatting! 📚🤖**
**#LangChain #RAG #LLM #Groq #Cohere #FAISS #Streamlit**
