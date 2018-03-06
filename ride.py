#!/bin/python2
import car

class Ride:
    global variable

    def __init__(self, starti, startj, endi, endj, earliest, latest):
        self.starti= int(starti)
        self.startj= int(startj)
        self.endi= int(endi)
        self.endj= int(endj)
        self.earliest= int(earliest)
        self.latest= int(latest)
        self.duration= abs(self.starti - self.endi)+abs(self.startj - self.endj)
        self.is_Done = False
        self.is_possible= True
        self.deadline=self.latest-self.duration

    def set_is_done(self):
        self.is_Done = True

    def get_pick_up_loc(self):
        return [self.starti, self.startj]

    def get_drop_off_loc(self):
        return [self.endi, self.endj]

    def do_it(self):
        self.is_Done = True
        return self.get_drop_off_loc()

    def ride_is_possible(self, t):
        if (not self.is_possible):
            return False
        elif (self.is_Done):
            self.is_possible = False
            return False
        elif (self.latest >= t+self.duration):
            self.is_possible = True
            return True
        else:
            self.is_possible = False
            return False

    def time_left(self, t):
        time_left=self.deadline-t
        return time_left

    def time_left_bonus(self, t):
        time_left_bonus=self.earliest-t
        return time_left_bonus

    #this car, at time t, we already have checked if its availble
    def time_to_make_itAND_bonus(self, this_car, t):
        car_ij=this_car.pos_at_endof_lastride
        distance_to=0
        distance_to=int(this_car.distance_to_next_ride([self.starti, self.startj]))
        time_to_make_it=0
        time_to_make_it_bonus=0
        time_to_make_it=int(self.time_left(t))-distance_to
        time_to_make_it_bonus=int(self.time_left_bonus(t))-distance_to
        return [time_to_make_it,time_to_make_it_bonus]
