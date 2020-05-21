from typing import *
from FERAICourse2020.Exercise3.Entry import *
class trainingSet:
    def __init__(self):
        self._headers: List[str] = []
        self._entries: List[Entry] = []

    def get_headers(self) -> List[str]:
        return self._headers

    def set_headers(self, headers: List[str]):
        self._headers = headers

    def get_entries(self) -> List[Entry]:
        return self._headers

    def set_entries(self, entries: List[str]):
        self._entries = entries



    def read_file(self, path: str):
        doc = open(path, encoding="utf8")
        doc_lines: List[str] = doc.readlines()
        header_line: List[str] = doc_lines[0].split(",")
        self.set_headers(header_line)

        for line in doc_lines:
            if not (line.__contains__("yes") or line.__contains__("no")):
                continue

            temp_entry = Entry()
            split_line: List[str] = line.split(",")
            if split_line[-1] == "yes":
                temp_entry.set_label(True)
            else:
                temp_entry.set_label(False)

            for word in split_line:
                if not (word == "yes" or word == "no"):
                    temp_entry.append_element(word)
