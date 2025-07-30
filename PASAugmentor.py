import numpy as np
import cv2
import pandas as pd
from tiatoolbox.tools import stainnorm
import random
from albumentations.core.transforms_interface import ImageOnlyTransform
from Utils.RandStainNA.randstainna import RandStainNA
from histomicstk.saliency.tissue_detection import threshold_multichannel
from histomicstk.preprocessing.color_conversion import rgb_to_hsi

class PASAugmentor(ImageOnlyTransform):
    def __init__(self, 
                 p: float = 1.0, 
                 stain_augmentor: str = "PASAugmentor", 
                 mode: str = "Random", 
                 reference_matrix: float = None,
                 randstainna_std_hyper: float = None,
                 randstainna_distribution: str = "uniform",
                 background_removal: bool = True, 
                 always_apply: bool = False):
        super().__init__(always_apply=always_apply, p=p)
        assert stain_augmentor in ["PASAugmentor", "RandStainNA"], "Invalid stain augmentor specified."
        assert mode in ["Random", "Sequential"], "Invalid mode specified."
        if mode != "Random":
            assert reference_matrix is not None and reference_matrix in range(0,100), "Reference matrix must be provided for Sequential mode in a range between (0, 99)."
        assert randstainna_distribution in ["normal","laplacian","uniform"], "Unsupported distribution style specified for RandStainNA."

        self.template_path = './Utils/AugmentationTemplates/MatrixBased.tsv'
        self.template = pd.read_csv(self.template_path, sep='\t')
        self.rand_stainna_template_path = './Utils/AugmentationTemplates/RandStainNA.yaml'
        self.stain_augmentor = stain_augmentor
        self.mode = mode
        self.reference_matrix = reference_matrix
        self.background_removal = background_removal
        self.randstainna_std_hyper = randstainna_std_hyper
        self.randstainna_distribution = randstainna_distribution

    def apply(self, img, **params):
        if self.background_removal:
            background, _ = threshold_multichannel(rgb_to_hsi(img), {
                'hue': {'min': 0, 'max': 1.0},
                'saturation': {'min': 0, 'max': 0.2},
                'intensity': {'min': 220, 'max': 255},
            }, just_threshold=True)
        else:
            background = np.zeros(img.shape[:2], dtype=np.uint8)
        
        if self.stain_augmentor == "RandStainNA":
            if self.randstainna_std_hyper is not None:
                stainAugmentor = RandStainNA(
                    yaml_file=self.rand_stainna_template_path,
                    std_hyper=self.randstainna_std_hyper,
                    probability=self.p,
                    distribution=self.randstainna_distribution,
                    is_train=True,
                )
            else:
                # Default std_hyper to their original values
                stainAugmentor = RandStainNA(
                    yaml_file=self.rand_stainna_template_path,
                    probability=self.p,
                    distribution=self.randstainna_distribution,
                    is_train=True,
                )
                
            augmented_img = stainAugmentor(img)
            augmented_img = cv2.cvtColor(augmented_img, cv2.COLOR_BGR2RGB)
        else:
            stainAugmentor = stainnorm.MacenkoNormalizer()
            if self.mode == "Random":
                idx = random.randint(0, len(self.template) - 1)
            else:
                idx = self.reference_matrix
            stain_matrix = np.array([
                [
                    np.random.normal(self.template.loc[idx,'mu11'],self.template.loc[idx,'std11']),
                    np.random.normal(self.template.loc[idx,'mu12'],self.template.loc[idx,'std12']),
                    np.random.normal(self.template.loc[idx,'mu13'],self.template.loc[idx,'std13'])
                ],
                [
                    np.random.normal(self.template.loc[idx,'mu21'],self.template.loc[idx,'std21']),
                    np.random.normal(self.template.loc[idx,'mu22'],self.template.loc[idx,'std22']),
                    np.random.normal(self.template.loc[idx,'mu23'],self.template.loc[idx,'std23'])
                ]
            ]).reshape((2,3))
            maxC_matrix = np.array([
                np.array([
                    np.random.normal(self.template.loc[idx,'muMaxC1'],self.template.loc[idx,'stdMaxC1']),
                    np.random.normal(self.template.loc[idx,'muMaxC2'],self.template.loc[idx,'stdMaxC2'])
                ])
            ],dtype='float')
            stainAugmentor.stain_matrix_target = stain_matrix
            stainAugmentor.maxC_target = maxC_matrix
            augmented_img = stainAugmentor.transform(img)
        
        # Preserve original background pixels in the augmented image
        augmented_img[background == 1] = img[background == 1]
        return augmented_img

    def get_transform_init_args_names(self):
        # This helps Albumentations with serialization (optional, but recommended)
        return ("stain_augmentor", "mode", "reference_matrix", "background_removal")

    def template_size(self):
        return len(self.template)
