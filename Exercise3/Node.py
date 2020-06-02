from abc import ABC, abstractmethod
from typing import *


class Node(ABC):

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def print_tree(self) -> str:
        pass

    @abstractmethod
    def predict(self, test_feature: Dict[str, str]) -> str:
        pass
