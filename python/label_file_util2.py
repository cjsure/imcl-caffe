from numpy import *

file_path = "D:/Project/caffe-windows-master-zhangjunhui/data/blur5000/others/pure.txt"
dst_path = "D:/Project/caffe-windows-master-zhangjunhui/data/blur5000/others/pure.proto"

def score_bound(score, max_score, min_score):
    tmp_score = (score - min_score)/(max_score - min_score)
    return 1 - tmp_score

def max_min(file_path):
    with open(file_path, 'r') as T:
        lines = T.readlines()
    score = []
    max = -inf
    min = inf
    for line in lines:
        sp = line.split(' ')
        if max < float(sp[1]):
            max = float(sp[1]);
        if min > float(sp[1]):
            min = float(sp[1]);
    print 'max:' + str(max) + 'min:' + str(min)
    return max, min

def load_new_format_labelscore(file_path):
    with open(file_path, 'r') as T:
        lines = T.readlines()
    img_name = []
    score = []
    #max, min = max_min(file_path)
    for line in lines:
        sp = line.split(' ')
        img_name.append(str(sp[0]))
        #score.append(score_bound(float(sp[1]), max, min))
        score.append(float(1))
    return img_name, score

def convet2standard(file_path, dst_path):
    file_list, score_list = load_new_format_labelscore(file_path)
    tmp = []
    tmp.append("filelist {\n"+"  root: "+"\"C:/root_path/\"\n")
    for i in range(len(file_list)):
        tmp.append("  file {\n    name: \""+str(file_list[i])+"\"\n    gold_score: "+str(score_list[i])+"\n  }\n")
        #tmp.append("  file {\n    name: \""+"blur/"+str(file_list[i]+"\"\n    gold_score: "+str(score_list[i])+"\n  }\n"))
    tmp.append("}")
    file(dst_path, "w").writelines(tmp)

def avi2png(file_path):
    avi_name_list, score_list = load_new_format_labelscore(file_path)
    tmp_name = []
    for i in range(len(avi_name_list)):
        tmp_name.append(avi_name_list[i].split(".")[-2]+'.bmp\t' + str(score_list[i]) + '\n')
        print tmp_name[i]
    file(dst_path, "w").writelines(tmp_name)


if __name__ == '__main__':
    #avi2png(file_path)
   convet2standard(file_path, dst_path)