import os
from fpdf import FPDF
from PIL import Image

def save_carousel_images_as_pdf(category,output_folder='news_latters'):
    # Get the list of carousel images from the "/news" folder
    carousel_images = sorted([f for f in os.listdir('news') if f.endswith('.jpg') or f.endswith('.png')])

    # Determine the maximum dimensions of the images news/00_news_latter_title.png
    max_width = 0
    max_height = 0
    for image in carousel_images:
        if(carousel_images.index(image)==0):
            img = Image.open(os.path.join('news', "00_news_latter_title.png"))
        else:
            img = Image.open(os.path.join('news', image))
        width, height = img.size
        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height

    # Create PDF object with adjusted dimensions
    pdf = FPDF(unit='pt', format=(max_width, max_height))

    # Add each image to the PDF
    for image in carousel_images:
        pdf.add_page()
        pdf.image(os.path.join('news', image), x=0, y=0, w=max_width, h=max_height)

    # Generate the filename with a date and timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_filename = f"{category} News Weekly Digest {timestamp}.pdf"

    # Save the PDF
    pdf.output(os.path.join(output_folder, pdf_filename), 'F')
    print("Carousel images saved as PDF successfully!")


