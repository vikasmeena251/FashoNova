import os
import requests

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

def upscale_image(image_url, scale=2):
    if not REPLICATE_API_TOKEN:
        raise ValueError("REPLICATE_API_TOKEN not set in environment.")

    endpoint = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Bearer {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json",
        "Prefer": "wait"
    }

    data = {
        "version": "f121d640bd286e1fdc67f9799164c1d5be36ff74576ee11c803ae5b665dd46aa",
        "input": {
            "image": image_url,
            "scale": scale
        }
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code != 201:
        raise Exception(f"Error from Replicate API: {response.status_code} - {response.text}")

    return response.json()
