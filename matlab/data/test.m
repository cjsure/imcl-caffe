Files = dir(strcat('D:\\Project\\caffe-windows-master-zhangjunhui\\data\\Blur2000\\test\\','*.BMP'));
LengthFiles = length(Files);
for i=1:LengthFiles;
    echo Files(i).name;
end