import random

class Bombs:
    @staticmethod
    def createbomb():
        row = random.sample([0,1,2,3,4],2)
        col = random.sample([0,1,2,3,4],2)
        return [(x, y) for x in row for y in col ]
        pass
