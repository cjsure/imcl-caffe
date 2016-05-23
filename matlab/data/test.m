Files = dir(strcat('D:\\Project\\caffe-windows-master-zhangjunhui\\data\\pure\\blur\\','*.bmp'));
LengthFiles = length(Files);
for i = 1:LengthFiles;
    img_file=imread(Files(i).name);
    img_name = Files(i).name;
    file_name =stract('',[img_name(1,end-4)]);
    imwrite(img_file,String(file_name),'jpg');
end