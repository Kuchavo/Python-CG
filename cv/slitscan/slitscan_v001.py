# === SlitScan Effect ===
# Contributors: Igor Kuchavo
# Requires at least: Python 2.7
# Tested up to: Python 2.7
# Version: 1.0.0

# creation of arguments for cmd
import argparse

parser = argparse.ArgumentParser(description='SlitScan v001 by Igor Kuchavo')

# path to video (/vid in default value)
parser.add_argument(
    '-i', '--input',
    type=str,
    default='/vid',
    help='provide a path to video (default: /vid)'
)

# path to video (/vid in default value)
parser.add_argument(
    '-o', '--output',
    type=str,
    default='/img',
    help='provide a path to video (default: /img)'
)

# name of input file
parser.add_argument('fname', type=str, help='filename')
args = parser.parse_args()

# import of libs
from moviepy.editor import VideoFileClip, VideoClip
from PIL import Image
import numpy as np

clip = VideoFileClip(args.fname).resize(0.4)

# outputting parms of video for test
# print('%s is %i fps, for %f seconds df at %s' % (args.fname, clip.fps, clip.duration, clip.size))

img = np.zeros((clip.size[1], clip.size[0], 3), dtype='uint8')

# boundary
currentX = 0
slitwidth = 1
slitpoint = clip.size[0] // 2 + clip.size[0] // 3 + 84

frame_generator = clip.iter_frames(fps=clip.fps, dtype='uint8')

# make frame
def make_frame(t):
    global img, currentX
    next_frame = next(frame_generator)
    # shifting
    img = np.roll(img, -1, axis=1)
    img[:,slitpoint,:] = next_frame[:,slitpoint,:]
    next_frame[:,max(slitpoint - currentX, 0):slitpoint,:] = img[:,max(0, slitpoint - currentX):slitpoint,:]
    currentX += 1
    return next_frame

# writting in .gif file
output = VideoClip(make_frame=make_frame, duration=35)
output.write_gif('slitscan_OUT.gif', fps=12)
