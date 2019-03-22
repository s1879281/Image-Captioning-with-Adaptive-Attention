This is a PyTorch implementation of Image Captioning.



The soft-attention model is based on the paper [Show, Attend and Tell: 
Neural Image Caption 
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044.pdf).

The adaptive-attention model is based on the paper [Knowing When to 
Look: Adaptive 
Attention via A Visual Sentinel for Image Captioning](https://arxiv.org/pdf/1612.01887.pdf).

We will use Andrej Karpathy's training, validation, and test splits. To download the zip file, you can use the following command:
```
wget http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip
```

You can feel free to choose MSCOCO, Flicker8k or Flicker30k datasets.

You can use the following command to download these datasets:
```
wget http://images.cocodataset.org/zips/train2014.zip
wget http://images.cocodataset.org/zips/val2014.zip
wget http://nlp.cs.illinois.edu/HockenmaierGroup/Framing_Image_Description/Flickr8k_Dataset.zip
wget http://shannon.cs.illinois.edu/DenotationGraph/data/flickr30k-images.tar
```

Thanks to [a-PyTorch-Tutorial-to-Image-Captioning](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning).
