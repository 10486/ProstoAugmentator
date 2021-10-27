import random


class Augmentator:
    def __init__(self, augmentations, seed=42):
        self.augmentations = augmentations
        random.seed(seed)

    def __call__(self, text:str)->str:
        for aug in self.augmentations:
            text = aug(text)
        return text
