import numpy as np
import matplotlib.pyplot as plt
import random
import cv2

class Image:
    
    takenMag = 0
    takenPhase = 0
    
    def __init__(self,spatialDomainData):
        self.spatialDomainData = spatialDomainData

    def getfft(self):
        return np.fft.fft2(self.spatialDomainData)
    
    def getfftshift(self):
        return np.fft.fftshift(self.getfft())
    def getMag(self):
        return np.sqrt(np.real(self.getfftshift()) ** 2 + np.imag(self.getfftshift()) ** 2)
    def getPhase(self):
        return np.arctan2(np.imag(self.getfftshift()), np.real(self.getfftshift()))
    def getPathOfMagOrPhasePlot(self,magTPhaseF):
        plt.figure(figsize=[15, 8])
        
        if magTPhaseF:
            plt.imshow(np.log(self.getMag()+1e-10), cmap='gray')
            name = f'magnitude{random.randint(1,10000)}.jpg'
        else:
            plt.imshow((self.getPhase()), cmap='gray')
            name = f'phase{random.randint(1,10000)}.jpg'
        path = f'static/assets/{name}'
        plt.savefig(path)
        plt.close()
        return path
    
    @staticmethod
    def mixMagAndPhase(mag,phase):
        img_comb = np.multiply(mag, np.exp(1j * phase))
        resulting_img= np.real(np.fft.ifft2(np.fft.ifftshift(img_comb)))
        return resulting_img
    
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
    
    
    # plt.figure(figsize=[15, 8])
    # plt.imshow(np.log(img_magnitude+1e-10), cmap='gray')
    name = f'magnitude{random.randint(1,10000)}.jpg'
    path = f'static/assets/{name}'
    cv2.imwrite(path,20*np.log(np.abs(img_magnitude)))
    # plt.savefig(path)
    # plt.close()
    return name

def plot_phase(img_phase):
    plt.figure(figsize=[8, 4])
    plt.imshow((img_phase), cmap='gray')
    path = f'static/img/phase{random.randint(1,10000)}.jpg'
    plt.savefig(path)
    plt.close()
    return path

