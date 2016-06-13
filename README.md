#caffe环境搭建
1.安装CUDA7.5

2.把3rdparty解压到根目录

3.打开工程文件buildVS2013/MainBuilder.sln,重新生成所有工程

中文博客:http://blog.csdn.net/happynear/article/details/45372231

#python环境搭建
1.安装Anaconda

2.安装pycharm

#imcl-caffe使用说明
##生成数据
根目录下python文件夹里面包含了实验所用到的数据生成等脚本

主要文件使用如下:

gen_test_train.py:将总数据划分为训练集和测试集

label_file_util.py:读取caffe格式或者文本格式图像标签文本文件

genh5_data.py:生成实验数据.h5文件

predict3.py:实验测试
##开始训练
根目录下

run_surtest.bat:用实验室Alex_net网络训练,需要在自己环境下修改相应目录路径

snapshot.bat:在上一次断点处继续训练

weights.bat:调整训练权重再训练

