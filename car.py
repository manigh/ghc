class Car:
    def __init__(self, listOfDoneRides, i, j):
        self.i= i
        self.j= j
        self.listOfDoneRides= []
        self.schedule = {}
        self.is_not_available_until = 0

    def getPos(self):
        return (self.i,self.j)

    def is_available(self,t):
        return self.is_not_available_until <= t

