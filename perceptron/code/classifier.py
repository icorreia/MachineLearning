import numpy as np

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

            self.weights = np.zeros([self.num_features])

            self.eta  = 0

        def train(self):
            pass

        def test(self):

            print "[INFO] Testing model..."

            predictions = self.evaluate()

            for i in xrange(self.num_test_insts):
                if self.test_y[i] == 1 and predictions[i] == 0:
                        self.FN += 1
                elif self.test_y[i] == 1 and predictions[i] == 1:
                        self.TP += 1
                elif self.test_y[i] == 0 and predictions[i] == 0:
                        self.TN += 1
                elif self.test_y[i] == 0 and predictions[i] == 1:
                        self.FP += 1

            self.print_metrics(predictions)


        # Returns an array with the evaluations.
        def evaluate(self):
            return np.zeros([self.num_test_insts])            

        # Executes both the training and the testing stages.
        def execute(self):
            self.weights = self.train()
            self.test()

        def plot(self, predictions):
            pass

        def print_metrics(self, predictions):
            print "Weight vector: ", self.weights, "\n"
            print "True Positives: ", self.TP
            print "False Positives:", self.FP
            print "True Negatives: ", self.TN
            print "False Negatives:", self.FN
            print "----------------"
            print "Recall:   ", self.recall
            print "Precision:", self.precision
            print "F1:       ", self.f1
            print "Accuracy: ", self.accuracy, "\n"

            self.plot(predictions)
