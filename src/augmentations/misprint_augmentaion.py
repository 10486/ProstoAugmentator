from src.augmentations.base_augmnentation import BaseAugmentation
import json
import random
import os
from pathlib import Path


class MisprintAugmentation(BaseAugmentation):
    """ Аугментация, которая заменяет букву в слове на одну из букв в ближайщем окружении на клавиатуре """

    def __init__(self,probability:float=0.5):
        super().__init__(probability)
        package_path = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
        path = package_path/'data'/'marks.json'
        with open(path, 'r', encoding='utf-8') as marks:
            self._marks = json.load(marks)

    def __call__(self, text: str) -> str:
        if random.random() <= self.probability:

            letter = random.choice(text)
            is_upper = True if letter.isupper() else False
            if letter.lower() in self._marks:
                    m = self._marks[letter.lower()]
                    mark = random.choice(m)
                    if is_upper:
                        mark = mark.capitalize()
                    l_ind = text.index(letter)
                    text = text[:l_ind] + mark + text[l_ind + 1:]
            return text
        return text
