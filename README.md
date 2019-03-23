# Image-Captioning-with-Adaptive-Attention

This is a PyTorch implementation of [Knowing When to
Look: Adaptive
Attention via A Visual Sentinel for Image Captioning](https://arxiv.org/pdf/1612.01887.pdf).

![example](https://github.com/s1879281/Image-Captioning-with-Adaptive-Attention/blob/master/images/example.jpg)

## Requirements

This code is all written in Python. You will need a GPU to train the model.

You also need to install the following package in order to sucessfully run the code.

* Torch
* torchvision
* h5py
* scipy
* tqdm
* NLTK

## Dataset

You can feel free to choose [MSCOCO](http://cocodataset.org/#home), [Flicker8k](https://forms.illinois.edu/sec/1713398)
 or [Flicker30k](http://shannon.cs.illinois.edu/DenotationGraph) as your dataset.

You might want to use the following command to download the MSCOCO dataset:
```
wget http://images.cocodataset.org/zips/train2014.zip
wget http://images.cocodataset.org/zips/val2014.zip
```

We will use Andrej Karpathy's training, validation, and test splits. To download the zip file, you can use the following command:
```
wget http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip
```
## Data preprocess
In order to preprocess the data on the MSCOCO dataset, you can use the following command:
```
mkdir coco_folder
python create_input_files.py -d coco -i [YOUR-IMAGE-FLODER]
```

## Training
Use the following command to training the model:
```
python train.py -d coco
```

For comparison, you may also want to train the model with soft attention ([paper](http://proceedings.mlr.press/v37/xuc15.pdf)):
```
python train.py -d coco -a
```

## Evaluation
You can feel free to choose different beam sizes during evaluation. Use the following command to compute all BLEU (i.e. BLEU-1 to BLEU-4) scores:
```
python eval.py -d coco -cf [PATH-TO-CHECKPOINT] -b 5
```
Note that the best checkpoint is based on the BLEU-4 score.


## Captioning
For captioning on your own image, you can use the following command:
```
python caption.py
```

## Reference
If you use this code as part of any published research, please acknowledge the following paper:

```
@misc{Lu2017Adaptive,
author = {Lu, Jiasen and Xiong, Caiming and Parikh, Devi and Socher, Richard},
title = {Knowing When to Look: Adaptive Attention via A Visual Sentinel for Image Captioning},
journal = {CVPR},
year = {2017}
}
```

## Acknowledgement
The code is developed based on [a-PyTorch-Tutorial-to-Image-Captioning](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning).
