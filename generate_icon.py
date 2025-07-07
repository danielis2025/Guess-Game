from PIL import Image, ImageDraw, ImageFont

# Create a blank black image
size = (64, 64)
image = Image.new("RGB", size, "black")

# Initialize drawing context
draw = ImageDraw.Draw(image)

# Load a default font
font = ImageFont.load_default()

# Define the text
text = "cmdAR1"

# Calculate text size using font.getbbox
bbox = font.getbbox(text)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Calculate position to center the text
position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)

# Draw the text in white
draw.text(position, text, fill="white", font=font)

# Save the image as .ico and .png
image.save("cmdAR1_icon.ico")
image.save("cmdAR1_icon_preview.png")

print("Icon and preview image have been created.")
