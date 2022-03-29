# TTVSR (CVPR2022, Oral)
This is the official PyTorch implementation of the paper [Learning Trajectory-Aware Transformer for Video Super-Resolution](Arxiv).

## Contents
- [Introduction](#introduction)
  - [Contribution](#contribution)
  - [Approach overview](#approach-overview)
  - [Main results](#main-results)
- [Requirements and dependencies](#requirements-and-dependencies)
- [Model](#model)
- [Dataset](#dataset)
- [Test](#quick-test)
- [Train](#train)
- [Citation](#citation)
- [Acknowledgment](#acknowledgment)
- [Contact](#contact)


## Introduction
<!-- We proposed an approach named TTSR for RefSR task. Compared to SISR, RefSR has an extra high-resolution reference image whose textures can be utilized to help super-resolve low-resolution input. -->
<img src="https://github.com/ChengxuLiu/TTVSR/blob/main/fig/teaser_TTVSR.png" width=100%>

### Contribution
<!-- 1. We are one of the first to introduce the transformer architecture into image generation tasks. More specifically, we propose a texture transformer with four closely-related modules for image SR which achieves significant improvements over SOTA approaches.
2. We propose a novel cross-scale feature integration module for image generation tasks which enables our approach to learn a more powerful feature representation by stacking multiple texture transformers. -->

### Approach overview
<img src="https://github.com/ChengxuLiu/TTVSR/blob/main/fig/framework_TTVSR.png" width=100%>

### Main results
<img src="https://github.com/ChengxuLiu/TTVSR/blob/main/fig/case_TTVSR.png" width=100%>

## Requirements and dependencies
* python 3.7 (recommend to use [Anaconda](https://www.anaconda.com/))
* pytorch == 1.9.0
* torchvision == 0.10.0
* mmcv-full == 1.3.9
* scikit-image == 1.7.3
* lmdb == 1.2.1
* yapf == 0.31.0
* tensorboard == 2.6.0

## Model
<!-- Pre-trained models can be downloaded from [onedrive](https://1drv.ms/u/s!Ajav6U_IU-1gmHZstHQxOTn9MLPh?e=e06Q7A), [baidu cloud](https://pan.baidu.com/s/1j9swBtz14WneuMYgTLkWtA)(0u6i), [google drive](https://drive.google.com/drive/folders/1CTm-r3hSbdYVCySuQ27GsrqXhhVOS-qh?usp=sharing).
* *TTSR-rec.pt*: trained with only reconstruction loss
* *TTSR.pt*: trained with all losses
 -->

## Dataset
1. Download [CUFED train set](https://drive.google.com/drive/folders/1hGHy36XcmSZ1LtARWmGL5OK1IUdWJi3I) and [CUFED test set](https://drive.google.com/file/d/1Fa1mopExA9YGG1RxrCZZn7QFTYXLx6ph/view)
2. Make dataset structure be:
- CUFED
    - train
        - input
        - ref
    - test
        - CUFED5

## Test
<!-- 1. Clone this github repo
```
git clone https://github.com/FuzhiYang/TTSR.git
cd TTSR
```
2. Download pre-trained models and modify "model_path" in test.sh
3. Run test
```
sh test.sh
```
4. The results are in "save_dir" (default: `./test/demo/output`)
 -->

<!-- ## Evaluation
1. Prepare CUFED dataset and modify "dataset_dir" in eval.sh
2. Download pre-trained models and modify "model_path" in eval.sh
3. Run evaluation
```
sh eval.sh
```
4. The results are in "save_dir" (default: `./eval/CUFED/TTSR`) -->

## Train
<!-- 1. Prepare CUFED dataset and modify "dataset_dir" in train.sh
2. Run training
```
sh train.sh
```
3. The training results are in "save_dir" (default: `./train/CUFED/TTSR`) -->

## Citation
```
@InProceedings{liu2022learning,
author = {Liu, Chengxu and Yang, Huan and Fu, Jianlong and Qian, Xueming},
title = {Learning Trajectory-Aware Transformer for Video Super-Resolution},
booktitle = {CVPR},
year = {2022},
month = {June}
}
```

## Acknowledgment
This code is built on [mmediting](https://github.com/open-mmlab/mmediting). We thank the authors of [BasicVSR](https://github.com/ckkelvinchan/BasicVSR-IconVSR) for sharing their code.

## Contact
If you meet any problems, please describe them in issues or contact:
* Chengxu Liu: <liuchx97@gmail.com>
