import random

class Ind:

    def __init__(self):

        self.cof = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]
        self.fitness = None

    def printer(self):
        print(f'{self.cof[3]}-{self.cof[2]}-{self.cof[1]}-{self.cof[0]}')

    def fit_ness(self, ys, xs):
        sum = 0
        for i in range(100):
            sum += (ys[i] - (self.cof[3]*(xs[i]**3) + self.cof[2]*(xs[i]**2) + self.cof[1]*xs[i] + self.cof[0]))**2
        mse = sum / 100
        self.fitness = (1 / (1+mse))

