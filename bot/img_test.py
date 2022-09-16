import os
import random
from io import BytesIO

import cv2
import numpy as np
import requests
import telebot
from PIL import Image

# from default_config import config
# from utils import Db_connection

# bot = telebot.TeleBot(config["BOT_TOKEN"])
# conn = Db_connection()


# path = "image/7b1d8be1-2dd4-11ed-bf9e-5f788833145f.jpg"

# img = Image.open(path)

# print(img)

# '({0})'.format(i) for i in paths


path = "test_img"
files = os.listdir(path)
print(files)

for image in files:
    # Read image
    img = cv2.imread(f"test_img/{image}")

    # The number of pixels
    num_rows, num_cols = img.shape[:2]

    # Creating a translation matrix
    translation_matrix = np.float32([[1, 0, 5], [0, 1, 5]])

    # Image translation
    img_translation = cv2.warpAffine(
        img, translation_matrix, (num_cols + 1, num_rows + 1)
    )

    fout = f"test_img/1px_{image}"
    cv2.imwrite(fout, img_translation)


img_hash_path_dict = {}

for idx, image_path in enumerate(files):
    if image_path.endswith("jpg"):
        image = Image.open(f"{path}/{image_path}")
        image = image.resize((12, 11), Image.ANTIALIAS).convert("L")
        pixel_data = list(image.getdata())
        average_pixel = sum(pixel_data) / len(pixel_data)
        bits = "".join(["1" if (px >= average_pixel) else "0" for px in pixel_data])
        hex_representation = str(hex(int(bits, 2)))[2:][::-1].upper()
        img_hash_path_dict.update({hex_representation: f"{path}/{image_path}"})
        print(idx)
    else:
        continue

i = 1
for path in img_hash_path_dict.values():
    image = Image.open(path)
    image_name_path = "selected/" + "new_imgs" + str(i) + ".jpg"
    i = i + 1
    image.save(image_name_path)
