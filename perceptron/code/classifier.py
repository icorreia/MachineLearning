import numpy as np
import matplotlib as plt
import pylab as pyplt


class Classifier():


        def __init__(self, dataset_reader):

                self.num_features    = dataset_reader.num_features
                self.num_train_insts = dataset_reader.num_train_insts
                self.num_test_insts  = dataset_reader.num_test_insts

                self.train_X = dataset_reader.train_X
                self.train_y = dataset_reader.train_y
                self.test_X  = dataset_reader.test_X
                self.test_y  = dataset_reader.test_y

                # Evaluation metrics.
                self.TP = 0
                self.FP = 0
                self.FN = 0
                self.TN = 0

		self.recall    = 0
		self.precision = 0
		self.f1        = 0
		self.accuracy  = 0

        def train(self):
		pass

        def test(self):

	        predictions = self.evaluate()

        	for i in xrange(self.num_test_insts):
                	if self.test_y[i] == 1 and predictions[i] == 0:
                       		FN += 1
               		elif self.test_y[i] == 1 and predictions[i] == 1:
                        	TP += 1
                	elif self.test_y[i] == 0 and predictions[i] == 0:
                        	TN += 1
                	elif self.test_y[i] == 0 and predictions[i] == 1:
                        	FP += 1

		self.print_metrics()


        # Returns an array with the evaluations.
        def evaluate(self):
                return np.zeros([self.num_test_insts])

	def plot(self):
		if self.num_features > 2:
			print "[WARN] Too many features! Will only use the first two..."

	def print_metrics(self):
		print "True Positives: ", TP
		print "False Positives:", FP
		print "True Negatives: ", TN
		print "False Negatives:", FN
		print "----------------"
		print "Recall:   ", self.recall
		print "Precision:", self.precision
		print "F1:       ", self.f1
		print "Accuracy: ", self.accuracy
