from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

from app.services.gemini_service import transform_with_gemini
from app.services.replicate_service import upscale_image

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Route: Gemini Image Transformation
@app.post("/transform-image")
async def transform_image(
    image: UploadFile = File(...),
    prompt: str = Form(...)
):
    try:
        output_path = await transform_with_gemini(image, prompt)
        return FileResponse(output_path, media_type="image/jpeg", filename="output.jpg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route: Image Upscaling via Replicate
@app.post("/upscale-image")
async def upscale_image_api(image_url: str, scale: int = 2):
    try:
        result = upscale_image(image_url, scale)
        output_image_url = result.get("output", None)
        return {
            "message": "Image upscaled successfully",
            "output_image_url": output_image_url,
            "raw_response": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
