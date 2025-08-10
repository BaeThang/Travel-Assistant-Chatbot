# ChatBot Travel

A travel-focused chatbot web application that provides concise, English-only answers to travel-related questions using advanced AI models and strict topic filtering. The backend uses Python (HuggingFace Inference API, SQLite for keyword management), while the frontend and API server are built with Node.js and Express.

## Features
- Answers only travel-related questions (destinations, culture, food, etc.)
- English-only, concise, plain-text responses (no markdown)
- Strict keyword-based topic filtering (managed via SQLite database)
- Global travel support (not limited to Vietnam)
- Modern, English-language web interface

## Project Structure
```
ChatBot_Travel/
├── package.json
├── sever.js                # Node.js Express server
├── chatbot.py              # Python backend (AI logic)
├── keyword_database.py     # Python class for managing keywords in SQLite
├── travel_keywords.sql     # SQL schema for keywords/destinations
├── .env                    # HuggingFace API token (not committed)
├── public/
│   ├── index.html          # Frontend UI
│   └── images/             # Travel images
```

## Setup Instructions

### 1. Install Node.js Dependencies
```powershell
npm install
```

### 2. Install Python Dependencies
```powershell
pip install -r requirements.txt
```
(If `requirements.txt` is missing, install: `transformers`, `huggingface_hub`, `python-dotenv`, `sqlite3`)

### 3. Set HuggingFace API Token
Create a `.env` file in the project root:
```
HUGGINGFACE_TOKEN=your_huggingface_token_here
```

### 4. Initialize the SQLite Database
Run the SQL script to create the keyword tables:
```powershell
sqlite3 travel_keywords.db < travel_keywords.sql
```

### 5. Start the Application
- Start the Python backend (chatbot):
```powershell
python chatbot.py
```
- In a new terminal, start the Node.js server:
```powershell
npm start
```

### 6. Open the Web Interface
Go to [http://localhost:3000](http://localhost:3000) in your browser.

## Customization
- **Keywords:** Edit `travel_keywords.sql` and use `keyword_database.py` to manage allowed/blocked keywords.
- **Frontend:** Edit `public/index.html` for UI changes.
- **Backend Logic:** Edit `chatbot.py` for AI/model changes.

## Troubleshooting
- Ensure both Python and Node.js servers are running.
- Check `.env` for a valid HuggingFace token.
- If answers contain markdown or non-English, check the prompt and post-processing in `chatbot.py`.
- For database errors, ensure `travel_keywords.db` is initialized.

## License
This project is for educational and demonstration purposes.