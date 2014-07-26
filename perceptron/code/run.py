from datasetReader import DatasetReader
from perceptron import Perceptron

reader = DatasetReader(3, 4, "train.db", 8, "test.db") 
perceptron = Perceptron(reader)

print "[INFO] Finished!"
