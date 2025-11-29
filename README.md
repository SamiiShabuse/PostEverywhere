# PostEverywhere
A tool to upload your social media videos (reels) to multiple platforms.

This repository contains a minimal MVP scaffold: a FastAPI backend that accepts video uploads and a tiny static web UI to upload and queue posts.

Quick start (local, Windows PowerShell):

1. Backend (create virtualenv and install):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

2. Open the UI: open `frontend\index.html` in your browser (or serve it with a static server). The page will POST to `http://localhost:8000/api/upload`.

What's included:
- `backend/` - FastAPI app with `/api/upload` and `/api/publish` (publish is a stub/queue for now).
- `frontend/` - Simple HTML+JS upload UI to send reels to the backend.
- `backend/app/publishers/` - publisher adapter stubs (YouTube stub provided).

Next recommended steps:
- Implement persistent job queue and publisher adapters (YouTube first).
- Add OAuth flows and token storage for each platform.
- Replace static UI with React app for improved UX and scheduling.

If you want, I'll continue by implementing the YouTube OAuth + upload flow next and wire it into the publish endpoint.
