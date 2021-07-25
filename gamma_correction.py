import glob
import os
import tqdm
import numpy as np
import cv2
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--input_imgdir', type=str,
                    help='Path to input image directory.')
parser.add_argument('--output_imgdir', type=str,
                    help='Path to output image directory.')

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 \
                        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def main():
    args = parser.parse_args()
    input_folder = args.input_imgdir
    output_folder = args.output_imgdir

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    else:
        for file in glob.glob(output_folder + '*.jpg'):
            os.remove(file)

    for file in tqdm.tqdm(glob.glob(os.path.join(input_folder, '*.jpg'))):
        original = cv2.imread(file)
        adjusted = adjust_gamma(original, gamma=1.5)

        img_name = os.path.split(file)[-1]
        img_name = os.path.splitext(img_name)[0][9:]
        cv2.imwrite(os.path.join(output_folder, 'gammacorrect' + img_name + '.jpg'), adjusted)
    print('Gamma correction finished!')

if __name__ == '__main__':
    main()
