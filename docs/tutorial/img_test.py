import numpy as np
import skimage.io as skio
import skimage.transform as sktrans

def flip(image):
    image1 = np.flipud(image)
    image2 = np.fliplr(image)
    return [image1, image2]

def rotate(image):
    angle = 5;
    image1 = sktrans.rotate(image, angle)
    image2 = sktrans.rotate(image, -angle)
    return [image1, image2]

def augment_image(image):
    images = []
    images.extend(flip(image))
    images.extend(rotate(image))
    return images

def process():
    image_dir = 'D:/Project/caffe-windows-master/data/Blur1000/test/2.bmp'
    image = skio.imread(image_dir)
    images = augment_image(image)
    for i, im in enumerate(images):
        skio.imsave(str(i)+'.bmp', im)
        skio.imshow(images[i])
        skio.show()

if __name__ == '__main__':
    process()
    pass