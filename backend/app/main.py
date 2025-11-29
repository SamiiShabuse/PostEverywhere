from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import shutil

BASE_DIR = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
UPLOAD_DIR = os.path.join(ROOT, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="PostEverywhere - Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/platforms")
def list_platforms():
    return {"platforms": ["youtube", "instagram", "tiktok"]}


@app.post("/api/upload")
async def upload_reel(file: UploadFile = File(...), title: str = ""):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")
    ext = os.path.splitext(file.filename)[1]
    reel_id = str(uuid.uuid4())
    filename = f"{reel_id}{ext}"
    dest_path = os.path.join(UPLOAD_DIR, filename)
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"id": reel_id, "filename": filename, "title": title}


@app.post("/api/publish")
async def publish(payload: dict):
    # payload: {"id": "<reel_id>", "platforms": ["youtube","instagram"]}
    reel_id = payload.get("id")
    platforms = payload.get("platforms", [])
    if not reel_id:
        raise HTTPException(status_code=400, detail="Missing reel id")

    # In the MVP we only accept and queue. Real publisher adapters come later.
    # For now return success and echo what would be scheduled.
    return {"status": "queued", "id": reel_id, "platforms": platforms}
