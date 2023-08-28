# import os
# import subprocess

# def create_video(stories_dir, videos_dir):
#     # Get the list of image files in the stories directory
#     image_files = [f for f in os.listdir(stories_dir) if f.endswith('.jpg') or f.endswith('.png')]
#     image_files.sort()  # Sort the files alphabetically

#     # Create a list to store the images with delay
#     images_with_delay = []

#     # Iterate over each image and add it to the list with a delay
#     for image_file in image_files:
#         image_path = os.path.join(stories_dir, image_file)

#         # Add the image multiple times with a delay
#         for _ in range(5):  # Add a delay of 5 seconds
#             images_with_delay.append(image_path)

#     # Set the output video path
#     output_path = os.path.join(videos_dir, 'output.mp4')

#     # Create the command for generating the video using ImageMagick
#     command = [
#         'convert',  # ImageMagick command
#         '-delay', '500',  # Delay between frames in milliseconds (500 = 0.5 seconds)
#         '-loop', '0',  # Loop the animation
#         *images_with_delay,
#         output_path
#     ]

#     # Execute the command
#     subprocess.run(command)

#     print(f"Video created: {output_path}")


# # Provide the directory paths
# stories_dir = "news/stories"
# videos_dir = "news/videos"

# # Call the function to create the video
# create_video(stories_dir, videos_dir)


import re


def extract_tags(text):
    excluded_words = ['says', 'it', 'is', 'he', 'be', 'and', 'of']
    pattern = r'\b(?!' + '|'.join(excluded_words) + r')\w+\b'
    tags = re.findall(pattern, text)
    return tags

text = 'Tesla boss says xAI will be ‘pro-humanity’ and admits development of large systems cannot be pausedElon Musk has launched an artificial intelligence startup that will be “pro-humanity”, as he warned that the world needed to worry about the prospect of a “term…'
tags = extract_tags(text)
print(tags)
