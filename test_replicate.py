# test_replicate.py
from app.services.replicate_service import upscale_image

if __name__ == "__main__":
    test_image = "https://replicate.delivery/pbxt/Ing7Fa4YMk6YtcoG1YZnaK3UwbgDB5guRc5M2dEjV6ODNLMl/cat.jpg"
    result = upscale_image(test_image, scale=2)
    print("Upscaled Image Result:", result)
