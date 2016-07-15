import numpy as np

class LogisticRegression(object): 
    def __init__(self):
        # TODO 
        # flag for opt method
        # make calls to seperate inits based on above
        # read data from file?
        pass

    def forward_pass(self):
        # forward pass for prediction
        pass

    def compute_gradient(self):
        # evaluate local gradient
        pass

    def compute_hession(self):
        # needed for newtons
        # and backtracking line search??
        pass

    def begin_optimzation(self):
        # this is what the optimizers will override, 
        #     all other methods will be reused
        raise Exception('Optimization Method Not Implemented')
