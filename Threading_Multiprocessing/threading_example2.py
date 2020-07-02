import requests
import time
import concurrent.futures as cf

img_urls = [
    #Image URLS get from Unsplash or any other free website.
]

t1 = time.perf_counter()
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = '%s.jpg'%img_name
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print('%s was downloaded'%img_name)


with cf.ThreadPoolExecutor() as executor:
    executor.mao(download_image, img_urls)

#This will download images much much faster (almost 5 times faster than usual for loop methods)
#since all images will be downloaded concurrently as opposed to one by one or asynchronously as opposed to synchronously


