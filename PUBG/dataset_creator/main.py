import os
import cv2


def simply_frame(img):
    out_length = 128
    out_height = 72
    img = cv2.resize(img, (out_length,out_height))
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # TODO add centercrop
    return img

def video2img(video_path, image_save_path, info_txt_path, cpu_index):
    cap = cv2.VideoCapture(video_path)
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if num_frames == 0:
        print("err frame=0", video_path)
        exit()
    with open(info_txt_path,'w') as f:
        for i in range(num_frames):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            time_stamp = str(cap.get(cv2.CAP_PROP_POS_MSEC))
            img_name = str((i + 1) * (cpu_index + 1)) + '.png'
            img_path = os.path.join(image_save_path, img_name)
            _, frame = cap.read()
            print(frame.shape)
            frame = simply_frame(frame)
            cv2.imwrite(img_path, frame)
            print(frame.shape)
            f.write(img_name + ' ' + '\n')
    cap.release()


def gen_dirs(new_path):
    if not os.path.exists(new_path):
        os.mkdir(new_path)
        print('create new folder')
    else:
        print('imgs path already exits')


if __name__ == '__main__':
    video_path = 'xxx/test.mov'
    info_txt_path = './i.txt'
    image_save_path = './imgs'
    gen_dirs(image_save_path)
    video2img(video_path,image_save_path,info_txt_path,0)
    exit()
