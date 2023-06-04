import os

label_en = []
label_cn = []
with open("label.txt", "r") as file:
    labels = file.readlines()
for i in labels:
    label_en.append(i.rstrip())

with open("label_cn.txt", "r", encoding="UTF-8") as file:
    labels = file.readlines()
for i in labels:
    label_cn.append(i.rstrip())

cur_dir = os.getcwd()
basedir = os.path.join(cur_dir, "caltech-101/101_ObjectCategories")

i = 0
for label in os.listdir(basedir):
    os.rename(os.path.join(basedir, label), os.path.join(basedir, label_cn[i]))
    i += 1
