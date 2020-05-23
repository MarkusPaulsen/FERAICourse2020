#Class that stores the the information from a ROW in the traaining Set
from typing import *
class Entry:

    def __init__(self):
        self._label: bool = False
        self.row: List[str] = []

    def get_label(self) -> bool:
        return self._label

    def set_label(self, label: bool):
        self._label = label

    def get_row(self) -> List[str]:
        return self._row

    def set_row(self, row: List[str]):
        self._row = row

    def append_element(self, element: str):
        self._row.append(element)