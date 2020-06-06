import copy
from typing import *

from DataSet import DataSet
from LeafNode import LeafNode
from Node import Node
from TreeID3 import TreeID3


class TreeNode(Node):

    def __init__(self, depth: int, header_element: str, full_data_set: DataSet, branch_data_sets: Dict[str, DataSet]):
        self._depth: int = depth
        self._header: str = header_element
        self._full_data_set: DataSet = full_data_set
        self._branch_data_sets: Dict[str, DataSet] = branch_data_sets
        self._branches: Dict[str, Node] = {}

    def fit(self):
        branch_list: List[str] = list(self._branch_data_sets.keys())
        if len(branch_list) == 1:
            only_branch_dataset: DataSet = self._branch_data_sets[branch_list[0]]
            most_likely: str = only_branch_dataset.find_most_likely()
            self._branches[branch_list[0]] = \
                LeafNode(
                    depth=self._depth + 1,
                    decision=most_likely
                )
        else:
            for branch_data_set in self._branch_data_sets:
                train_dataset = self._branch_data_sets[branch_data_set]
                if train_dataset.get_configuration() is not None:
                    max_depth: int = train_dataset.get_configuration().get_max_depth()
                    if max_depth == -1 or max_depth > (self._depth + 1):
                        if train_dataset.all_equal() is not None:
                            self._branches[branch_data_set] = LeafNode(depth=self._depth + 1, decision=train_dataset.all_equal())
                        else:
                            train_dataset_copy: DataSet = copy.deepcopy(train_dataset)
                            tree_id_3: TreeID3 = TreeID3(train_dataset_copy)
                            best_header_element: Tuple[str, float] = tree_id_3.get_gain_header()[0]
                            branch_data_sets: Dict[str, DataSet] = train_dataset_copy.remove_header_element(
                                header_element=best_header_element[0], configuration=train_dataset_copy.get_configuration()
                            )
                            self._branches[branch_data_set] = TreeNode(
                                depth=self._depth + 1,
                                header_element=best_header_element[0],
                                full_data_set=train_dataset,
                                branch_data_sets=branch_data_sets
                            )
                    else:
                        self._branches[branch_data_set] = LeafNode(depth=self._depth + 1,
                                                                   decision=train_dataset.find_most_likely())
                    self._branches[branch_data_set].fit()

    def print_tree(self) -> str:
        return_string = str(self._depth) + ":" + self._header
        for branch in self._branches:
            if type(self._branches[branch]) == TreeNode:
                return_string = return_string + ", " + self._branches[branch].print_tree()

        return return_string

    def predict(self, test_feature: Dict[str, str]) -> str:
        try:
            return self._branches[test_feature[self._header]].predict(test_feature=test_feature)
        except KeyError:
            x = self._full_data_set.find_most_likely()
            return self._full_data_set.find_most_likely()
