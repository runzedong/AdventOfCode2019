WIDTH_PIXELS = 25
HEIGHT_PIXELS = 6

def yield_image_layer(input_file, image_width, image_height):
    f = open(input_file, 'r')
    image = f.read()
    pointer = 0
    offset = image_width * image_height
    while pointer < len(image): 
        yield image[pointer:pointer+offset]
        pointer += offset
    f.close()

def count_layer_pixels(layer):
    number_0 = 0
    number_1 = 0
    number_2 = 0
    others = 0
    for i in layer:
        if i == '0':
            number_0 += 1
        elif i == '1':
            number_1 += 1
        elif i == '2':
            number_2 += 1
        else:
            others += 1
    return (number_0, number_1, number_2, others)

def main():
    count_0 = None
    multiple_1_and_2 = None
    print('Start')
    for layer in yield_image_layer('input.txt', WIDTH_PIXELS, HEIGHT_PIXELS):
        # skip the last invalid layer in case
        if len(layer) < WIDTH_PIXELS * HEIGHT_PIXELS:
            continue
        number_0, number_1, number_2, others = count_layer_pixels(layer)
        if count_0 is None:
            count_0 = number_0
            multiple_1_and_2 = number_1 * number_2
        elif count_0 > number_0:
            count_0 = number_0
            multiple_1_and_2 = number_1 * number_2
        else:
            print('Skip')
    print('Done')
    print('Count 0 is {}'.format(count_0))
    print('Output is {}'.format(multiple_1_and_2))
main()