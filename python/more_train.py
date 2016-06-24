from google.protobuf import text_format
import conf_pb2
ALL = 4 #multi nums for all trian images

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

def more_train(file_path):
    file_list, score_list = get_name_score_from_proto(file_path)
    sum = 0
    tmp_file_list = []
    tmp_score_list = []
    tmp_all = ALL
    while(tmp_all):
        for i in range(len(file_list)):
            tmp_file_list.append(file_list[i])
            tmp_score_list.append(score_list[i])
        tmp_all = tmp_all - 1
    return tmp_file_list, tmp_score_list

def convert2proto(file_path, dst_test_path):
    file_list, score_list = more_train(file_path)
    tmp = []
    tmp.append("filelist {\n"+"  root: "+"\"C:/root_path/\"\n")
    for i in range(len(file_list)):
        tmp.append("  file {\n    name: \""+str(file_list[i]+"\"\n    gold_score: "+str(score_list[i])+"\n  }\n"))
    tmp.append("}")
    file(dst_test_path, "w").writelines(tmp)


if __name__ == '__main__':
    train_proto = 'D:\Project\caffe-windows-master-zhangjunhui\data\gray\\train.proto'
    dst_train_path = 'D:\Project\caffe-windows-master-zhangjunhui\data\gray\\train_'+str(ALL)+'.proto'
    convert2proto(train_proto, dst_train_path)