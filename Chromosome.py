class Chromosome:
    
    def __init__(self):
        self.gens = []

    def setGenAt(self, gen):
        self.gens.append(gen)
    
    def getGenAt(self, i):
        return self.gens[i]