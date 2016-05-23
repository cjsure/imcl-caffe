import numpy as np
import skimage.transform as sktrans
import skimage.io as skio

IMG = "C:\\Users\\zhang\\Pictures\\Camera Roll\\10.jpg"

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

def test():
    image = skio.imread(IMG)
    imgs = augment_image(image)
    for i in imgs:
        skio.imshow(i)
        skio.show()
    imgs = np.swapaxes(imgs, 1, 3)
    imgs = np.swapaxes(imgs, 2, 3)



if __name__ == '__main__':
    test()