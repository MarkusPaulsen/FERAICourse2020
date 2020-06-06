from DataSet import DataSet
from MLTree import MLTree
import sys

train_dataset = DataSet()
train_dataset.read_file(training_set_path=sys.argv[1], configuration_path=sys.argv[3])
test_dataset = DataSet()
test_dataset.read_file(training_set_path=sys.argv[2], configuration_path=sys.argv[3])
decision_tree = MLTree()
decision_tree.fit(train_dataset=train_dataset)
decision_tree.print_tree()
decision_tree.predict(test_dataset=test_dataset)
decision_tree.accuracy(test_dataset=test_dataset)
decision_tree.confusion_matrix(test_dataset=test_dataset)
