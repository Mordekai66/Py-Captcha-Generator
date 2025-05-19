from captcha.image import ImageCaptcha
import os

def generate_image_captcha(data, output_path):
    if not data:
        raise ValueError("Captcha text cannot be empty.")
    
    image = ImageCaptcha()
    image_file = os.path.join(output_path, "captcha.png")
    image.write(data, image_file)
    return image