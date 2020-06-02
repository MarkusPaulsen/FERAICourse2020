from Instance import *
from Configuration import *


# Class that stores the configuration + training set (headers + entries)
# Class reads the correspondant files an populates the lists
# noinspection PyShadowingNames
class DataSet:
    def __init__(self):
        self._instance_header: List[str] = []
        self._instance_set: List[Instance] = []
        self._configuration: Optional[Configuration] = None

    def get_instance_header(self) -> List[str]:
        return self._instance_header

    def set_instance_header(self, instance_header: List[str]):
        self._instance_header = instance_header

    def get_instance_set(self) -> List[Instance]:
        return self._instance_set

    def set_instance_set(self, instance_set: List[Instance]):
        self._instance_set = instance_set

    def all_equal(self) -> Optional[str]:
        labels: List[str] = list(map(
            lambda instance: instance.get_label(),
            self._instance_set
        ))
        if len(labels) == 0:
            return ""
        reference_element = labels[0]
        a = list(filter(lambda label: label == reference_element, labels))
        b = len(a) == len(labels)
        if b:
            return reference_element
        else:
            return None

    # Reads files .cfg and .csv
    def read_file(self, training_set_path: str, configuration_path: str):
        training_set_file = open(training_set_path, encoding="utf8")
        training_set_lines: List[str] = training_set_file.readlines()
        training_set_file.close()
        self._instance_header = list(map(lambda header: header.strip(".\n"), training_set_lines[0].split(",")))
        instance_set_lines = list(map(lambda line: line.split(","), training_set_lines[1:]))
        for training_set_line in instance_set_lines:
            training_set_line_cleaned = list(map(lambda line: line.strip(".\n"), training_set_line))
            self._instance_set.append(
                Instance(
                    features=training_set_line_cleaned[0:-1:1],
                    label=training_set_line_cleaned[-1]
                )
            )
        configuration_file = open(configuration_path, encoding="utf8")
        configuration_lines: List[str] = configuration_file.readlines()
        configuration_file.close()
        cls: List[Tuple[str, str]] = list(map(
            lambda configuration_line: configuration_line.split("="),
            configuration_lines
        ))
        self._configuration = Configuration(
            mode=cls[0][1].strip(".\n"), model=cls[1][1].strip(".\n"),
            max_depth=int(cls[2][1].strip(".\n")), num_trees=int(cls[3][1].strip(".\n")),
            feature_ratio=int(cls[4][1].strip(".\n")), example_ratio=int(cls[5][1].strip(".\n"))
        )

    def remove_header_element(self, header_element: str) -> dict:
        some_dict: Dict[str, DataSet] = {}
        header_element_index = self._instance_header.index(header_element)
        header_element_values = list(set(map(
            lambda instance: instance.get_features()[header_element_index],
            self._instance_set
        )))
        header_element_values.sort()
        for value in header_element_values:
            new_instance_header = self._instance_header.copy()
            new_instance_header.pop(header_element_index)
            new_instance_set: List[Instance] = []
            for instance in self._instance_set.copy():
                new_instance_set.append(Instance(instance.get_features().copy(), instance.get_label()))
            new_instance_set: List[Instance] = list(filter(
                lambda instance: instance.get_features()[header_element_index] == value,
                new_instance_set
            )).copy()
            for instance in new_instance_set:
                instance.get_features().pop(header_element_index)
            some_dict[value] = DataSet()
            some_dict[value].set_instance_header(instance_header=new_instance_header)
            some_dict[value].set_instance_set(instance_set=new_instance_set)
        return some_dict
