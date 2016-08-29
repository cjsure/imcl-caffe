#-*- coding:UTF-8 -*-
#############################################################################
# Plotting ROC curve
#############################################################################
import sys
import os
from operator import itemgetter
import matplotlib.pyplot as plt

def LoadActives(fname):
    actives = []
    for line in open(fname, 'r').readlines():
        id = line.strip()
        actives.append(id)
    return actives

def LoadScores(fname):
    sfile = open(fname, 'r')
    label = sfile.readline()
    label = label.strip()
    scores = []
    for line in sfile.readlines():
        id, score = line.strip().split()
        scores.append((id, float(score)))
    return label, scores


def GetRates(predict, truth):
    tpr = [0.0]  # true positive rate
    fpr = [0.0]  # false positive rate
    nexamples = len(truth)
    foundactives = 0.0
    founddecoys = 0.0
    threshhold = 0.0
    best_threshhold = 0.0
    flag_threshhold = 0.0
    distense = 0.0
    min_dist = 0.0
    while(threshhold <= 1.0):
        threshhold = threshhold + 0.01
        for name in truth:
            if (predict[name] > threshhold) and (truth[name] > threshhold):
                foundactives += 1.0#计算真正预测个数
            if((predict[name] > threshhold)) and (truth[name] < threshhold):
                founddecoys += 1.0#计算假正预测个数
        tp = foundactives / float(nexamples)
        fp = founddecoys / float(nexamples)
        distense = (fp-0)*(fp-0)+(tp-1)*(tp-1)#fpr横坐标，tpr纵坐标，求点(fp, tp)到最大阈值（0,1）的距离
        if(distense < min_dist):
            min_dist = distense
            flag_threshhold = min_dist
        tpr.append(tp)
        fpr.append(fp)
    best_threshhold = flag_threshhold
    return tpr, fpr, best_threshhold

def SetupROCCurvePlot(plt):
    plt.xlabel("FPR", fontsize=14)
    plt.ylabel("TPR", fontsize=14)
    plt.title("ROC Curve", fontsize=14)

def SaveROCCurvePlot(plt, best_treshhold, fname, randomline=True):
    if randomline:
        x = [0.0, 1.0]
        plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.legend(fontsize=10, loc='best_treshhold:%f' % best_treshhold)
    plt.tight_layout()
    plt.savefig(fname)


def AddROCCurve(plt, predict, truth, color, label):
    tpr, fpr, best_treshhold = GetRates(predict, truth)
    plt.plot(fpr, tpr, color=color, linewidth=2, label=label)
    return best_treshhold

def DepictROCCurve(predict, truth, label, color, fname, randomline=True):
    plt.figure(figsize=(4, 4), dpi=80)
    SetupROCCurvePlot(plt)
    best_treshhold = AddROCCurve(plt, predict, truth, color, label)
    SaveROCCurvePlot(plt, best_treshhold, fname, randomline)

def IsSupportedImageType(ext):
    fig = plt.figure()
    return (ext[1:] in fig.canvas.get_supported_filetypes())

def process():
    afname = 'C:\\Users\\zhang\\Documents\\GitHub\\imcl-caffe\\python\\utils\\actives.txt'
    sfname = 'C:\\Users\\zhang\\Documents\\GitHub\\imcl-caffe\\python\\utils\\scores.txt'
    ofname = 'C:\\Users\\zhang\\Documents\\GitHub\\imcl-caffe\\python\\utils\\roc.jpg'
    # read id of actives
    predict = {}
    print("Loaded %d actives from %s" % (len(predict), afname))
    # read molecule id - score pairs
    label, scores = LoadScores(sfname)
    print("Loaded %d %s scores from %s" % (len(scores), label, sfname))
    # sort scores by ascending order
    truth = {}
    ALL_IMG = []
    print("Plotting ROC Curve ...")
    color = "#008000"  # dark green
    DepictROCCurve(predict, truth, ALL_IMG, label, color, ofname)

if __name__ == "__main__":
    process()