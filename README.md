# PASAugmentor
GitHub repository for the augmentation described in "Clustering-based Stain Augmentation: Templates for Periodic Acid-Schiff Biopsy Images".

Paper Link:

# Background
The lack of proposed methods for the modeling of distribution and constraints of stain variation in a representative reference
dataset presents a particular challenge for image augmentation pipelines in the context of training well-generalizable pathology-specific deep learning models. This project gathered a large collection of Periodic-acid-Schiff stained image patches, spanning 14 different datasets and displaying extensive stain variation with the aim of producing easily shareable and reusable: (i) extensive RandStainNA's stain style templates; and (ii) stain-matrix related templates calculated using a bespoke method based on cluster-based sampling of stain vectors to be used during model training, aiding the generation of reliable and realistic PAS augmentations during deep learning model training.

| ![Figure 1: (a) Principal component analysis showing the stain distribuition present in the acquired dataset clustered into 100 different stain vectors groups and (b)  Illustration of the center patch for each cluster.](https://github.com/patologiivest/PASAugmentor/blob/main/Images/src/Fig2.png?raw=true) |
|:--:| 
| *Figure: (a) Principal component analysis showing the stain distribuition present in the acquired dataset clustered into 100 different stain vectors groups and (b)  Illustration of the center patch for each cluster.* |

| ![Figure 2: Example of the different stain augmentations achieved from a single source image.](https://github.com/patologiivest/PASAugmentor/blob/main/Images/src/AugmentedImages.png?raw=true) |
|:--:| 
| *Figure 2: Example of the different stain augmentations achieved from a single source image.*|


# Use in Data Augmentation Pipelines
For more details on the use of PASAugmentor refer to *[PASAugmentor.py](PASAugmentor.py)*, [Notebook pipeline example.ipynb](https://github.com/patologiivest/PASAugmentor/blob/52c960333215578575f57c2c9e9264a470cec8ff/Examples/Notebook%20pipeline%20example.ipynb)* and *[Notebook disk example.ipynb](https://github.com/patologiivest/PASAugmentor/blob/52c960333215578575f57c2c9e9264a470cec8ff/Examples/Notebook%20disk%20example.ipynb)*

```
transforms_list = [
        stain_augmenter_method = "PASAugmentor"
        PASAugmentor(stain_augmenter=stain_augmenter_method,mode='Random', p=1, background_removal=False)
    ]
    
transforms.Compose(transforms_list)
```

# License
Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
