import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
from io import BytesIO
from app_data.manage_app_config import *


def generate_news_image(image_url, news):
    # Download the source image
    response = requests.get(image_url)
    source_image = Image.open(BytesIO(response.content))
    # Define the parameters for the text and image generation
    text = news
    font_path = "app_data/Anton-Regular.ttf"
    font_size = 60
    font_color_quote = "#33CC66"
    font_color_normal = "#ffffff"
    text_bg_color = "#00000000"
    padding_bottom = 110
    line_spacing = 13
    char_spacing = -3

    # Create a new blank image
    output_image_size = (1024, 1024)
    output_image = Image.new("RGB", output_image_size)

    # Calculate the scaling factor for the source image
    scaling_factor = max(output_image_size[0] / source_image.width, output_image_size[1] / source_image.height)
    new_image_size = (int(source_image.width * scaling_factor), int((source_image.height) * scaling_factor))

    # Resize the source image with the calculated dimensions
    resized_image = source_image.resize(new_image_size, Image.ANTIALIAS)

    # Calculate the position to paste the resized image onto the output image (centered)
    paste_position = ((output_image_size[0] - resized_image.width) // 2, (output_image_size[1] - resized_image.height) // 2)

    # Paste the resized image onto the output image
    output_image.paste(resized_image, paste_position)

    # Create a gradient overlay
    gradient_height = int(output_image_size[1] * 0.7)  # 50% of the image height
    gradient_width = output_image_size[0]
    gradient = Image.new("L", (gradient_width, gradient_height), color=0)  # Set the color to black
    draw = ImageDraw.Draw(gradient)
    for y in range(gradient_height):
        alpha = int((y / gradient_height) * 255)  # Linear gradient from 0% to 100% opacity
        draw.line((0, y, gradient_width, y), fill=alpha)

    # Resize the gradient overlay to match the size of the output image
    resized_gradient = gradient.resize(output_image_size, Image.ANTIALIAS)

    # Invert the gradient
    resized_gradient = ImageOps.invert(resized_gradient)

    # Create a mask using the resized gradient
    mask = Image.new("L", output_image_size)
    mask.paste(resized_gradient, (0, 0))

    # Apply the mask to the output image
    output_image = Image.composite(output_image, Image.new("RGB", output_image_size), mask)

    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(output_image)

    # Wrap the text into multiple lines
    wrapper = textwrap.TextWrapper(width=39)
    wrapped_text = wrapper.wrap(text)

    # Calculate the height of each line
    line_height = font.getsize(text)[1]

    # Calculate the total height of the wrapped text
    total_text_height = line_height * len(wrapped_text) + line_spacing * (len(wrapped_text) - 1)

    # Calculate the position for the text
    text_position_y = (output_image_size[1] - total_text_height -padding_bottom)

    # Draw each line of the text
    for line in wrapped_text:
        # Calculate the width of the line
        line_width = font.getsize(line)[0]

        # Calculate the position for the line to be centered
        text_position_x = (output_image_size[0] - line_width) // 2

        if "*" in line:
            # Split the line by single quotes
            parts = line.split("*")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Draw the part outside single quotes with white color
                    draw.text((text_position_x, text_position_y), part, font=font, fill=font_color_normal,
                              align="center", spacing=char_spacing)
                    text_position_x += font.getsize(part)[0]
                else:
                    # Draw the part within single quotes with the specified color and background box
                    text_width, text_height = font.getsize(part)
                    bg_width = text_width + 10
                    bg_height = text_height + 10
                    bg_position_x = text_position_x - 5
                    bg_position_y = text_position_y - 5
                    bg_rectangle = [(bg_position_x, bg_position_y),
                                    (bg_position_x + bg_width, bg_position_y + bg_height)]

                    draw.rectangle(bg_rectangle, fill=font_color_quote)
                    draw.text((text_position_x, text_position_y), part, font=font, fill=text_bg_color,
                              align="center", spacing=char_spacing)

                    text_position_x += text_width
        else:
            # Draw the line with white color
            draw.text((text_position_x, text_position_y), line, font=font, fill=font_color_normal,
                      align="center", spacing=char_spacing)

        # Move to the next line position
        text_position_y += line_height + line_spacing
    
    header_text = get_config("header_text")
    header_font = ImageFont.truetype("app_data/ABeeZee-Regular.ttf", 25)
    header_text_width, header_text_height = header_font.getsize(header_text)
    # header_text_position = (30, 30)
    # Calculate the position for the header text (bottom center)
    header_text_position_x = (output_image_size[0] - header_text_width) // 2
    header_text_position_y = output_image_size[1] - header_text_height - 30

    # Draw the header text
    # draw.text((header_text_position_x, header_text_position_y), header_text, font=header_font, fill=font_color_normal)



    logo_path = "app_data/logo (4).png"
    logo_image = Image.open(logo_path)

    # Resize the logo image to 200x25 pixels with antialiasing
    logo_image = logo_image.resize((300, 55), Image.ANTIALIAS)

    # Calculate the position to paste the logo image onto the output image
    logo_position_x = (output_image_size[0] - logo_image.width) // 2
    logo_position_y = output_image_size[1] - logo_image.height - 30  # 20-pixel padding from the bottom

    # Paste the logo image onto the output image
    output_image.paste(logo_image, (logo_position_x, logo_position_y), logo_image)


    # Extract a few words from the title for the filename
    title_words = news.split()[:3]
    # title_words= title_words.replace("/","_")
    filename = "_".join(title_words) + "_01.jpg"

    filename="news/"+filename.replace("*","")

    # Save the resulting image with the modified filename
    output_image.save(filename)
    return filename


def generate_news_image_from_path(image_path, news):
    # Download the source image
    
    source_image = Image.open(image_path)

    # Define the parameters for the text and image generation
    text = news
    font_path = "app_data/Anton-Regular.ttf"
    font_size = 60
    font_color_quote = "#33CC66"
    font_color_normal = "#ffffff"
    text_bg_color = "#00000000"
    padding_bottom = 110
    line_spacing = 13
    char_spacing = -3

    # Create a new blank image
    output_image_size = (1024, 1024)
    output_image = Image.new("RGB", output_image_size)

    # Calculate the scaling factor for the source image
    scaling_factor = max(output_image_size[0] / source_image.width, output_image_size[1] / source_image.height)
    new_image_size = (int(source_image.width * scaling_factor), int((source_image.height) * scaling_factor))

    # Resize the source image with the calculated dimensions
    resized_image = source_image.resize(new_image_size, Image.ANTIALIAS)

    # Calculate the position to paste the resized image onto the output image (centered)
    paste_position = ((output_image_size[0] - resized_image.width) // 2, (output_image_size[1] - resized_image.height) // 2)

    # Paste the resized image onto the output image
    output_image.paste(resized_image, paste_position)

    # Create a gradient overlay
    gradient_height = int(output_image_size[1] * 0.7)  # 50% of the image height
    gradient_width = output_image_size[0]
    gradient = Image.new("L", (gradient_width, gradient_height), color=0)  # Set the color to black
    draw = ImageDraw.Draw(gradient)
    for y in range(gradient_height):
        alpha = int((y / gradient_height) * 255)  # Linear gradient from 0% to 100% opacity
        draw.line((0, y, gradient_width, y), fill=alpha)

    # Resize the gradient overlay to match the size of the output image
    resized_gradient = gradient.resize(output_image_size, Image.ANTIALIAS)

    # Invert the gradient
    resized_gradient = ImageOps.invert(resized_gradient)

    # Create a mask using the resized gradient
    mask = Image.new("L", output_image_size)
    mask.paste(resized_gradient, (0, 0))

    # Apply the mask to the output image
    output_image = Image.composite(output_image, Image.new("RGB", output_image_size), mask)

    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(output_image)

    # Wrap the text into multiple lines
    wrapper = textwrap.TextWrapper(width=39)
    wrapped_text = wrapper.wrap(text)

    # Calculate the height of each line
    line_height = font.getsize(text)[1]

    # Calculate the total height of the wrapped text
    total_text_height = line_height * len(wrapped_text) + line_spacing * (len(wrapped_text) - 1)

    # Calculate the position for the text
    text_position_y = (output_image_size[1] - total_text_height -padding_bottom)

    # Draw each line of the text
    for line in wrapped_text:
        # Calculate the width of the line
        line_width = font.getsize(line)[0]

        # Calculate the position for the line to be centered
        text_position_x = (output_image_size[0] - line_width) // 2

        if "*" in line:
            # Split the line by single quotes
            parts = line.split("*")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Draw the part outside single quotes with white color
                    draw.text((text_position_x, text_position_y), part, font=font, fill=font_color_normal,
                              align="center", spacing=char_spacing)
                    text_position_x += font.getsize(part)[0]
                else:
                    # Draw the part within single quotes with the specified color and background box
                    text_width, text_height = font.getsize(part)
                    bg_width = text_width + 10
                    bg_height = text_height + 10
                    bg_position_x = text_position_x - 5
                    bg_position_y = text_position_y - 5
                    bg_rectangle = [(bg_position_x, bg_position_y),
                                    (bg_position_x + bg_width, bg_position_y + bg_height)]

                    draw.rectangle(bg_rectangle, fill=font_color_quote)
                    draw.text((text_position_x, text_position_y), part, font=font, fill=text_bg_color,
                              align="center", spacing=char_spacing)

                    text_position_x += text_width
        else:
            # Draw the line with white color
            draw.text((text_position_x, text_position_y), line, font=font, fill=font_color_normal,
                      align="center", spacing=char_spacing)

        # Move to the next line position
        text_position_y += line_height + line_spacing
    
    # header_text = get_config("header_text")
    # header_font = ImageFont.truetype("app_data/ABeeZee-Regular.ttf", 25)
    # header_text_width, header_text_height = header_font.getsize(header_text)
    # # header_text_position = (30, 30)
    # # Calculate the position for the header text (bottom center)
    # header_text_position_x = (output_image_size[0] - header_text_width) // 2
    # header_text_position_y = output_image_size[1] - header_text_height - 30

    # Draw the header text
    # draw.text((header_text_position_x, header_text_position_y), header_text, font=header_font, fill=font_color_normal)



    logo_path = "app_data/logo (4).png"
    logo_image = Image.open(logo_path)

    # Resize the logo image to 200x25 pixels with antialiasing
    logo_image = logo_image.resize((300, 55), Image.ANTIALIAS)

    # Calculate the position to paste the logo image onto the output image
    logo_position_x = (output_image_size[0] - logo_image.width) // 2
    logo_position_y = output_image_size[1] - logo_image.height - 30  # 20-pixel padding from the bottom

    # Paste the logo image onto the output image
    output_image.paste(logo_image, (logo_position_x, logo_position_y), logo_image)


    # Extract a few words from the title for the filename
    title_words = news.split()[:3]
    # title_words= title_words.replace("/","_")
    filename = "_".join(title_words) + "_01.jpg"


    filename="news/products/"+filename.replace("*","")

    # Save the resulting image with the modified filename
    output_image.save(filename)
    return filename


def generate_news_image_potraite(image_url, news,image_path):
    # Download the source image
    if(image_url!= ""):
        response = requests.get(image_url)
        source_image = Image.open(BytesIO(response.content))
    
    if(image_path!=None):
        source_image = Image.open(image_path)

    # Define the parameters for the text and image generation
    text = news
    font_path = "app_data/Anton-Regular.ttf"
    font_size = 70
    font_color_quote = "#33CC66"
    font_color_normal = "#ffffff"
    text_bg_color = "#000000"
    padding_bottom = 140
    line_spacing = 13
    char_spacing = -3

    # Create a new blank image
    output_image_size = (1080, 1920)
    output_image = Image.new("RGB", output_image_size)

    # Calculate the scaling factor for the source image
    scaling_factor = max(output_image_size[0] / source_image.width, output_image_size[1] / source_image.height)
    new_image_size = (int(source_image.width * scaling_factor), int(source_image.height * scaling_factor))

    # Resize the source image with the calculated dimensions
    resized_image = source_image.resize(new_image_size, Image.ANTIALIAS)

    # Calculate the position to paste the resized image onto the output image (centered)
    paste_position = ((output_image_size[0] - resized_image.width) // 2, (output_image_size[1] - resized_image.height) // 2)

    # Paste the resized image onto the output image
    output_image.paste(resized_image, paste_position)

    # Create a gradient overlay
    gradient_height = int(output_image_size[1] * 0.9)  # 50% of the image height
    gradient_width = output_image_size[0]
    gradient = Image.new("L", (gradient_width, gradient_height), color=0)  # Set the color to black
    draw = ImageDraw.Draw(gradient)
    for y in range(gradient_height):
        alpha = int((y / gradient_height) * 255)  # Linear gradient from 0% to 100% opacity
        draw.line((0, y, gradient_width, y), fill=alpha)

    # Resize the gradient overlay to match the size of the output image
    resized_gradient = gradient.resize(output_image_size, Image.ANTIALIAS)

    # Invert the gradient
    resized_gradient = ImageOps.invert(resized_gradient)

    # Create a mask using the resized gradient
    mask = Image.new("L", output_image_size)
    mask.paste(resized_gradient, (0, 0))

    # Apply the mask to the output image
    output_image = Image.composite(output_image, Image.new("RGB", output_image_size), mask)

    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(output_image)

    # Wrap the text into multiple lines
    wrapper = textwrap.TextWrapper(width=35)
    wrapped_text = wrapper.wrap(text)

    # Calculate the height of each line
    line_height = font.getsize(text)[1]

    # Calculate the total height of the wrapped text
    total_text_height = line_height * len(wrapped_text) + line_spacing * (len(wrapped_text) - 1)

    # Calculate the position for the text
    text_position_y = (output_image_size[1] - total_text_height -padding_bottom)

    # Draw each line of the text
    for line in wrapped_text:
        # Calculate the width of the line
        line_width = font.getsize(line)[0]

        # Calculate the position for the line to be centered
        text_position_x = (output_image_size[0] - line_width) // 2

        if "*" in line:
            # Split the line by single quotes
            parts = line.split("*")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Draw the part outside single quotes with white color
                    draw.text((text_position_x, text_position_y), part, font=font, fill=font_color_normal,
                              align="center", spacing=char_spacing)
                    text_position_x += font.getsize(part)[0]
                else:
                    # Draw the part within single quotes with the specified color and background box
                    text_width, text_height = font.getsize(part)
                    bg_width = text_width + 10
                    bg_height = text_height + 10
                    bg_position_x = text_position_x - 5
                    bg_position_y = text_position_y - 5
                    bg_rectangle = [(bg_position_x, bg_position_y),
                                    (bg_position_x + bg_width, bg_position_y + bg_height)]

                    draw.rectangle(bg_rectangle, fill=font_color_quote)
                    draw.text((text_position_x, text_position_y), part, font=font, fill=text_bg_color,
                              align="center", spacing=char_spacing)

                    text_position_x += text_width
        else:
            # Draw the line with white color
            draw.text((text_position_x, text_position_y), line, font=font, fill=font_color_normal,
                      align="center", spacing=char_spacing)

        # Move to the next line position
        text_position_y += line_height + line_spacing
    
    # header_text = get_config("header_text")
    # header_font = ImageFont.truetype("app_data/ABeeZee-Regular.ttf", 35)
    # header_text_width, header_text_height = header_font.getsize(header_text)
    # header_text_position = (40, 40)

    # draw.text(header_text_position, header_text, font=header_font, fill=font_color_normal)

    logo_path = "app_data/logo (4).png"
    logo_image = Image.open(logo_path)

    # Resize the logo image to 200x25 pixels with antialiasing
    logo_image = logo_image.resize((400, 65), Image.ANTIALIAS)

    # Calculate the position to paste the logo image onto the output image
    logo_position_x = (output_image_size[0] - logo_image.width) // 2
    logo_position_y = output_image_size[1] - logo_image.height - 30  # 20-pixel padding from the bottom

    # Paste the logo image onto the output image
    output_image.paste(logo_image, (logo_position_x, logo_position_y), logo_image)



    # Extract a few words from the title for the filename
    title_words = news.split()[:3]
    # title_words= title_words.replace("/","_")
    filename = "_".join(title_words) + "_01.jpg"

    filename="news/stories/"+filename.replace("*","")

    # Save the resulting image with the modified filename
    output_image.save(filename)
    return filename