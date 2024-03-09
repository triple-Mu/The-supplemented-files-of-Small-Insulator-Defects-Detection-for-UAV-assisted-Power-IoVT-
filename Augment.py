from PIL import Image

def apply_mosaic(image, block_size=10):

    width, height = image.size


    mosaic_image = Image.new('RGB', (width, height))


    for y in range(0, height, block_size):
        for x in range(0, width, block_size):

            box = (x, y, x + block_size, y + block_size)

            block = image.crop(box)

            average_color = tuple(map(lambda x: int(sum(x) / len(x)), zip(*block.getdata())))

            Image.Image.paste(mosaic_image, Image.new('RGB', block.size, average_color), box)

    return mosaic_image

def image_enhance(image_path):

    img = Image.open(image_path)


    img_rotated = img.rotate(90, expand=True)


    img_flipped_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)


    img_flipped_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)


    width, height = img.size
    x0 = width / 4
    y0 = height / 4
    x1 = 3 * width / 4
    y1 = 3 * height / 4
    img_cropped = img.crop((x0, y0, x1, y1))


    img_mosaic = apply_mosaic(img)


    img.show(title="Original Image")
    img_rotated.show(title="Rotated 90° Image")
    img_flipped_horizontal.show(title="Horizontally Flipped Image")
    img_flipped_vertical.show(title="Vertically Flipped Image")
    img_cropped.show(title="Cropped Image")
    img_mosaic.show(title="Mosaic Image")


image_path = 'path_to_your_image.jpg'
image_enhance(image_path)
