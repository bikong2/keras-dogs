# @author: lixihua9@126.com
# @date:   20170925
# @brief:  each class of samples put into one folder

import os
from shutil import copy

label_cnt = 0
img_folder_train = '/home/lixihua/datas/dogs_recognition/ori_data/train'
img_folder_valid = '/home/lixihua/datas/dogs_recognition/ori_data/valid'
train_folder = '/home/lixihua/datas/dogs_recognition/keras_train'
valid_folder = '/home/lixihua/datas/dogs_recognition/keras_valid'

train_img_txt = "/home/lixihua/datas/dogs_recognition/ori_data/data_train_image.txt"
valid_img_txt = "/home/lixihua/datas/dogs_recognition/ori_data/data_valid_image.txt"

train_dict = {}
train_dog = []
train_imgs = open(train_img_txt, "r")
for line in train_imgs:
    line = line.strip().split(" ")
    img_name = line[0]
    dog_name = line[1]
    train_dict[img_name] = dog_name
    if dog_name not in train_dog:
        train_dog.append(dog_name)
train_imgs.close()
print train_dog

valid_dict = {}
valid_dog = []
valid_imgs = open(valid_img_txt, "r")
for line in valid_imgs:
    line = line.strip().split(" ")
    img_name = line[0]
    dog_name = line[1]
    valid_dict[img_name] = dog_name
    if dog_name not in valid_dog:
        valid_dog.append(dog_name)
valid_imgs.close()
print valid_dog

"""
# for train
for i, file_name in enumerate(os.listdir(img_folder_train)):
    file_path = os.path.join(img_folder_train, file_name)
    if os.path.isfile(file_path):
        cur_label = file_name.split(".j")[0]
        if cur_label not in train_dict:
            continue
        cur_dog = train_dict[cur_label]
        if not os.path.exists(os.path.join(train_folder, cur_dog)):
            os.makedirs(os.path.join(train_folder, cur_dog))
        print os.path.join(os.path.join(train_folder, cur_dog), file_name)
        copy(file_path, os.path.join(os.path.join(train_folder, cur_dog), file_name))
"""

# for valid
for i, file_name in enumerate(os.listdir(img_folder_valid)):
    file_path = os.path.join(img_folder_valid, file_name)
    if os.path.isfile(file_path):
        cur_label = file_name.split(".j")[0]
        if cur_label not in valid_dict:
            continue
        cur_dog = valid_dict[cur_label]
        if not os.path.exists(os.path.join(valid_folder, cur_dog)):
            os.makedirs(os.path.join(valid_folder, cur_dog))
        print os.path.join(os.path.join(valid_folder, cur_dog), file_name)
        copy(file_path, os.path.join(os.path.join(valid_folder, cur_dog), file_name))
