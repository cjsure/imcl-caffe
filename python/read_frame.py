import cv2
import time
import caffe
import os
import skimage.io as skio

FRAMES = 4

def read_video(file):
    if file is False:
        return
    video = cv2.VideoCapture(file)
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        size = (int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
                int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
        print "Frames size: {0}".format(size)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
        print "Frames size: {0}".format(size)

    # Number of frames to capture
    num_frames = FRAMES;
    print "Capturing {0} frames".format(num_frames)
    # Start time
    start = time.time()
    # Grab a few frames
    images = []
    for i in xrange(0, num_frames):
        ret, frame = video.read()
        images.append(frame)
        #skio.imsave(video_file.split('.')[0] + '_' + '{}.jpg'.format(i), frame)
        # cv2.imwrite(img_filename, frame)
    # End time
    end = time.time()
    for im in images:
        skio.imshow(im)
        skio.show()
    # Time elapsed
    seconds = end - start
    print "Time taken : {0} seconds".format(seconds)
    video.release()
    return images

def showIM():
    imgs = read_video('C:\\Users\\zhang\\Pictures\\test\\1.avi')
    for im in imgs:
        skio.imshow(im)
        skio.show()


if __name__ == '__main__':
    showIM()
    pass