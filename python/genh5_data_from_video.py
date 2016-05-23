# -*-coding=utf-8-*-
import h5py, os
import caffe
import numpy as np
import skimage.io as skio
import img_mani
import label_file_util as label_util
import random
import cv2
import time

ROOT = 'C:\\Users\\zhang\\Documents\\caffe-tools\\data\\3dcnn'
PHASE = 'train'
LABEL_FILE = 'C:\\Users\\zhang\\Documents\\caffe-tools\\data\\3dcnn\\' + PHASE + '.proto'

SIZE = 170 # fixed size to all images
HD5SIZE = 800
INI_VALUE = -1000
FRAMES = 5


def swap_caffe_axies(narray):
    narray = np.swapaxes(narray, 0, 2)
    narray = np.swapaxes(narray, 1, 2)
    return narray


def caffe_format_img(img):
    img = caffe.io.resize(img, (SIZE, SIZE, 3)) # resize to fixed size
    img = swap_caffe_axies(img)
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


def write_XY_h5(h5name, X, y, shuffle=False):
    if shuffle:
        randidx = np.random.permutation(X.shape[0])
        X = X[randidx]
        y = y[randidx]
    with h5py.File(h5name, 'w') as H:
        H.create_dataset('X', data=X)
        H.create_dataset('y', data=y)


def resize_batch(imgs):
    for i, img in enumerate(imgs):
        imgs[i] = caffe.io.resize(img, (SIZE, SIZE, 3))
    return imgs


def augment_img(img):
    #augment here
    img_augs = img_mani.augment_image(img)
    img_augs.append(img)
    img_augs = resize_batch(img_augs)
    img_augs = np.stack(img_augs)
    return img_augs

def get_empty_XY():
    X = np.empty(shape=(0, 3, SIZE, SIZE))
    y = np.empty(shape = 0)
    return X, y

def write_h5names(filename, h5name_list):
    with open(filename, 'w') as L:
        for name in h5name_list:
            L.write(name + '\n' ) # list all h5 files you are going to use


def save_batch(name_seed, imgs, additional_name_info=[]):
    temp_dir = './_temp/'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    name, _ = os.path.splitext(name_seed)
    for i, img in enumerate(imgs):
        skio.imsave(temp_dir + os.sep + additional_name_info + '-{}-{}.bmp'.format(name, i), img)


def shuffleL1L2(a, b):
    combined = zip(a, b)
    random.shuffle(combined)

    a[:], b[:] = zip(*combined)
    return a, b

def read_video(file):
    if file is False:
        return
    video = cv2.VideoCapture(file)
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        size = (int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
                int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
        print "Frames size: {0}".format(size)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
        print "Frames size: {0}".format(size)
    num_frames = FRAMES;
    print "Capturing {0} frames".format(num_frames)
    start = time.time()
    images = []
    for i in xrange(0, num_frames):
        ret, frame = video.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        images.append(frame)
    end = time.time()
    seconds = end - start
    print "Time taken : {0} seconds".format(seconds)
    video.release()
    return images

def convert2h5data():
    Xs, ys = get_empty_XY()
    count = 0
    h5name_record = []
    '''if os.path.splitext(LABEL_FILE)[1] == '.txt':
        file_list, score_list = label_util.load_old_format_labelscore(LABEL_FILE)
    if os.path.splitext(LABEL_FILE)[1] == '.proto':
        file_list, score_list = label_util.get_name_score_from_proto(LABEL_FILE)'''
    file_list, score_list = label_util.load_gt_sep(LABEL_FILE)
    file_list, score_list = shuffleL1L2(file_list, score_list)

    for path, y in zip(file_list, score_list):
        video_path = ROOT + '/' +path
        if not os.path.exists(video_path):
            print 'not exost:' + video_path
            continue
        print 'processing '+ str(count) + ':' + video_path
        imgs = read_video(video_path)
        imgs = resize_batch(imgs)
        imgs = np.stack(imgs)
        if imgs == []:
            continue
        dice = np.random.rand()
        if dice > 0.95:
            save_batch(os.path.split(video_path)[1], imgs, additional_name_info=str(y))
        imgs = np.swapaxes(imgs, 1, 3)
        imgs = np.swapaxes(imgs, 2, 3)
        y = np.repeat(y, imgs.shape[0], axis=0)
        Xs = np.vstack([Xs, imgs])
        ys = np.hstack([ys, y])
        count += 1
        if Xs.shape[0] >= HD5SIZE:
            write_XY_h5(ROOT + os.sep + PHASE + str(count) + '.h5', Xs, ys, shuffle=True)
            h5name_record.append(ROOT + os.sep + PHASE + str(count) + '.h5')
            Xs, ys = get_empty_XY()

    # in case number of last batch of X,y is smaller than HD5SIZE
    write_XY_h5(ROOT + os.sep + PHASE + str(count) + '.h5', Xs, ys, shuffle=True)
    h5name_record.append(ROOT + os.sep + PHASE + str(count) + '.h5')
    write_h5names(ROOT + os.sep + PHASE + '_h5_list.txt', h5name_record)

if __name__ == '__main__':
    convert2h5data()