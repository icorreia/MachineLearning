import numpy as np
import csv
from sklearn.datasets import make_classification
from pylab import rand

class DatasetReader():

        def __init__(self, num_features, num_train_insts, num_test_insts, train_file = '', test_file  = ''):

            self.num_features    = num_features
            self.num_train_insts = num_train_insts
            self.num_test_insts  = num_test_insts

            self.train_X = []
            self.train_y = []
            self.test_X  = []
            self.test_y  = []

            # Loads the datasets.
            if train_file != '':
                self.load_trainCsv(train_file)
                self.load_testCsv(test_file)
            else:
                #self.load_random_regression()
                #self.load_and_dataset()
                self.load_separable_dataset()

        #######################################################################################
        #  LOADERS                                                                            #
        #######################################################################################
        def load_trainCsv(self, fname, delimeter = ',', quotechar = '"'):
            self.train_X = np.zeros([self.num_train_insts, self.num_features])
            self.train_y = np.zeros([self.num_train_insts])

            self.readFromCsv(self.train_X, self.train_y, fname, delimeter, quotechar)

        def load_testCsv(self, fname, delimeter = ',', quotechar = '"'):
            self.test_X = np.zeros([self.num_test_insts, self.num_features])
            self.test_y = np.zeros([self.num_test_insts])

            self.readFromCsv(self.test_X, self.test_y, fname, delimeter, quotechar)

        def load_random_regression(self):
            train_random_set = make_classification(n_features = self.num_features, n_samples = self.num_train_insts, n_redundant = 0, n_repeated = 0)
            test_random_set  = make_classification(n_features = self.num_features, n_samples = self.num_test_insts , n_redundant = 0, n_repeated = 0)

            self.train_X = train_random_set[0]
            self.train_y = train_random_set[1]
            self.test_X  = test_random_set[0]
            self.test_y  = test_random_set[1]

        def load_separable_dataset(self):

            self.train_X = np.zeros([self.num_train_insts, self.num_features])
            self.train_y = np.zeros([self.num_train_insts])
            self.test_X = np.zeros([self.num_test_insts, self.num_features])
            self.test_y = np.zeros([self.num_test_insts])

            for i in xrange(self.num_train_insts / 2):
                self.train_X[i*2] = [(rand(1)[0]*2-1)/2-0.5, (rand(1)[0]*2-1)/2+0.5, 1]
                self.train_y[i*2] = 1

                self.train_X[i*2 + 1] = [(rand(1)[0]*2-1)/2+0.5, (rand(1)[0]*2-1)/2-0.5, 1]
                self.train_y[i*2 + 1] = 0

            for i in xrange(self.num_test_insts / 2):
                self.test_X[i*2] = [(rand(1)[0]*2-1)/2-0.5, (rand(1)[0]*2-1)/2+0.5, 1]
                self.test_y[i*2] = 1

                self.test_X[i*2 + 1] = [(rand(1)[0]*2-1)/2+0.5, (rand(1)[0]*2-1)/2-0.5, 1]
                self.test_y[i*2 + 1] = 0

        def load_and_dataset(self):

            self.num_features    = 3
            self.num_train_insts = 4
            self.num_test_insts  = 4

            self.train_X = np.zeros([self.num_train_insts, self.num_features])
            self.train_y = np.zeros([self.num_train_insts])

            self.test_X = np.zeros([self.num_test_insts, self.num_features])
            self.test_y = np.zeros([self.num_test_insts])

            # Defines train dataset.
            self.train_X[0] = [0,0,1]
            self.train_X[1] = [0,1,1]
            self.train_X[2] = [1,0,1]
            self.train_X[3] = [1,1,1]

            self.train_y[0] = 0 
            self.train_y[1] = 0
            self.train_y[2] = 0
            self.train_y[3] = 1

            # Defines test dataset.
            self.test_X[0] = [0,0,1]
            self.test_X[1] = [0,1,1]
            self.test_X[2] = [1,0,1]
            self.test_X[3] = [1,1,1]

            self.test_y[0] = 0 
            self.test_y[1] = 0
            self.test_y[2] = 0
            self.test_y[3] = 1

        #######################################################################################
        #  READERS                                        #
        #######################################################################################
        def readFromCsv(self, X, y, fname, in_delimeter, in_quotechar):
        
            with open(fname, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter = in_delimeter, quotechar = in_quotechar)

                line_counter = 0
                print "[INFO] Loading dataset '" + fname + "'..."
                for row in reader:

                    for i in xrange(self.num_features):
                        X[line_counter, i] = row[i]
                    y[line_counter] = row[self.num_features]

                    line_counter += 1
                
                print "[INFO] Finished loading dataset!"

