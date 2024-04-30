import os
import random
from captcha.image import ImageCaptcha
from io import BytesIO

def generate_random_text(length=5):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def main() -> None:
    text: str = generate_random_text()  # Generate random text
    captcha: ImageCaptcha = ImageCaptcha(
        width=400,
        height=220,
        fonts=[
            os.path.join(r"C:\Windows\Fonts", "arial.ttf"),  # Example font path
            os.path.join(r"C:\Windows\Fonts", "times.ttf"),  # Example font path
            os.path.join(r"C:\Windows\Fonts", "verdana.ttf")  # Example font path
        ],
        font_sizes=(40, 70, 100)
    )
    captcha.write(text, 'captcha.png')
    print("Captcha generated successfully.")

if __name__ == '__main__':
    main()
