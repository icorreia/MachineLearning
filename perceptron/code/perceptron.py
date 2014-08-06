import classifier
import numpy as np
import matplotlib.pyplot as plt
import pylab as pyplt

class Perceptron(classifier.Classifier):

        # The unit step function to classify the instance.
        def f(self, x):
            if x > 0.0:
                return 1
            return 0

        def train(self):

            print "[INFO] Training model..."

            weights = np.zeros([self.num_features])
            # The learning step.
            self.eta  = 1
            self.bias = 0

            for i in xrange(self.num_train_insts):

                inst     = self.train_X[i]
                expected = self.train_y[i]

                pred = self.f(weights.dot(inst) + self.bias)

                # Update weights.
                if expected != pred:
                    weights += self.eta * (expected - pred) * inst

            return weights

        def evaluate(self):

            predictions = np.zeros([self.num_test_insts])

            for i in xrange(self.num_test_insts):
                inst = self.test_X[i]
                predictions[i] = self.f(self.weights.dot(inst) + self.bias)

            return predictions

        def plot(self, predictions):
            if self.num_features > 2:
                print "[WARN] Too many features! Will only use the first two..."

            # Plots the points.
            for i in xrange(len(self.test_X)):

                inst  = self.test_X[i]
                label = self.test_y[i]
                pred  = predictions[i]

                if label == pred:
                    colour = 'b'
                else:
                    colour = 'r'

                if label == 0:
                    plt.scatter(inst[0], inst[1], marker = 'o', color = colour)
                else:
                    plt.scatter(inst[0], inst[1], marker = 'x', color = colour)
            

            # Plots the decision boundary. The '* 1000' is for giving the 
            # impression of an infinite line.
            plt.plot([-self.weights[1] * 1000, self.weights[1] * 1000], [self.weights[0] * 1000 + self.bias, -self.weights[0] * 1000 + self.bias])

            # The decision line is made by two points. We shorten the screen so it
            # will seem like it is an infinite line.
            plt.xlim([min(self.test_X[:,0]) - 5, max(self.test_X[:,0]) + 5])
            plt.ylim([min(self.test_X[:,1]) - 5, max(self.test_X[:,1]) + 5])

            plt.show()


