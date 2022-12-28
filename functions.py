import numpy as np
import matplotlib.pyplot as plt
import random

def fourier_transform_shift(img):
    img_fft= np.fft.fftshift(np.fft.fft2(img))
    img_magnitude = np.sqrt(np.real(img_fft) ** 2 + np.imag(img_fft) ** 2)
    img_phase = np.arctan2(np.imag(img_fft), np.real(img_fft))
    return img_fft,img_magnitude,img_phase

def reconstruct_image(mag,phase):
    img_comb = np.multiply(mag, np.exp(1j * phase))
    resulting_img= np.real(np.fft.ifft2(np.fft.ifftshift(img_comb)))
    return resulting_img

def plot_magnitude(img_magnitude):
    plt.figure(figsize=[15, 8])
    plt.imshow(np.log(img_magnitude+1e-10), cmap='gray')
    path = f'static/img/magnitude{random.randint(1,10000)}.jpg'
    plt.savefig(path)
    plt.close()
    return path

