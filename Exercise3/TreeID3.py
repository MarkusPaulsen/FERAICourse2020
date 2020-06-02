import math
from functools import reduce

from DataSet import *


# Class resposible for the storage and operations related with the ID3 tree
# noinspection PyMethodMayBeStatic,PyShadowingNames
class TreeID3:

    def __init__(self, train_dataset: DataSet):
        self._train_dataset = train_dataset
        self._gain_header: Dict[str, float] = {}
        self._set_calc()

    def get_gain_header(self) -> List[Tuple[str, float]]:
        output: List[Tuple[str, float]] = []
        for entry in self._gain_header:
            output.append((entry, self._gain_header[entry]))
        output.sort(key=(lambda entry: (float(entry[1]))), reverse=True)
        return output

    # Calc of entropy for 2 values p[positive] n[negative]
    def _calc_entropy(self, p: int, n: int) -> float:
        if p == 0 or n == 0:
            return 0
        else:
            return (-p / (p + n)) * (math.log2(p / (p + n))) - ((n / (p + n)) * (math.log2(n / (p + n))))


    def _set_calc(self):
        train_dataset_yes = len(list(filter(
            lambda instance: instance.get_label() == "yes" or instance.get_label() == "True",
            self._train_dataset.get_instance_set()
        )))
        train_dataset_no = len(self._train_dataset.get_instance_set()) - train_dataset_yes
        train_dataset_entropy = self._calc_entropy(train_dataset_yes, train_dataset_no)
        average_information_header: Dict[str, float] = {}

        for index, header in list(enumerate(self._train_dataset.get_instance_header(), 0))[0:-1:1]:
            header_attributes = list(set(map(
                lambda instance: instance.get_features()[index],
                self._train_dataset.get_instance_set()
            )))
            header_attribute_entropy: Dict[str, float] = {}
            for header_attribute in header_attributes:
                header_attribute_instances = list(filter(
                    lambda instance: instance.get_features()[index] == header_attribute,
                    self._train_dataset.get_instance_set()
                ))

                header_attribute_instances_yes = len(list(filter(
                    lambda instance: instance.get_label() == "yes" or instance.get_label() == "True" ,
                    header_attribute_instances
                )))
                header_attribute_instances_no = len(list(filter(
                    lambda instance: instance.get_label() == "no" or instance.get_label() == "False",
                    header_attribute_instances
                )))
                header_attribute_entropy_value = self._calc_entropy(
                        header_attribute_instances_yes, header_attribute_instances_no
                    )
                header_attribute_entropy_weight = (header_attribute_instances_yes + header_attribute_instances_no)/\
                    (train_dataset_yes + train_dataset_no)

                header_attribute_entropy[header_attribute] = header_attribute_entropy_value * header_attribute_entropy_weight
            average_information_header[header] = reduce(
                lambda accumulator, entropy: accumulator + entropy,
                header_attribute_entropy.values()
            )
        for header in average_information_header:
            self._gain_header[header] = train_dataset_entropy - average_information_header[header]
