#! /usr/bin/env python
"""
Script to copy an image for selfcal looping
"""
import argparse
from argparse import RawTextHelpFormatter
import sys
import shutil
import os


def main(image, counter):
    """
    Copy an image

    Parameters
    ----------
    image : str
        Name of image to copy
    counter : int
        Index of loop

    Returns
    -------
    result : dict
        Dict with image name from previous loop

    """
    counter = int(counter)

    image_copy = image.replace('image42', 'image42_iter{}'.format(counter))
    if os.path.exists(image_copy):
        shutil.rmtree(image_copy)
    shutil.copytree(image, image_copy)

    if counter > 0:
        image_prev = image.replace('image42', 'image42_iter{}'.format(counter-1))
    else:
        image_prev = image.replace('image42', 'image32')

    return {'previous_image': image_prev}


if __name__ == '__main__':
    descriptiontext = "Copy an image.\n"

    parser = argparse.ArgumentParser(description=descriptiontext, formatter_class=RawTextHelpFormatter)
    parser.add_argument('image', help='name of the image to copy')
    parser.add_argument('counter', help='loop index')
    args = parser.parse_args()

    main(args.image, args.counter)




