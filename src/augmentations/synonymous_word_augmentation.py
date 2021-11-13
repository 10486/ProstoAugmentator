from src.augmentations.base_augmnentation import BaseAugmentation
import torch
from navec import Navec
import numpy as np
import random
import os
from pathlib import Path


class SynonymousWordAugmentation(BaseAugmentation):
    """ Аугментация, которая заменяет слово на похожее """
    def __init__(self, probability:float=0.5):
        self.probability = probability
        package_path = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
        path = package_path/'data'/'navec_hudlit_v1_12B_500K_300d_100q.tar'
        navec = Navec.load(path)
        self.vocab = navec.vocab
        self.embeddings = torch.Tensor(np.array([navec.pq[x] for x in range(len(navec.pq.indexes))]))
        self.idx2word = {navec.vocab.word_ids[i]:i for i in navec.vocab.word_ids}

    def __call__(self, text:str)->str:
        if random.random() < self.probability:
            words = text.split()
            idx_word = random.choice(range(len(words)))
            try:
                vocab_idx = self.vocab[words[idx_word]]
                if vocab_idx is not None:
                    similar_words = self.get_similar_words(vocab_idx)
                    words[idx_word] = random.choice(similar_words)
                    return " ".join(words)
            except KeyError:
                return text
        return text

    def get_similar_words(self, idx):
        dist = torch.cdist(self.embeddings[idx].unsqueeze(0), self.embeddings)[0]
        ids = dist.topk(k=4,largest=False).indices[1:]
        words = [self.idx2word[i.item()] for i in ids]
        return words
