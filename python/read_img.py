import glob
import os
import skimage.io as skio

IMG_DIR = 'D:\\Project\\caffe-windows-master-zhangjunhui\\data\\leaf\\normal\\'
DST_FILE = 'D:\\Project\\caffe-windows-master-zhangjunhui\\data\\leaf\\norm.txt'
back_end = '*.bmp'

def read_img(image_dir):
    name_list = glob.glob(image_dir + os.sep + back_end)
    for i in range(len(name_list)):
        image = skio.imread(name_list[i])
        sp = name_list[i].split('.bmp')
        skio.imsave(sp[0] + '.jpg', image)
        print "processing " + str(i) + ": " + sp[0] + '.jpg'

def gen_filelist_txt(image_dir):
    tmp = []
    file_names = os.listdir(image_dir)
    if(len(file_names) > 0):
        for fn in file_names:
            fullfilename = os.path.join(image_dir, fn)
            tmp.append(fullfilename.split("\\")[len(fullfilename.split("\\"))-1]+"\t1\n")
            print fullfilename.split("\\")[len(fullfilename.split("\\"))-1]
        tmp[-1] = tmp[-1].split("\n")[0]
        for line in tmp:
            print line
    file(DST_FILE, 'w').writelines(tmp)

if __name__ == '__main__':
    # read_img(IMG_DIR)
    gen_filelist_txt(IMG_DIR)