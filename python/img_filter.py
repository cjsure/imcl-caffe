from google.protobuf import text_format
import conf_pb2
import shutil

IMG_ROOT = "D:/Project/caffe-windows-master-zhangjunhui/data/gblur/"
FILE_PATH = "D:/Project/caffe-windows-master-zhangjunhui/data/gblur/mos.proto"
DST_PATH = "D:/Project/caffe-windows-master-zhangjunhui/data/gblur/selected/"

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

def file_filter(file_path):
    name, score = get_name_score_from_proto(file_path)
    selected_name = []
    tmp = []
    for i in range(len(name)):
        if(score[i] != 1):
            selected_name.append((name[i]))
            tmp.append(str(name[i]) +' ' + str(score[i]) + '\n')
    file(DST_PATH + 'selected.txt', 'w').writelines(tmp)
    return selected_name

def copy_file(file_path):
    name = file_filter(file_path)
    sum = 0
    for file in name:
        shutil.copy(IMG_ROOT+file,DST_PATH+file)
        sum = sum + 1
    print sum

if __name__ == '__main__':
    copy_file(FILE_PATH)