import caffe
import numpy as np
import glob
import os
import shutil

#caffe_root = './caffe'
NET_FILE = 'D:\\Project\\caffe-windows-master-zhangjunhui\\models\\status\\1-0\\train_val-deploy.prototxt'
PARAM_FILE = 'D:\\Project\\caffe-windows-master-zhangjunhui\\models\\status\\1-0\\alexnet_train2016011161007_iter_29593.caffemodel'
#img_path = 'D:/Project/caffe-windows-master/data/Blur1000/test/132.BMP'
IMAGE_ROOT = 'D:/Project/caffe-windows-master-zhangjunhui/data/Blur5000/normal/'
#dst_path = 'D:/Project/caffe-windows-master-zhangjunhui/data/Blur5000/'
DST_PATH = 'D:/Project/caffe-windows-master-zhangjunhui/data/Blur5000/'
DIRT = 'dirt.txt'
PURE = 'pure.txt'
SCORE = 'score.txt'

SZ = 170
back_end = '*.bmp'
debug = False
debug_num = -100

caffe.set_mode_gpu
net = caffe.Net(NET_FILE, PARAM_FILE, caffe.TEST)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))

def predict(image_path):
    net.blobs['data'].reshape(1, 3, SZ, SZ)
    net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(image_path))
    out = net.forward()
    return np.squeeze(out.values())

def predict_batch(image_dir):
    name_list = glob.glob(image_dir + os.sep + back_end)
    file_list = []
    score_list = []
    import time

    if debug:
        name_list = name_list[debug_num:]

    for path in name_list:
        print 'predicting {}'.format(path)
        name = os.path.split(path)[1]
        tStart = time.time()
        score = predict(path)
        tEnd = time.time()
        print "It cost %f sec" % (tEnd - tStart)
        file_list.append(name)
        score_list.append(np.min((np.max((score, 0)), 1)))
        print "score:%f" % score
    return file_list, score_list

def gen_filelist_txt(image_dir):
    path_list = glob.glob(image_dir + os.sep + back_end)
    name_score = []
    for path in path_list:
        name_score.append(str(os.path.split(path)[1])+' '+str(1))
    for line in name_score:
        print line

def gen_file_score_txt():
    file_list, score_list = predict_batch(IMAGE_ROOT)
    name_score = []
    for i in range(len(score_list)):
        name_score.append(str(file_list[i])+' '+str(score_list[i])+'\n')
    file(DST_PATH+SCORE, 'w').writelines(name_score)
    return file_list, score_list

def load_old_format_labelscore(file_path):
    with open(file_path, 'r') as T:
        lines = T.readlines()
    img_name = []
    score = []
    for line in lines:
        sp = line.split(' ')
        img_name.append(sp[0])
        score.append(float(sp[1]))
    return img_name, score

def gen_pure_dirt_txt(file_path):
    file_list, score_list = load_old_format_labelscore(file_path)
    pure_file_list = []
    dirt_file_list = []
    dirt_tmp = []
    pure_tmp = []
    for i in range(len(score_list)):
        if score_list[i] >= 0.95:
            pure_file_list.append(file_list[i])
            pure_tmp.append(str(file_list[i])+' '+str(score_list[i])+'\n')
        if score_list[i] < 0.8:
            dirt_file_list.append(file_list[i])
            dirt_tmp.append(str(file_list[i])+'\n')
    file(DST_PATH+PURE, 'w').writelines(pure_tmp)
    file(DST_PATH+DIRT, "w").writelines(dirt_tmp)
    return pure_file_list, dirt_file_list

def move_file(file_path):
    pure_file_list, dirt_file_list = gen_pure_dirt_txt(file_path)
    index = 0
    for file in pure_file_list:
        shutil.move(IMAGE_ROOT+file,DST_PATH+'pure/'+file)#copyfile&move test and practice
        index = index + 1
        print "file:"+str(index)
    for file in dirt_file_list:
        shutil.move(IMAGE_ROOT+file,DST_PATH+'dirt/'+file)#copyfile&move test and practice
        index =index + 1
        print "file:"+str(index)

if __name__ == '__main__':
    move_file(DST_PATH+SCORE)
#    gen_filelist_txt(IMAGE_ROOT)
