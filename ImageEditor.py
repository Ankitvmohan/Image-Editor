from PIL import Image, ImageEnhance, ImageFilter
import os
path = "./imgs" # folder for unedited images
pathOut = "./editedImgs" # folder for edited images
# Check if the output directory exists; if not, create it
if not os.path.exists(pathOut):
    os.makedirs(pathOut)
for filename in os.listdir(path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')): # Check for image files
        img = Image.open(os.path.join(path, filename))
        # Sharpening and converting to black and white
        edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)
        # Adjust contrast
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)
        # ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/
        clean_name = os.path.splitext(filename)[0]
        edit.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))
print("Editing complete.")