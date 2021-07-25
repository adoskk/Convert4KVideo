import glob
import os
import tqdm
from argparse import ArgumentParser
import cv2
import numpy as np

parser = ArgumentParser()
parser.add_argument('--input_imgdir', type=str,
                    help='Path to input image directory.')
parser.add_argument('--output_imgdir', type=str,
                    help='Path to output image directory.')


def output(img, kernel_sharpen, path, output_folder):
    #applying the kernel to the input image
    output = cv2.filter2D(img, -1, kernel_sharpen)
    filename = os.path.splitext(path)[0]
    filename = os.path.split(filename)[-1]

    cv2.imwrite(os.path.join(output_folder,
                'sharpened_' + filename + '.jpg'), output)


def sharpen(path, output_folder):
    #reading the image passed thorugh the command line
    try:
        img = cv2.imread(path)

        #generating the kernels
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

        #process and output the image
        output(img, kernel, path, output_folder)
    except BaseException:
        pass
    return


def main():
    args = parser.parse_args()
    input_folder = args.input_imgdir
    output_folder = args.output_imgdir

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    else:
        for file in glob.glob(output_folder + '*.jpg'):
            os.remove(file)

    for file in tqdm.tqdm(glob.glob(os.path.join(input_folder,'*.jpg'))):
        sharpen(file, output_folder)
    print('Frames sharpened successfully!')


if __name__ == '__main__':
    main()
