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
    

# Example usage
input_file = "./test.png"  # Replace with your input file name
output_file = "pink_icon.png"  # Replace with your desired output file name
pink_color = (255, 5, 141)  # RGB values for pink (you can change this)

change_icon_color(input_file, output_file, pink_color)