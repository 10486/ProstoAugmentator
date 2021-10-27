from src.augmentations.base_augmnentation import BaseAugmentation
import random
import yaml
import json
import requests


class TranslateAugmentation(BaseAugmentation):
    """ Аугментация, которая совершает перевод на английский язык и обратно """
    def __init__(self, probability:float=0.5, lang:str="en"):
        super().__init__(probability)
        self.lang = lang
        with open("config/translator.yml", "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        self.config = config

    def __call__(self, text:str)->str:
        if random.random() <= self.probability:
            translated = json.loads(self.translate(text, lang=self.lang))["translations"][0]["text"]
            augmented = json.loads(self.translate(translated, lang="ru"))["translations"][0]["text"]
            return augmented
        return text

    def translate(self, text:str, lang:str="ru"):

        data = {
            "texts": [text],
            "targetLanguageCode": lang
        }
        data = {**data, **self.config["data"]}
        data = json.dumps(data)
        response = requests.request("POST", self.config["url"], data=data, headers=self.config["headers"])
        return response.text
