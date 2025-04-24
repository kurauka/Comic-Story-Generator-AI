from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.gemini import generate_comic_story
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://kurauka.github.io/Comic-Story-Generator-AI/"],  # 👈 or use ["http://localhost:5500"] if you want to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Comic Book Generator API is running!"}


@app.post("/generate-story")
def generate_story(request: PromptRequest):
    try:
        story = generate_comic_story(request.prompt)
        return {"story": story}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

