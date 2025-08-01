# PASAugmentor

GitHub repository for the augmentation described in "Clustering-based Stain Augmentation: Templates for Periodic Acid-Schiff Biopsy Images".

Paper Link:

# Background

In computational pathology, stain augmentation is one of the key approaches to produce deep learning models that are more generalizable and invariant to the types of stain variation that often exists between laboratories. However, achieving realistic augmentations typically requires knowledge about the target domain characteristics, the modeling of which depends on access to large and varied reference datasets. Access to such data is often limited and dataset sharing is restricted due to privacy regulations, severely hampering the ability of research groups to establish diverse and representative augmentation baselines. To overcome this issue, the current project suggested to establish augmentation templates that are more easily shared between research groups. For this purpose, Periodic acid-Schiff stained images from over 14 different sources were collected and utilized to establish a stain style-related (RandStainNA) and a stain vector-related augmentation template.

# Material and methods

This GitHub repository contains these two augmentation templates as well as the code for producing new augmentations. Augmentations can either be achieved using the RandStainNA tool (using the stain style template). We are also introducing the PASAugmentor, a bespoke tool for creating augmentations from the stain vector-related augmentation templates. Both augmentation methods allow optional removal of background pixels prior to augmentation.

| ![Figure 1: Illustration of augmentations. An example glomerulus (top) is randomly augmented 100 times either with the RandStainNA (bottom left) or the PASAugmentor (bottom right). Both augmentations employ background removal to focus color shifts only to foreground pixels. The RandStainNA is run using the uniform distribution setting.](https://github.com/patologiivest/PASAugmentor/blob/main/Images/src/Fig.png?raw=true) |
|:--:| 
| *Figure 1: Illustration of augmentations. An example glomerulus (top) is randomly augmented 100 times either with the RandStainNA (bottom left) or the PASAugmentor (bottom right). Both augmentations employ background removal to focus color shifts only to foreground pixels. The RandStainNA is run using the uniform distribution setting.* |

# Use in Data Augmentation Pipelines

For more details on the use of PASAugmentor refer to [*PASAugmentor.py*](PASAugmentor.py), [Notebook pipeline example.ipynb](https://github.com/patologiivest/PASAugmentor/blob/52c960333215578575f57c2c9e9264a470cec8ff/Examples/Notebook%20pipeline%20example.ipynb) and [*Notebook disk example.ipynb*](https://github.com/patologiivest/PASAugmentor/blob/52c960333215578575f57c2c9e9264a470cec8ff/Examples/Notebook%20disk%20example.ipynb)

```         
transforms_list = [
        stain_augmenter_method = "PASAugmentor"
        PASAugmentor(stain_augmenter=stain_augmenter_method,mode='Random', p=1, background_removal=False)
    ]
    
transforms.Compose(transforms_list)
```

# License

Shield: [![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)
