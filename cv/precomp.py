from PIL import Image,ImageEnhance

# open imgs
render = Image.open('render.png')
bg = Image.open('bg.png').resize(render.size)
mask = Image.open('alpha.png').split()[-1].convert('L').resize(render.size)
shadow = Image.open('shadow.png').resize(render.size)

# add shadow
bg.paste(shadow, (0, 0), shadow)

# shadow contrast
img_contrast = ImageEnhance.Contrast(shadow)
factor = 15
shadow_c = img_contrast.enhance(factor)

# compile
im = Image.composite(render, bg, mask)

im.show()
