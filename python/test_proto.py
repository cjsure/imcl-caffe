import caffe
import os
import matplotlib.pyplot as plt
import conf_pb2
from google.protobuf import text_format

img = 'D:\Project\caffe-windows-master-zhangjunhui\data\Blur2000\\test\\2.bmp'

SIZE = 170

def caffe_format_img(img):
    img = caffe.io.resize(img, (SIZE, SIZE, 3)) # resize to fixed size
    return img


def load_image(img_path):
    if not os.path.exists(img_path):
        print '\tfile not exist {}'.format(img_path)
        return False
    img = caffe.io.load_image(img_path)
    return img

def load_caffe_format_img(img_path):
    img = load_image(img_path)
    return caffe_format_img(img)

def show_image(img_path):
    img = plt.imread(img_path)
    plt.imshow(img)
    plt.show()
    img = load_caffe_format_img(img_path)
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    show_image(img)