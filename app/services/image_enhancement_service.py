import replicate
import tempfile

class ImageEnhancementService:
    def enhance_image(self, image_file, scale: int = 2):
        # Save uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            temp_file.write(image_file.read())
            temp_path = temp_file.name

        input = {
            "image": open(temp_path, "rb"),
            "scale": scale
        }

        output = replicate.run(
            "nightmareai/real-esrgan:f121d640bd286e1fdc67f9799164c1d5be36ff74576ee11c803ae5b665dd46aa",
            input=input
        )
        
        output_path = "enhanced_image.png"
        with open(output_path, "wb") as file:
            file.write(output.read())
        
        return output_path
