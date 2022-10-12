import os

import pandas as pd

path = "/home/tinctura/git/hateful_memes/bot/bot_images"
files = os.listdir(path)

df = pd.DataFrame(files, columns=["uri"])
print(df)
df.to_csv("imgs.csv", index=False)

# from PIL import Image
# import os


# path = 'C:/BadreevDR/image processing/New folder/'
# files = os.listdir(path)


# img_hash_path_dict = {}
# for idx, image_path in enumerate(files):
#   image = Image.open(f'{path}{image_path}')
#   image = image.resize((12,11), Image.ANTIALIAS).convert('L')
#   pixel_data = list(image.getdata())
#   average_pixel = sum(pixel_data)/len(pixel_data)
#   bits = "".join(['1' if (px >= average_pixel) else '0' for px in pixel_data])
#   hex_representation = str(hex(int(bits, 2)))[2:][::-1].upper()
#   img_hash_path_dict.update({hex_representation : f'{path}{image_path}'})

# i=1
# for path in img_hash_path_dict.values():
#     image = Image.open(path)
#     image_name_path = "C:/BadreevDR/image processing/New folder (4)/" + str(i) + ".png"
#     i = i+1
#     image.save(image_name_path)
