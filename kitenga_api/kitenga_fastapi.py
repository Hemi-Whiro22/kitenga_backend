from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import datetime
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(title="Kitenga Tool API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock OCR tool
def mock_ocr(file: UploadFile):
    filename = file.filename
    return f"Extracted text from {filename} (placeholder)"

# Mock translate tool
def mock_translate_to_maori(text: str):
    return f"(Te Reo translation of) {text}"

@app.get("/")
def root():
    return {"message": "Kitenga is watching..."}

@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    result = mock_ocr(file)
    timestamp = datetime.datetime.utcnow().isoformat()
    filename = file.filename
    image_url = f"https://{SUPABASE_URL}/storage/v1/object/public/kitenga-ocr/{filename}"
    supabase.table("kitenga_ocr_logs").insert({
        "image_url": image_url,
        "extracted_text": result,
        "tool_used": "ocr_image",
        "created_at": timestamp
    }).execute()
    return {
        "tool": "ocr_image",
        "filename": filename,
        "extracted_text": result,
        "image_url": image_url,
        "timestamp": timestamp
    }

@app.post("/translate/maori")
async def translate_to_maori(text: str = Form(...)):
    translated = mock_translate_to_maori(text)
    timestamp = datetime.datetime.utcnow().isoformat()
    supabase.table("kitenga_translations").insert({
        "source_text": text,
        "translated_text": translated,
        "lang": "mi",
        "created_at": timestamp
    }).execute()
    return {
        "tool": "translate_to_maori",
        "original": text,
        "translated": translated,
        "timestamp": timestamp
    }

@app.post("/stamp/meta")
async def stamp_meta(
    source_type: str = Form(...),
    source_url: str = Form(...),
    tags: Optional[str] = Form(None),
):
    timestamp = datetime.datetime.utcnow().isoformat()
    tags_list = tags.split(",") if tags else []
    supabase.table("kitenga_meta_stamps").insert({
        "source_type": source_type,
        "source_url": source_url,
        "tags": tags_list,
        "agent": "kitenga",
        "timestamp": timestamp
    }).execute()
    return {
        "tool": "stamp_metadata",
        "source_type": source_type,
        "source_url": source_url,
        "tags": tags_list,
        "agent": "kitenga",
        "timestamp": timestamp
    }

@app.get("/howl")
def latest_howl():
    ocr_log = supabase.table("kitenga_ocr_logs").select("*").order("created_at", desc=True).limit(1).execute().data
    translation_log = supabase.table("kitenga_translations").select("*").order("created_at", desc=True).limit(1).execute().data
    meta_log = supabase.table("kitenga_meta_stamps").select("*").order("timestamp", desc=True).limit(1).execute().data

    return {
        "howl": {
            "last_ocr": ocr_log[0] if ocr_log else {},
            "last_translation": translation_log[0] if translation_log else {},
            "last_meta": meta_log[0] if meta_log else {},
            "agent": "kitenga",
            "issued_at": datetime.datetime.utcnow().isoformat()
        }
    }
