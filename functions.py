import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
#michael
class Image:
    
    takenMag = 1
    
    def __init__(self,spatialDomainPath,takenInOrOut = 1):
        self.spatialDomainPath = spatialDomainPath
        self.takenInOrOut = takenInOrOut
    
    def toggleInOrOut(self):
        self.takenInOrOut = not self.takenInOrOut
    
    def getSpatialDomainData(self):
        return cv2.imread(self.spatialDomainPath,0)
    def getfft(self):
        return np.fft.fft2(self.getSpatialDomainData())
    
    def getfftshift(self):
        return np.fft.fftshift(self.getfft())
    
    def getInverShift(self):
        return np.fft.ifftshift(self.getfftshift())
    def getInverseFourier(self):
        return np.fft.ifft2(self.getInverShift())
    
    def getMag(self):
        return np.sqrt(np.real(self.getfftshift()) ** 2 + np.imag(self.getfftshift()) ** 2)
    
    def getPhase(self):
        return np.angle(self.getfftshift())
        # return np.arctan2(np.imag(self.getfftshift()), np.real(self.getfftshift()))
    
    def scale(self,image_array):
        image=((image_array - image_array.min()) * (1/(image_array.max() - image_array.min()) * 255)).astype('uint8')
        return image
    
    def getMask(x,y,width,height,inverse):
        x = int(float(x))
        y = int(float(y))
        height = int(float(height))
        width = int(float(width))
        mask = np.zeros((281,180),np.uint8)
        # mask[crow-30:crow+30, ccol-30:ccol+30] = 1
    
    def getMasked(self,x,y,width,height,inverse,magTPhaseF):
        
        if magTPhaseF:
            masked = self.getMag()
        else:
            masked = self.getPhase()
        # masked = self.getfftshift()
        rows, cols = self.getSpatialDomainData().shape
        for i in range(rows):
            for j in range(cols):
                inRect = Image.inRect(i,j,x,y,width,height)
                if inverse:
                    if inRect:
                        masked[i][j] = 0
                else:
                    if not inRect:
                        masked[i][j] = 0
        # masked = np.fft.ifftshift(masked)
        print('masked')
        return masked
    def combine(fourierToMag,fourierToPhase):
        combined = np.multiply(np.abs(fourierToMag), np.exp(1j*np.angle(fourierToPhase)))
        newInSpatial = np.fft.ifft2(combined)
        img_back = np.real(np.fft.ifft2(newInSpatial))
        img_back = np.abs(newInSpatial)
        
        name = f'result{random.randint(1,10000)}.jpg'
        path = f'static/assets/{name}'
        cv2.imwrite(path,img_back)
        print('combined')
        print(path)
        return path
    def getPathOfMagOrPhasePlot(self,magTPhaseF):
        # if 1 get mag if 0 get phase
        if magTPhaseF:
            name = f'magnitude{random.randint(1,10000)}.jpg'
        else:
            name = f'phase{random.randint(1,10000)}.jpg'
        path = f'static/assets/{name}'
        if magTPhaseF:
            cv2.imwrite(path,20*np.log(np.abs(self.getMag())))
        else:
            cv2.imwrite(path,self.scale(self.getPhase()))
        return name
    
    @staticmethod
    def mixMagAndPhase(mag,phase):
        img_comb = np.multiply(mag, np.exp(1j * phase))
        resulting_img= np.real(np.fft.ifft2(np.fft.ifftshift(img_comb)))
        name = f'result{random.randint(1,10000)}.jpg'
        path = f'static/assets/{name}'
        
        cv2.imwrite(path,resulting_img)
        return path
    @staticmethod
    def inRect(xi,yi,x,y,width,height):
        if xi > x and xi < x+width and yi > y and yi < y + height:
            return True
        return False

 
 
    
    
#not needed any more    
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

