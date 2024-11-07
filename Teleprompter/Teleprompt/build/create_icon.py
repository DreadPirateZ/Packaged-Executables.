# create_icon.py
from PIL import Image, ImageDraw
import random

# Create a new image with a random background color
size = (64, 64)
img = Image.new('RGB', size, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
draw = ImageDraw.Draw(img)

# Draw a "T" for Teleprompter
draw.text((20, 10), "T", fill='white', size=40)

# Save as icon
img.save('teleprompter_icon.ico', format='ICO')