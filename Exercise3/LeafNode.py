from typing import *

from Node import Node


class LeafNode(Node):

    def __init__(self, depth: int, decision: str):
        self._depth: int = depth
        self._decision: str = decision

    def fit(self):
        pass

    def print_tree(self) -> str:
        return ""

    def predict(self, test_feature: Dict[str, str]) -> str:
        return self._decision
