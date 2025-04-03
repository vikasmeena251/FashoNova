import os
from google import genai
from google.genai import types
import shutil
from uuid import uuid4
import base64

async def transform_with_gemini(image, prompt):
    # Save the uploaded image locally
    input_path = f"temp_{uuid4().hex}.png"
    with open(input_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    # Setup Gemini client
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    # Upload the image to Gemini
    uploaded_file = client.files.upload(file=input_path)
    

    # Prepare content
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=uploaded_file.uri,
                    mime_type=uploaded_file.mime_type,
                ),
                types.Part.from_text(text=prompt),
            ]
        )
    ]

    # Define generation config
    config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_modalities=["image", "text"],
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_CIVIC_INTEGRITY",
                threshold="OFF",
            ),
        ],
        response_mime_type="text/plain",
    )

    # Generate content
    for chunk in client.models.generate_content_stream(
        model="gemini-2.0-flash-exp-image-generation",
        contents=contents,
        config=config,
    ):
        if chunk.candidates and chunk.candidates[0].content.parts:
            part = chunk.candidates[0].content.parts[0]
            if part.inline_data:
                output_path = f"output_{uuid4().hex}.jpg"
                with open(output_path, "wb") as out_file:
                    out_file.write(part.inline_data.data)
                return output_path

    raise Exception("No image data returned by Gemini API.")
