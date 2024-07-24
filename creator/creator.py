from PIL import Image

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
    
    # Save the new image
    img.save(output_path, "PNG")
    print(f"New icon saved as {output_path}")


input_file = "./test.png"  # Replace with your input file name
output_file = "pink_icon.png"  # Replace with your desired output file name
pink_color = (255, 5, 141)  # RGB values for pink (you can change this)


change_icon_color(input_file, output_file, pink_color)