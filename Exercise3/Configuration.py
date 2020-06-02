# Class that stores the information from .cfg files
class Configuration:
    def __init__(self, mode: str, model: str, max_depth: int, num_trees: int, feature_ratio: int, example_ratio: int):
        self._mode: str = mode
        self._model: str = model
        self._max_depth: int = max_depth
        self._num_trees: int = num_trees
        self._feature_ratio: int = feature_ratio
        self._example_ratio: int = example_ratio

    def get_mode(self) -> str:
        return self._mode

    def set_mode(self, mode: str):
        self._mode = mode

    def get_model(self) -> str:
        return self._model

    def set_model(self, model: str):
        self._model = model

    def get_max_depth(self) -> int:
        return self._max_depth

    def set_max_depth(self, max_depth: int):
        self._max_depth = max_depth

    def get_num_trees(self) -> int:
        return self._num_trees

    def set_num_trees(self, num_trees: int):
        self._num_trees = num_trees

    def get_feature_ratio(self) -> int:
        return self._feature_ratio

    def set_feature_ratio(self, feature_ratio: int):
        self._feature_ratio = feature_ratio

    def get_example_ratio(self) -> int:
        return self._example_ratio

    def set_example_ratio(self, example_ratio: int):
        self._example_ratio = example_ratio
