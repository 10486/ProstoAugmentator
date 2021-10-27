from src.augmentations.base_augmnentation import BaseAugmentation
import random


class ChangeCharsAugmentation(BaseAugmentation):
    """ Аугментация, которая меняет две соседние буквы в слове """
    def __init__(self,probability:float):
        super().__init__(probability)

    def __call__(self, text: str) -> str:
        if random.random() <= self.probability:
            letter = random.choice(text)
            letind = text.index(letter)
            if letind != 0:
                letter2 = text[letind - 1]
                newtext = text.replace(letter2 + letter, letter + letter2)
            else:
                letter2 = text[letind + 1]
                newtext = text.replace(letter + letter2, letter2 + letter)

            return newtext
        return text
