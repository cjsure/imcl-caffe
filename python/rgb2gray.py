# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
import skimage.io as skio


def read_img(img_path):
    # 读取图片,灰度化，并转为数组
    im = array(Image.open(img_path).convert('L'))
    skio.imshow(im)
    skio.show()

if __name__ == '__main__':
    read_img('C:\\Users\\zhang\\Pictures\\Camera Roll\\10.jpg')