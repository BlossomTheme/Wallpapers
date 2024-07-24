from PIL import Image
import os 

def create_wallpaper(image, output_path):
    bg = Image.new(mode = "RGB", size = (1920, 1080), color = (16, 17, 27))

    bg_width, bg_height = bg.size
    ov_width, ov_height = image.size
    
    x = (bg_width - ov_width) // 2
    y = (bg_height - ov_height) // 2

    bg.paste(image, (x, y), image)

    # Save the new image
    bg.save(output_path, "PNG")
    print(f"New wallpaper saved as {output_path}")

def change_icon_color(input_path, output_path, new_color):
    # Open the image
    img = Image.open(input_path)
    
    # Convert the image to RGBA if it's not already
    img = img.convert("RGBA")
    
    # Get the image data
    data = img.getdata()
    
    # Create a new list for the modified pixels
    new_data = []
    
    # Process each pixel
    for item in data:
        # If the pixel is not transparent (alpha > 0)
        if item[3] > 0:
            # Replace it with the new color, keeping the original alpha
            new_data.append(new_color + (item[3],))
        else:
            # Keep fully transparent pixels as is
            new_data.append(item)
    
    # Update the image with new data
    img.putdata(new_data)
    
    create_wallpaper(img, output_path)

def process_folder(input_folder, output_folder, new_color):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"blossom_{filename}")
            change_icon_color(input_path, output_path, new_color)

input_folder = "./icons"  # Replace with your input folder path
output_folder = "./output"  # Replace with your desired output folder path
pink_color = (255, 5, 141)  # RGB values for pink (you can change this)

process_folder(input_folder, output_folder, pink_color)