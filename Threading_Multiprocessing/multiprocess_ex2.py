#This program shows a much more practical application of using Multiprocessing to save processing time.

import time
from PIL import Image, ImageFilter
import concurrent.futures

img_names = [
    #names of photos.
    'Night-Rainbow-Print.jpg',
    'Leaning-into-the-night-Print.jpg',
    'Rainbow-Ice-Print-846x564.jpg',
    '4.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)

#Multiprocessing is better when there are more CPU Bound tasks.
#Threading is better when there are more IO Bound tasks.

def image_filter(img_name):
    img = Image.open(img_name) #IO Bound
    img = img.filter(ImageFilter.GaussianBlur(15)) #CPU BOUND

    img.thumbnail(size)
    img.save('Processed-%s.jpg'%img_name) #IO Bound
    print('%s was processed...'%img_name)



if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(image_filter, img_names)

t2 = time.perf_counter()

print('Finished in %.2f second(s)'%(t2-t1))
