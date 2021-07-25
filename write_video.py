import glob
import cv2
import tqdm
from argparse import ArgumentParser
import os


parser = ArgumentParser()
parser.add_argument('--input_imgdir', type=str,
                    help='Path to input image directory.')
parser.add_argument('--output_video', type=str,
                    help='Path to output video.')


def main():
    args = parser.parse_args()
    input_folder = args.input_video
    output_video = args.output_imgdir

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video, fourcc, 24, (5120, 2880))

    for filename in tqdm.tqdm(glob.glob(os.path.join(input_folder, '*.jpg'))):
        frame = cv2.imread(filename)
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()


if __name__ == '__main__':
    main()
