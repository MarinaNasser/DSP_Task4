from PIL import image #pip install Pillow

def crop(image_path, coords, saved_location):
    """
    @param image_path: the path to the image to edit
    @param coords: a tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: path to save the cropped image
    """
    image_obj = image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()

