from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def add_timestamp_to_image(category, image_path='app_data/news_latter_title.png'):
    # Load the image
    image = Image.open(image_path)

    # Get the current date and time
    current_datetime = category+" "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a copy of the image with an alpha channel
    timestamped_image = image.copy().convert("RGBA")

    # Create a new transparent layer for the timestamp
    timestamp_layer = Image.new("RGBA", timestamped_image.size, (0, 0, 0, 0))

    # Set the font properties for the timestamp
    font_size = 45
    font_color = (255, 255, 255)
    font = ImageFont.truetype("app_data/ABeeZee-Regular.ttf", font_size)

    # Calculate the size of the text
    text_width, text_height = font.getsize(current_datetime)

    # Calculate the position to place the timestamp
    padding = 60
    position = (timestamped_image.width - text_width - padding, timestamped_image.height - text_height - padding)

    # Create a drawing object
    draw = ImageDraw.Draw(timestamp_layer)

    # Draw the timestamp text on the transparent layer
    draw.text(position, current_datetime, font=font, fill=font_color)

    # Composite the image and the timestamp layer
    timestamped_image = Image.alpha_composite(timestamped_image, timestamp_layer)

    # Save the timestamped image with a new filename
    output_filename = "news/00_news_latter_title.png"
    timestamped_image.save(output_filename)

    print(f"Timestamped image saved as '{output_filename}'.")

# Example usage:
# add_timestamp_to_image("app_data/news_latter_title.png")
