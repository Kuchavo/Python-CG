# videos.py
import argparse

parser = argparse.ArgumentParser(description='Slit Scan v001 by Igor Kuchavo')
#parser.add_argument('indir', type=str, help=image'Input dir for videos')
#parser.add_argument('outdir', type=str, help='Output dir for image')
parser.add_argument(
    '-i', '--input',
    type=str,
    default='/vid',
    help='provide a path to video (default: /vid)'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    default='/img',
    help='provide a path to video (default: /img)'
)
parser.add_argument('fname', type=str, help='filename')
args = parser.parse_args()

# print(args.fname)

from moviepy.editor import VideoFileClip, VideoClip
from PIL import Image
import numpy as np

clip = VideoFileClip(args.fname).resize(0.4)

# print('%s is %i fps, for %f seconds df at %s' % (args.fname, clip.fps, clip.duration, clip.size))

img = np.zeros((clip.size[1], clip.size[0], 3), dtype='uint8')

#process
currentX = 0
slitwidth = 1
slitpoint = clip.size[0] // 2 + clip.size[0] // 3 + 84
# slitpoint = clip.size[0] // 2 + clip.size[0] // 2
frame_generator = clip.iter_frames(fps=clip.fps, dtype='uint8')

def make_frame(t):
    global img, currentX
    next_frame = next(frame_generator)
    #shifting
    img = np.roll(img, -1, axis=1)
    img[:,slitpoint,:] = next_frame[:,slitpoint,:]
    next_frame[:,max(slitpoint - currentX, 0):slitpoint,:] = img[:,max(0, slitpoint - currentX):slitpoint,:]
    currentX += 1
    return next_frame

output = VideoClip(make_frame=make_frame, duration=35)
output.write_gif('output1.gif', fps=12)
#
#
#
#
# # from PIL import Image
# # import glob, os
# #
# # for invideo in glob.glob("vid\*"):
# #     os.system('ffmpeg.exe -i ' + invideo +' -filter:v "crop=2:1080:960:1" -q:v 1 temp/images-%04d.jpeg')
# #
# # print("frames extracted")
# #
# # im_sequence = glob.glob("img\*.jpeg")
# # im_size = (len(im_sequence), 1080)
# # composite = Image.new("RGB", im_size)
# # pix_col = 0
# #
# # for infile in im_sequence:
# #     file, ext = os.path.splitext(infile)
# #     im = Image.open(infile)
# #     im_center = 1920 / 2
# #     im_strip = im.crop( (0, 0, 1, 1080) )
# #     composite.paste(im_strip, (pix_col, 0))
# #     pix_col += 1
# #     im.close()
# #     os.remove(infile)
# #     print(file)
# #
# # composite.save("unwrapped.jpeg", "JPEG")
# #
# #
# # print("done")
