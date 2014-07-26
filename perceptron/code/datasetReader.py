import numpy as np
import csv

class DatasetReader():

        def __init__(self, num_features, num_train_insts, train_file, num_test_insts, test_file):

                self.num_features    = num_features
                self.num_train_insts = num_train_insts
                self.num_test_insts  = num_test_insts

		self.train_X = []
		self.train_y = []
		self.test_X  = []
		self.test_y  = []

                # Loads the datasets.
                self.load_trainCsv(train_file)
                self.load_testCsv(test_file)

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

	#######################################################################################
	#  READERS									      #
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

