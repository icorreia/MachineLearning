from datasetReader import DatasetReader
from perceptron import Perceptron

#reader = DatasetReader(3, 4, 8, "train.db", "test.db") 
reader = DatasetReader(2, 200, 100) 

perceptron = Perceptron(reader)
perceptron.execute()

print "[INFO] Finished!"
