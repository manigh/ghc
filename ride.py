class Ride:
    global variable

    def __init__(self, starti, startj,endi, endj, earliest, latest, number):
        self.starti= starti
        self.startj= startj
        self.endi= endi
        self.endj= endj
        self.earliest= earliest
        self.latest= latest
        self.number = number
        self.pickup_time = -1
        self.delivery_time = -1
        self.isdone = False

    def set_to_done(self,t):
        self.pickup_time = t
        self.delivery_time = t+abs(self.starti - self.endi)+abs(self.startj - self.endj)
        self.isdone = True

    def isWaiting(self):
        return not self.isdone
        
    def isDone(self):
        return self.isdone

