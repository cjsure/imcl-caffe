import caffe
import numpy as np
import os
import glob
from scipy import stats
import label_file_util as label_util
import matplotlib.pyplot as plt
import datetime
import time
import csv

#caffe_root = './caffe'
NET_FILE = 'D:\\Project\\caffe-windows-master-zhangjunhui\\models\\bvlc_alexnet-sur\\train_val-deploy.prototxt'
PARAM_FILE = 'D:\\Project\\caffe-windows-master-zhangjunhui\\models\\bvlc_alexnet-sur\\alexnet_train201605051021_iter_5000.caffemodel'
#img_path = 'D:/Project/caffe-windows-master/data/Blur1000/test/132.BMP'
IMAGE_ROOT = 'D:/Project/caffe-windows-master-zhangjunhui/data/gray/gray/'
GROUND_TRUTH = 'D:/Project/caffe-windows-master-zhangjunhui/data/gray/test.proto'
SZ = 170#227|170
debug = False
debug_num = -100
back_end = '*.jpg'

###################################set mode
caffe.set_mode_gpu()
net = caffe.Net(NET_FILE, PARAM_FILE, caffe.TEST)
# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
#transformer.set_mean('data', np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)) # mean pixel
#transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
#transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB

def predict(image_path):
    net.blobs['data'].reshape(1, 3, SZ, SZ)
    net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(image_path))
    out = net.forward()
    return np.squeeze(out.values())


def predict_batch(image_dir):
    name_list = glob.glob(image_dir + os.sep + back_end)
    score_record = {}
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
        score_record[name] = np.min((np.max((score, 0)), 1))
        print "score:%f" % score_record[name]
    return score_record


def intersect(dict1, dict2):
    if len(dict1) < len(dict2):
      inter = dict.fromkeys([x for x in dict1 if x in dict2])
    else:
      inter = dict.fromkeys([x for x in dict2 if x in dict1])
    v1 = []
    v2 = []
    interkey = []
    for key in inter:
        v1.append(float(dict1[key]))
        v2.append(dict2[key])
        interkey.append(key)
    return [np.array(v1), np.array(v2), np.array(interkey)]


def timestamp():
    ts = time.time()
    stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    return stamp

def test_case1():
    dict1={'a' : 1, 'b' : 2}
    dict2={'c' : 1, 'b' : 2}
    v1, v2 = intersect(dict1, dict2)
    print stats.spearmanr(v1, v2)[0]

def process():
    score = predict_batch(IMAGE_ROOT)
    #gt = label_util.load_groundtruth(GROUND_TRUTH)
    gt = label_util.load_gt_dict(GROUND_TRUTH, split_name=True)
    inter_score, inter_gt, interkey = intersect(score, gt)
    sorted_ind = np.argsort(inter_gt)
    inter_gt = inter_gt[sorted_ind]
    inter_score = inter_score[sorted_ind]
    interkey = interkey[sorted_ind]
    csvfile = file('predict_result.csv', 'wb')
    writer = csv.writer(csvfile)
    data = []
    for i, (v1, v2, key) in enumerate(zip(inter_score, inter_gt, interkey)):
        data.append([i,key,v1])
    writer.writerows(data)
    [rho, p_value] = stats.spearmanr(inter_score, inter_gt)
    fig = plt.figure()

    gt_handle,  = plt.plot(inter_gt, 'ko')
    score_handle, = plt.plot(inter_score, 'mo')
    plt.title('srocc: {}'.format(rho))
    plt.legend([score_handle, gt_handle], ['pred', 'ground truth'], loc=4)
    plt.ylim(-0.1, 1.1)
    plt.xlabel('#image')
    plt.ylabel('score and gt')
    plt.show()
    fig_dir, model_name = os.path.split(PARAM_FILE)
    stamp = str(timestamp())
    fig.savefig(fig_dir + os.sep + model_name + stamp + '.png', dpi=fig.dpi)
    fig.savefig(fig_dir + os.sep +  model_name + stamp + '.eps', dpi=fig.dpi)
    #os.system('pause')

if __name__ == '__main__':
    process()


