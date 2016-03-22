 # -*- coding: UTF-8 -*-
import csv
import numpy as np
from scipy import stats
import label_file_util as label_util
from predict2 import intersect
import string
from itertools import islice

GROUND_TRUTH = 'D:/Project/caffe-windows-master/data/Blur2000/test.proto'

def format_float(s):
    f = string.atof(s)
    f = f * 0.01
    return  f

def calc_corr(score_file):
    file = csv.reader(open(score_file, 'rb'))
    score = {}
    for line in file:
         [file_id, file_name, file_score] = line
         score[file_name] = float(file_score)
    gt = label_util.load_gt_dict(GROUND_TRUTH, split_name=True)
    inter_score, inter_gt, interkey = intersect(score, gt)
    sorted_ind = np.argsort(inter_gt)
    inter_gt = inter_gt[sorted_ind]
    inter_score = inter_score[sorted_ind]
    interkey = interkey[sorted_ind]

    [rho, p_value] = stats.spearmanr(inter_score, inter_gt)
    print rho

def calc_corr_str(score_file):
    file = csv.reader(open(score_file, 'r'))
    score = {}
    for line in islice(file, 1, None):
         [file_id, file_name, file_score] = line
         score[file_name] = float(file_score)
    gt = label_util.load_gt_dict(GROUND_TRUTH, split_name=True)
    inter_score, inter_gt, interkey = intersect(score, gt)
    sorted_ind = np.argsort(inter_gt)
    inter_gt = inter_gt[sorted_ind]
    inter_score = inter_score[sorted_ind]
    interkey = interkey[sorted_ind]

    [rho, p_value] = stats.spearmanr(inter_score, inter_gt)
    print rho
if __name__ == '__main__':
     calc_corr('predict_result.csv')
     calc_corr_str('only_blur.csv')
     calc_corr_str('3com_score.csv')