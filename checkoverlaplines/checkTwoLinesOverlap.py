class CheckLinesOverlap:
    def __init__(self):
        self.firstline = {}
        self.secondline = {}
    
    def linesOverlapp(self,firstline, secondline):
        self.firstline = firstline
        self.secondline = secondline
        return self.firstline[1] >= self.secondline[0] and self.secondline[1] >= self.firstline[0]
    
    
checkoverlappinglines = CheckLinesOverlap()
firstline = (1,5)
secondline = (2,6)
print(checkoverlappinglines.linesOverlapp(firstline, secondline))
    