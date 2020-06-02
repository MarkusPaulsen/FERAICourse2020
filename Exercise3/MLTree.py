import math
from typing import *
import copy

from DataSet import DataSet
from LeafNode import LeafNode
from Node import Node
from TreeID3 import TreeID3
from TreeNode import TreeNode


# noinspection DuplicatedCode
class MLTree:
    def __init__(self):
        self._root: Optional[Node] = None

    def fit(self, train_dataset: DataSet):
        if train_dataset.all_equal() is not None:
            self._root = LeafNode(depth=0, decision=train_dataset.all_equal() is not None)
        else:
            train_dataset_copy: DataSet = copy.deepcopy(train_dataset)
            tree_id_3: TreeID3 = TreeID3(train_dataset_copy)
            best_header_element: Tuple[str, float] = tree_id_3.get_gain_header()[0]
            branch_data_sets: Dict[str, DataSet] = train_dataset_copy.remove_header_element(
                header_element=best_header_element[0]
            )
            self._root = TreeNode(
                depth=0, header_element=best_header_element[0], branch_data_sets=branch_data_sets
            )
        self._root.fit()

    def print_tree(self):
        print(self._root.print_tree())

    def predict(self, test_dataset: DataSet):
        print_string = ""

        if self._root is not None:
            test_features: List[List[str]] = list(map(
                lambda instance: instance.get_features(),
                test_dataset.get_instance_set()
            ))
            for test_feature in test_features:
                feature_data = {}
                for index, element in enumerate(test_dataset.get_instance_header()[0:-1]):
                    feature_data[element] = test_feature[index]
                print_string = print_string + self._root.predict(test_feature=feature_data) + " "
        print(print_string.strip())

    def accuracy(self, test_dataset: DataSet):
        if self._root is not None:
            test_features: List[List[str]] = list(map(
                lambda instance: instance.get_features(),
                test_dataset.get_instance_set()
            ))
            test_predictions: List[str] = []
            for test_feature in test_features:
                feature_data = {}
                for index, element in enumerate(test_dataset.get_instance_header()[0:-1]):
                    feature_data[element] = test_feature[index]
                test_predictions.append(self._root.predict(test_feature=feature_data))
            test_labels: List[str] = list(map(
                lambda instance: instance.get_label(),
                test_dataset.get_instance_set()
            ))
            correct = len(list(filter(
                lambda compare: compare[0] == compare[1],
                (zip(test_predictions, test_labels))
            )))
            accuracy = correct / len(test_labels)
            print((math.floor(accuracy * 100000)) / 100000.0)

    def confusion_matrix(self, test_dataset: DataSet):
        if self._root is not None:
            test_features: List[List[str]] = list(map(
                lambda instance: instance.get_features(),
                test_dataset.get_instance_set()
            ))
            test_predictions: List[str] = []
            for test_feature in test_features:
                feature_data = {}
                for index, element in enumerate(test_dataset.get_instance_header()[0:-1]):
                    feature_data[element] = test_feature[index]
                test_predictions.append(self._root.predict(test_feature=feature_data))
            test_labels: List[str] = list(map(
                lambda instance: instance.get_label(),
                test_dataset.get_instance_set()
            ))
            tp = len(list(filter(
                lambda compare: (compare[0] == "yes" or compare[0] == "True")
                and (compare[1] == "yes" or compare[1] == "True"),
                (zip(test_predictions, test_labels))
            )))
            tn = len(list(filter(
                lambda compare: (compare[0] == "no" or compare[0] == "False")
                and (compare[1] == "no" or compare[1] == "False"),
                (zip(test_predictions, test_labels))
            )))
            fn = len(list(filter(
                lambda compare: (compare[0] == "no" or compare[0] == "False")
                                and (compare[1] == "yes" or compare[1] == "True"),
                (zip(test_predictions, test_labels))
            )))
            fp = len(list(filter(
                lambda compare: (compare[0] == "yes" or compare[0] == "True")
                                and (compare[1] == "no" or compare[1] == "False"),
                (zip(test_predictions, test_labels))
            )))
            print(str(tn) + " " + str(fp))
            print(str(fn) + " " + str(tp))
