import os 
import glob
import cv2
import tqdm
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--input_video', type=str,
                    help='Path to video.')
parser.add_argument('--output_imgdir', type=str,
                    help='Path to output image directory.')

    
def main():
    args = parser.parse_args()
    input_video = args.input_video
    output_folder = args.output_imgdir

    # prepare folder for output images
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    else:
        for file in tqdm.tqdm(glob.glob(os.path.join(output_folder, '*.jpg'))):
            os.remove(file)

    vidcap = cv2.VideoCapture(input_video)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(os.path.join(output_folder, 'frame%d.jpg' % count), image)     # save frame as JPEG file
        success, image = vidcap.read()
        count += 1
    print("Frames extracted successfully! Total video frames: ", count)
    return

if __name__ == '__main__':
    main()
