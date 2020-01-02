WIDTH_PIXELS = 25
HEIGHT_PIXELS = 6
BLACK = '0'
WHITE = '1'
TRANSPARENT = '2'

def yield_image_layer(input_file, image_width, image_height):
    f = open(input_file, 'r')
    image = f.read()
    pointer = 0
    offset = image_width * image_height
    while pointer < len(image): 
        yield image[pointer:pointer+offset]
        pointer += offset
    f.close()

def render_layer(image, layer):
    for i in range(len(image)):
        if image[i] == TRANSPARENT:
            image[i] = layer[i]

def main():
    image = [TRANSPARENT] * (WIDTH_PIXELS * HEIGHT_PIXELS)
    print('Start')
    for layer in yield_image_layer('input.txt', WIDTH_PIXELS, HEIGHT_PIXELS):
        # skip the last invalid layer in case
        if len(layer) < WIDTH_PIXELS * HEIGHT_PIXELS:
            continue
        render_layer(image, layer)
    print('Done')
    start = 0
    while start < len(image):
        print(''.join(image[start : start + WIDTH_PIXELS]))
        start += WIDTH_PIXELS
main()