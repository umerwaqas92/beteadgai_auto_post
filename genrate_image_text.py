from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_image_text(title,news):
    # Define the parameters for the text and image generation
    text = news
    font_path = "app_data/ABeeZee-Regular.ttf"
    font_size = 35
    font_color = "#ffffff"
    text_bg_color = "#000000"
    padding_left = 30
    padding_top = 30
    line_spacing = 13
    max_text_width = 994  # Maximum width for the wrapped text

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Wrap the text to fit the maximum width
    wrapped_text = textwrap.wrap(text, width=60)

    # Calculate the text height
    text_height = font_size * len(wrapped_text) + line_spacing * (len(wrapped_text) - 1)

    # Create a new black image with the fixed size
    image_width = 1034
    image_height = max(text_height + 2 * padding_top, 1024)
    image = Image.new("RGB", (image_width, image_height), text_bg_color)
    draw = ImageDraw.Draw(image)

    # Calculate the position to draw the wrapped text
    text_x = padding_left
    text_y = padding_top

    # Draw the wrapped text on the image
    for line in wrapped_text:
        draw.text((text_x, text_y), line, font=font, fill=font_color, align="left")
        text_y += font_size + line_spacing


    title_words = title.split()[:3]
    filename = "_".join(title_words) + "_02.jpg"

    filename="news/stories/"+filename.replace("*","")
    image.save(filename)



