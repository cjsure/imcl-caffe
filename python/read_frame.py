import cv2
import skimage.io as skio

video_file = 'C:/Users/zhang/Pictures/1.avi'

def read_video(file):
    cap = cv2.VideoCapture(file)

    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        img_filename = "./frames/" + str(i) + ".png"
        skio.imshow(frame)
        skio.show()
        #cv2.imwrite(img_filename, frame)
        i = i + 1
    cap.release()

if __name__ == '__main__':
    read_video(video_file)