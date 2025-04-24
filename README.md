```markdown
# 📚 Comic Book Generator API

A FastAPI-powered backend that uses Google's Gemini API to generate fun, kid-friendly comic book stories from user prompts.

---

## 🚀 Features

- 🔮 AI-generated multi-page comic book stories
- 🧒 Kid-friendly tone with characters, narration, and dialogue
- ⚡ Built with FastAPI for quick performance
- 🌍 CORS enabled for frontend compatibility

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework
- **Google Gemini API** – For generating comic content
- **python-dotenv** – Environment variable management
- **Uvicorn** – ASGI server for running the app

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/comic-book-generator-api.git
cd comic-book-generator-api
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5. Run the app

```bash
uvicorn main:app --reload
```

---

## 📡 API Endpoints

### `GET /`

Health check endpoint.

**Response:**

```json
{
  "message": "Comic Book Generator API is running!"
}
```

---

### `POST /generate-story`

Generates a comic story based on user prompt.

**Request:**

```json
{
  "prompt": "A magical treehouse that travels through time"
}
```

**Response:**

```json
{
  "story": "Page 1:...\nPage 2:..."
}
```

---

## 🛰 Deployment on Vercel

Make sure your project is structured like this:

```
project-root/
├── api/
│   └── index.py         # Your FastAPI app
├── utils/
│   └── gemini.py        # Gemini integration
├── requirements.txt
├── .env
└── vercel.json
```

**`vercel.json` example:**

```json
{
  "builds": [
    { "src": "api/index.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "api/index.py" }
  ]
}
```

To deploy:
1. Push to GitHub
2. Connect repo to [Vercel](https://vercel.com/)
3. Set environment variable `GEMINI_API_KEY` in Vercel dashboard

---

## 🧪 Testing

Test your endpoints using:

- [Postman](https://www.postman.com/)
- [curl](https://curl.se/)
- Your custom frontend

---

## 👏 Credits

Made for educational and hackathon purposes using Google Gemini + FastAPI.

---

## 📄 License

MIT License
```

---

Let me know if you want help writing a `.gitignore`, setting up the `.env.example`, or creating a project logo badge for your repo!
