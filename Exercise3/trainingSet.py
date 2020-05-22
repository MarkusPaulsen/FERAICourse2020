from typing import *
from FERAICourse2020.Exercise3.Entry import *
from FERAICourse2020.Exercise3.Configuration import *
class trainingSet:
    def __init__(self):
        self._headers: List[str] = []
        self._entries: List[Entry] = []
        self.config = Configuration()

    def get_headers(self) -> List[str]:
        return self._headers

    def set_headers(self, headers: List[str]):
        self._headers = headers

    def get_entries(self) -> List[Entry]:
        return self._headers

    def set_entries(self, entries: List[str]):
        self._entries = entries



    def read_file(self, training_set_path: str, config_path: str):
        doc_training_set = open(training_set_path, encoding="utf8")
        doc_lines: List[str] = doc_training_set.readlines()
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


        doc_config = open(config_path, encoding="utf8")
        doc_config_lines: List[str] = doc_config.readlines()
        temp_config = Configuration()

        for line in doc_config_lines:
            split_line = line.split("=")

            if(split_line[0]=="mode"):
                self.config.set_mode(split_line[1].strip(".\n"))
            elif(split_line[0]=="model"):
                self.config.set_model(split_line[1].strip(".\n"))
            elif (split_line[0] == "max_depth"):
                self.config.set_max_depth(split_line[1].strip(".\n"))
            elif (split_line[0] == "num_trees"):
                self.config.set_num_trees(split_line[1].strip(".\n"))
            elif (split_line[0] == "feature_ratio"):
                self.config.set_feature_ratio(split_line[1].strip(".\n"))
            elif (split_line[0] == "example_ratio"):
                self.config.set_example_ratio(split_line[1].strip(".\n"))
            else:
                print("Error in reading Config file")


        doc_config.close()
        doc_training_set.close()



