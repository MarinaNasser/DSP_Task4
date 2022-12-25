import numpy as np
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

def fourier_transform_shift(img):
    img_fft= np.fft.fftshift(np.fft.fft2(img))
    img_magnitude = np.sqrt(np.real(img_fft) ** 2 + np.imag(img_fft) ** 2)
    img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
    return img_fft,img_magnitude,img_phase

def reconstruct_image(mag,phase):
    img_comb = np.multiply(mag, np.exp(1j * phase))
    resulting_img= np.real(np.fft.ifft2(np.fft.ifftshift(img_comb)))
    return resulting_img

