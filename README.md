#Image-Captioning-with-Adaptive-Attention

This is a PyTorch implementation of [Knowing When to
Look: Adaptive
Attention via A Visual Sentinel for Image Captioning](https://arxiv.org/pdf/1612.01887.pdf).

![example](https://github.com/s1879281/Image-Captioning-with-Adaptive-Attention/blob/master/images/example.jpg)

##Dataset

We will use Andrej Karpathy's training, validation, and test splits. To download the zip file, you can use the following command:
```
wget http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip
```

You can feel free to choose [MSCOCO](http://cocodataset.org/#home), [Flicker8k](https://forms.illinois.edu/sec/1713398)
 or [Flicker30k](http://shannon.cs.illinois.edu/DenotationGraph) as your dataset.

You might want to use the following command to download the MSCOCO dataset:
```
wget http://images.cocodataset.org/zips/train2014.zip
wget http://images.cocodataset.org/zips/val2014.zip
```
##Reference
If you use this code as part of any published research, please acknowledge the following paper:

```
@misc{Lu2017Adaptive,
author = {Lu, Jiasen and Xiong, Caiming and Parikh, Devi and Socher, Richard},
title = {Knowing When to Look: Adaptive Attention via A Visual Sentinel for Image Captioning},
journal = {CVPR},
year = {2017}
}
```

##Acknowledgement
The code is developed based on [a-PyTorch-Tutorial-to-Image-Captioning](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning).
