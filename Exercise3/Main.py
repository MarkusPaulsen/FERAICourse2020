from DataSet import DataSet
from MLTree import MLTree
import sys

x = sys.argv
train_dataset = DataSet()
train_dataset.read_file(training_set_path=sys.argv[1], configuration_path=sys.argv[3])
test_data_set = DataSet()
test_data_set.read_file(training_set_path=sys.argv[2], configuration_path=sys.argv[3])
y = MLTree()
y.fit(train_dataset=train_dataset)
y.print_tree()
y.predict(test_dataset=test_data_set)
y.accuracy(test_dataset=test_data_set)
y.confusion_matrix(test_dataset=test_data_set)
