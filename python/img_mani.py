import os
import numpy as np
import skimage.io as skio
import skimage.transform as sktrans
import skimage.util as skutil
from skimage.morphology import square
from skimage.filters import rank
import skimage.data as skdata
from skimage import img_as_float

def is_more_than_720(image):
    height = image.shape[0]
    if height >= 720:
        return True

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


def crop_center(image):
    if not is_more_than_720(image) :
        return []
    height, width, _ = image.shape
    if width < height:  # very rare case
        return []
    x_margin = width - height
    return skutil.crop(image,((0, 0), (x_margin/2, x_margin/2), (0, 0)))


def filter_img(img):
    selem = square(11)
    img[:, :, 0] = rank.mean(img[:, :, 0], selem=selem)
    img[:, :, 1 ] = rank.mean(img[:, :, 1], selem=selem)
    img[:, :, 2] = rank.mean(img[:, :, 2], selem=selem)
    #return np.array(img, dtype=float)
    return img_as_float(img)


def preprocess(image):
    center_img = crop_center(image)
    return center_img


def compute_image_mean(image_dir, ext, size, ndim=3, show=False):
    if len(size) != ndim:
        print 'dim of size should be equal to ndim'
        return -1

    import os
    img_mean = np.zeros(size)
    img_num = 0
    for name in os.listdir(image_dir):
        _, file_ext = os.path.splitext(name)
        if not ext == file_ext:
            continue
        image_fullpath = os.path.join(image_dir, name)
        img = skio.imread(image_fullpath)
        if img.ndim !=  3:
            continue
        img = sktrans.resize(img, size)
        img_mean += img * 1.0
        img_num += 1
    img_mean = img_mean / img_num
    if show:
        skio.imshow(img_mean)
        skio.show()
    return img_mean


def test1():
    image_path = 'D:/Project/caffe-windows-master/data/Blur1000/test/000000000001.BMP'
    image = skio.imread(image_path)
    images = augment_image(image)
    for i, im in enumerate(images):
        skio.imsave(str(i)+'.bmp', im)


def test2():
    image_path = 'D:/Project/caffe-windows-master/data/Blur1000/test/000000000001.BMP'
    image = skio.imread(image_path)
    img_center = crop_center(image)
    if img_center != []:
        skio.imsave('center.bmp', img_center)


def test_filter_img():
    lena = skdata.lena()
    blurlena = filter_img(lena)
    skio.imshow(blurlena)
    skio.show()

if __name__ == '__main__':
    # test_filter_img()
    image_dir = 'D:/Project/caffe-windows-master/data/Blur1000/test/'
    ext = '.bmp'
    # compute_image_mean(image_dir, ext, size, ndim=3, show=False):
    pass