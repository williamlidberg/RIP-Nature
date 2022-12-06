import os
from urllib.parse import urlparse
import pandas as pd
import wget
from multiprocessing.dummy import Pool 

# save downloaded files here: 
dest_dir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/laz/' 

def download_files(urls):
    wget.download(urls, dest_dir)


df = pd.read_csv('Y:/William/RIP_NATURE_2/Canada/url_list.csv', header=None)
df = df[0].tolist()


Pool(60).map(download_files, df)
