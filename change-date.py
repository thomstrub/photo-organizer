
import os
import sys
import shutil
from exif import Image

root_dir = "/Users/thom.strub/Desktop/Photos/"

for f in os.listdir(root_dir):
    print(f)
    img = Image(root_dir + f)
    print(img.has_exif)
    print(img.get("datetime") + " <---- datetime")
    print(img.get("datetime_digitized") + " <---- datetime_digitized")
    print(img.get("datetime_original") + " <---- datetime_original")
    # print(sorted(img.list_all()))

