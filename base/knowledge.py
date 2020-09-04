class Knowledge:
    def __init__(self):
        self.KB = []
        self.alpha = []
    def setKnowledge(self, KB, alpha):
        self.KB = KB
        self.alpha = alpha
    def getKB(self):
        return self.KB
    def getAlpha(self):
        return self.alpha
