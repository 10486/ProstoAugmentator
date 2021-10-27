from src.augmentations.base_augmnentation import BaseAugmentation
import random


class DeleteChatAugmentation(BaseAugmentation):
    """ Аугментация, которая удаляет случайную букву в слове """

    def __call__(self, text: str) -> str:
        if self.probability <= random.random():
            letter = random.choice(text)
            newtext = text.replace(letter, '')
            return newtext
        return text
