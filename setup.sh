#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd yolov5
mkdir dataset
cd dataset
mkdir bdd100k
cd bdd100k
mkdir labels
cd labels
mkdir 100k
cd 100k
mkdir train
mkdir val
cd ../../../../../
python3 download_files.py
mv bdd100k_labels_images_train.json yolov5/dataset/bdd100k/
mv bdd100k_labels_images_val.json yolov5/dataset/bdd100k/
wget https://dl.cv.ethz.ch/bdd100k/data/100k_images_train.zip
wget  https://dl.cv.ethz.ch/bdd100k/data/100k_images_val.zip
unzip 100k_images_train.zip -d yolov5/dataset/
unzip 100k_images_val.zip -d yolov5/dataset/
rm 100k_images_train.zip
rm 100k_images_val.zip
cd yolov5
python preprocess.py