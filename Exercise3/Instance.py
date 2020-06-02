from typing import *


# Class that stores the the information from a ROW in the training Set
class Instance:

    def __init__(self, features: List[str], label: str):
        self._features: List[str] = features
        self._label: str = label

    def get_features(self) -> List[str]:
        return self._features

    def set_features(self, features: List[str]):
        self._features = features

    def append_feature(self, feature: str):
        self._features.append(feature)

    def get_label(self) -> str:
        return self._label

    def set_label(self, label: str):
        self._label = label
