# -*- coding: utf-8 -*-
"""tracking, bluring, counting using yolov8 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1adag5C2BBTvbmt4EbCuzkgNi1BVboNoi
"""

!git clone https://github.com/MuhammadMoinFaisal/YOLOv8-object-tracking-blurring-counting.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/YOLOv8-object-tracking-blurring-counting

!pip install -e '.[dev]'

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/YOLOv8-object-tracking-blurring-counting/ultralytics/yolo/v8/detect

!gdown "https://drive.google.com/uc?id=11ZSZcG-bcbueXZC3rN08CM0qqX3eiHxf&confirm=t"

!unzip 'deep_sort_pytorch.zip'

!gdown https://drive.google.com/uc?id=1_kt1alzcLRVxet-Drx0mt_KFSd3vrtHU

!python predict.py source="test1.mp4"

!rm "/content/result_compressed.mp4"

