Forked from https://www.github.com/BVLC/caffe master branch in 2015/11/09 .

#imcl-caffe
1. 安装VS2013，安装[CUDA7.5](http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_windows.exe)
2. 安装好上述软件之后，下载本项目（打开项目时，如果出现问题，多由CUDA版本不对导致，解决办法可以步骤参照[博文](http://blog.csdn.net/happynear/article/details/45372231)
3. 将[essential.rar](http://pan.baidu.com/s/1bolVeRt)在项目根目录解压，即补全项目的依赖lib\dll\.h文件
4. 打开工程（.sln)，重新生成解决方案
5. 在bin\x[86,64]目录下，双击run\_predict.bat执行测试程序，双击run\_ut.bat执行测试用例
6. 生成的结果文件放置于bin/\_tempdata目录
7. 项目的一些杂项放置于[私有云](http://pan.baidu.com/s/1bowBRER) 密码: 7ct2
8. dev\_train分支训练函数中，解压测试集[test_train](ut/data/test_tain.zip)即可使用测试数据
9. 默认编译是CPU_ONLY的，如果需要使用GPU，删除[Caffe-vs2013 - Release.props](Caffe-vs2013 - Release.props)中的`CPU_ONLY;`字段

中文安装说明：http://blog.csdn.net/happynear/article/details/45372231

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

