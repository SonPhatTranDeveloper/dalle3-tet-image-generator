"""
Generate images using DALL-E-3
Author: Son Phat Tran
"""
from generator import generate_image
from fileio import download_image
import os

# Define the prompts
PROMPTS = [
    "Củ Kiệu, a traditional delicacy of Vietnamese Tet holiday"
]

# Define directory
ROOT = os.path.dirname(os.path.abspath(__file__))
DIRECTORY = os.path.join(ROOT, "images")


if __name__ == "__main__":
    # Generate image and save to path
    for prompt in PROMPTS:
        url = generate_image(prompt)
        download_image(url, save_path=os.path.join(DIRECTORY, f"{prompt}.png"))
