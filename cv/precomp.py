from PIL import Image,ImageFilter
import glob
import os

# getting seq
ren_arr = sorted(glob.glob('wall/*WALL_and_TONNEL*.png'))
bg_arr = sorted(glob.glob('frames/*.png'))
mask_s_arr = sorted(glob.glob('alpha_stones/*ALPHA_STONES*.png'))
mask_w_arr = sorted(glob.glob('alpha_wall/*ALPHA_WALL*.png'))
shad_arr = sorted(glob.glob('shadow/*SHADOW*.png'))
sm_arr = sorted(glob.glob('smoke/*SMOKE*.png'))

# compositing
for i in range(len(bg_arr)):
    bg = Image.open(bg_arr[i])
    shadow = Image.open(shad_arr[i]).resize(bg.size)
    bg.paste(shadow, (0, 0), shadow)

    wall = Image.open(ren_arr[i])
    mask_stones = Image.open(mask_s_arr[i]).split()[-1].convert('L').resize(bg.size)
    mask_wall = Image.open(mask_w_arr[i]).split()[-1].convert('L').resize(bg.size).filter(ImageFilter.BoxBlur(12))

    im_a1 = Image.composite(wall, bg, mask_wall)
    im_a2 = Image.composite(wall, im_a1, mask_stones)

    smoke = Image.open(sm_arr[i]).resize(bg.size)
    im_a2.paste(smoke, (0, 0), smoke)

    im_a2.save('comp/wall_comp_' + str('{:04}'.format(i+1)) + '.png')
    print(str('{:04}'.format(i+1)) + ' is complete!')

comp_arr = sorted(glob.glob('comp/*.png'))

# convert comp to mp4
cmd = 'ffmpeg -r 25 -i comp/wall_comp_%04d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p wall_comp_v001.mp4'
os.system(cmd)

print('All is complete!')
