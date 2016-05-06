from google.protobuf import text_format
import conf_pb2
import os
import random

ONE_IN_ALL = 10

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

def get_random_files_from_proto(file_path):
    file_list, score_list = get_name_score_from_proto(file_path)
    sum = 0
    tmp_file_list = []
    tmp_score_list = []
    while(sum < len(file_list) / ONE_IN_ALL):
        flag = 0
        sum = sum + 1
        index = random.randint(0,len(file_list)-1)
        for file in tmp_file_list:
            if file == file_list[index]:
                flag = 1
                break
        if flag == 0:
            tmp_file_list.append(file_list[index])
            tmp_score_list.append(score_list[index])
    print "sum of test_files_num:"+str(len(tmp_file_list))
    return tmp_file_list, tmp_score_list

def convert_test2proto(file_path, dst_test_path):
    file_list, score_list = get_random_files_from_proto(file_path)
    tmp = []
    tmp.append("filelist {\n"+"  root: "+"\"C:/root_path/\"\n")
    for i in range(len(file_list)):
        tmp.append("  file {\n    name: \""+"blur/"+str(file_list[i]+"\"\n    gold_score: "+str(score_list[i])+"\n  }\n"))
    tmp.append("}")
    file(dst_test_path, "w").writelines(tmp)

def get_train_name_score_from_restfiles(total_files_path, subset_test_path):
    total_file_list, total_score_list = get_name_score_from_proto(total_files_path)
    subset_file_list, subset_score_list = get_name_score_from_proto(subset_test_path)
    tmp_file_list = []
    tmp_score_list = []
    sum = 0
    for index in range(len(total_file_list)):
        flag = 0
        sum = sum + 1
        for test_file in subset_file_list:
            if(test_file == total_file_list[index]):
                flag =1
                break
        if flag == 0:
            tmp_file_list.append(total_file_list[index])
            tmp_score_list.append(total_score_list[index])
    print "sum of train_files_num:" + str(len(tmp_file_list))
    return tmp_file_list, tmp_score_list

def convert_train2proto(total_files_path, subset_test_path, dst_train_path):
    file_list, score_list = get_train_name_score_from_restfiles(total_files_path, subset_test_path)
    tmp = []
    tmp.append("filelist {\n"+"  root: "+"\"C:/root_path/\"\n")
    for i in range(len(file_list)):
        tmp.append("  file {\n    name: \""+"blur/"+str(file_list[i]+"\"\n    gold_score: "+str(score_list[i])+"\n  }\n"))
    tmp.append("}")
    file(dst_train_path, "w").writelines(tmp)

if __name__ == '__main__':
    file_path = 'D:\Project\caffe-windows-master-zhangjunhui\data\Blur5000-\\blur.proto'
    dst_test_path = 'D:\Project\caffe-windows-master-zhangjunhui\data\Blur5000-\\test.proto'
    dst_train_path = 'D:\Project\caffe-windows-master-zhangjunhui\data\Blur5000-\\train.proto'
    convert_test2proto(file_path, dst_test_path)
    convert_train2proto(file_path, dst_test_path, dst_train_path)