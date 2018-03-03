#!/bin/python2
import setting

class Ride:
    global variable

    def __init__(self, starti, startj, endi, endj, earliest, latest, number):
        self.starti= int(starti)
        self.startj= int(startj)
        self.endi= int(endi)
        self.endj= int(endj)
        self.earliest= int(earliest)
        self.latest= int(latest)
        self.number = int(number)
        self.pickup_time = -1
        self.drop_off_time = -1
        self.distance= abs(self.starti - self.endi)+abs(self.startj - self.endj)
        self.is_Done = False
        self.car_associated= None
        self.deadline=self.latest-self.distance

    #0)if !isDone
    #0)if is_possible, is it possible to do at all

    #0)if car at ij ,t: time_to_make_it<0 this car cant do it (check if others can)-> !!! if no other can, its lost isDone=True

    #Do only if above is not true
    #1)if car at ij ,t: time_to_make_it=0 last chance for this car (check if others can)
    #2)if car at ij ,t: time_to_make_it>0 has time to be late (definately check others)
        #1,2)1) time_to_make_it_bonus=0 last chance for this car get bonus (check if others can)
        #1,2)2) time_to_make_it_bonus>0, has time to get bonus (definately check others)
        #1,2)3) time_to_make_it_bonus<0, car has lost chance to bonus (if no other can make it, do it)

    #do_it to return get_drop_off_time, get_location_to, bonus_at_time


    def get_drop_off_time(self):
        return get_drop_off_time;

    def do_it(self,t):
        self.drop_off_time = t+self.distance
        self.is_Done = True
        return(get_drop_off_time,get_location_to,bonus_at_time(t,int(setting.B)))

    def is_possible(self, t):
        if (is_Done):
            return False
        if (self.latest >= t+self.distance):
            return True;
        else:
            return False

    #ride is not done, left to finish ontime>=0, how much exactly?
    def time_left(self, t):
        time_left=self.deadline-t
        return time_left

    #ride is not done, left to get bonus >=0, how much exactly?
    def time_left_bonus(self, t):
        time_left_bonus=self.earliest-t
        return time_left_bonus

    def bonus_at_time(self, t):
        bonus=0
        if(t<=self.earliest):
            bonus+=int(setting.B)
        bonus+=self.distance
        return bonus

    #car related
    def time_to_make_itAND_bonus(self, car_number, t):
        if (not is_possible(t)):
            return [-1,-1]
        else:
            distance_to=abs(car_List[car_number].i-starti)+abs(car_List[car_number].j-startj)
            time_to_make_it=distance_to-time_left(t)
            time_to_make_it_bonus=distance_to-time_left_bonus(t)
            return [time_to_make_it,time_to_make_it_bonus]
