import os
import numpy as np
import skimage.io as skio
import conf_pb2
from google.protobuf import text_format
import skimage.transform as sktrans
import skimage.util as skutil
from skimage.morphology import square
from skimage.filters import rank
import skimage.data as skdata
from skimage import img_as_float

IMAGE_PATH = 'D:/Project/caffe-windows-master-zhangjunhui/data/Blur5000-/'
FILE_PATH = 'D:/Project/caffe-windows-master-zhangjunhui/data/Blur5000-/blur.proto'
DST_PATH = 'D:/Project/caffe-windows-master-zhangjunhui/data/Blur5000-/gen/'
DST_FILE = "aug_img.txt"

def flip(image):
    image1 = np.flipud(image)
    image2 = np.fliplr(image)
    return [image1, image2]

def augment_image(image):
    images = []
    images.extend(flip(image))
    return images

def read_proto_file(file_path, parser_object):
    file = open(file_path, "r")
    text_format.Merge(str(file.read()), parser_object)
    file.close()
    return parser_object

def get_name_score_from_proto(file_path):
    app_config = conf_pb2.AppConfig()
    read_proto_file(file_path, app_config)
    name = []
    score = []
    for f in app_config.filelist.file:
        name.append(f.name)
        score.append(f.gold_score)
    return name, score

def process(file_path):
    file_list, score_list = get_name_score_from_proto(file_path)
    tmp = []
    for k in range(len(file_list)):
        image = skio.imread(IMAGE_PATH + "blur/" + str(file_list[k]))
        images = augment_image(image)
        for i, im in enumerate(images):
            skio.imsave(DST_PATH + str(file_list[k]).split('.')[-2] + '(' + str(i) + 'z)' + '.bmp', im)
            print DST_PATH + str(file_list[k]).split('.')[-2] + '(' + str(i) + 'z)' + '.bmp'
            tmp.append(str(file_list[k]).split('.')[-2] + '(' + str(i) + 'z)' + '.bmp' + ' ' + str(score_list[k]) + '\n')
            #skio.imshow(im)
            skio.show()
    file(DST_PATH + DST_FILE, "w").writelines(tmp)


if __name__ == '__main__':
    process(FILE_PATH)