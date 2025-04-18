# backend/server/app/config.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import router
from settings import STATIC_DIR, ensure_static_folder  # Import the function

app = FastAPI()

def setup_cors():
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router)

    # ✅ Ensure static folder exists before mounting
    ensure_static_folder()
    
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

setup_cors()
