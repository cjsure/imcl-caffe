from google.protobuf import text_format
import conf_pb2
import shutil
import os

file_path = 'D:\Project\caffe-windows-master-zhangjunhui\data\Blur5000\\pure.proto'
dir_path = 'D:\Project\caffe-windows-master-zhangjunhui\data\Blur5000\\'
dst_path = "D:\Project\caffe-windows-master-zhangjunhui\data\Blur5000\\pure\\"
phase = 'pure'

def read_proto_file(file_path, parser_object):
    file = open(file_path, "r")
    text_format.Merge(str(file.read()), parser_object)
    file.close()
    return parser_object


def get_name_from_proto(file_path):
    app_config = conf_pb2.AppConfig()
    read_proto_file(file_path, app_config)
    name = []
    for f in app_config.filelist.file:
        name.append(f.name)
    return name

def copy_files(file_path):
    sum = 0
    file_list = get_name_from_proto(file_path)
    if not os.path.isdir(dst_path + 'blur/'):
        os.mkdir(dst_path)
    for file in file_list:
        tmp_file = dir_path + file
        shutil.copy(tmp_file, dst_path + file)
        print dst_path + file
        sum += 1
    shutil.copy(file_path,dst_path + phase + '.proto')
    print sum

if __name__ == '__main__':
    copy_files(file_path)