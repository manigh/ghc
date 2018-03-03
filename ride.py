#!/bin/python2
import setting

class Ride:
    global variable

    def __init__(self, starti, startj, endi, endj, earliest, latest):
        self.starti= int(starti)
        self.startj= int(startj)
        self.endi= int(endi)
        self.endj= int(endj)
        self.earliest= int(earliest)
        self.latest= int(latest)
        self.drop_off_time = -1
        self.duration= abs(self.starti - self.endi)+abs(self.startj - self.endj)
        self.is_Done = False
        self.is_possible= True
        self.deadline=self.latest-self.distance

    #for all cars available at time t, select ride r:

    #if !isDone
    #if is_possible at t

    #if car at ij ,t: time_to_make_itAND_bonus[]
    #time_to_make_itAND_bonus[0]=can get to DEADLINE and have this time to spare (int)
    #time_to_make_itAND_bonus[1]=can get to BONUS and have this time to spare (int)

    #if time_to_make_itAND_bonus[0]<0 car cant do it(check others) !!! if no other can, isDone=True
    #if time_to_make_itAND_bonus[0]=0 last chance for this car just to make it
        #if time_to_make_itAND_bonus[1]=0 last chance for this car to BONUS
        #if time_to_make_itAND_bonus[1]>0 car has time to spare to BONUS
        #if time_to_make_itAND_bonus[1]<0 car has MISSED BONUS
    #if time_to_make_itAND_bonus[0]>0 car has time to spare just to make it
        #if time_to_make_itAND_bonus[1]=0 last chance for this car to BONUS
        #if time_to_make_itAND_bonus[1]>0 car has time to spare to BONUS
        #if time_to_make_itAND_bonus[1]<0 car has MISSED BONUS

    #if we decide to do it
    #do_it to return [drop_off_time t, get_location_to [ij], bonus_at_time int]

    def get_drop_off_loc(self):
        return [self.starti, self.startj]

    def get_drop_off_time(self):
        return self.drop_off_time;

    def do_it(self,t):
        self.drop_off_time = t+self.duration
        self.is_Done = True
        return [self.drop_off_time,get_drop_off_loc(),bonus_at_time(t)]

    def is_possible(self, t):
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

    def bonus_at_time(self, t):
        bonus=0
        if (self.is_possible and (not self.is_Done)):
            if(t<=self.earliest):
                bonus+=int(setting.B)
            bonus+=self.distance
        return bonus

    #this car, at time t, we already have checked if its availble
    def time_to_make_itAND_bonus(self, car_list_index, t):
        this_car=car_List[car_list_index]
        car_ij=this_car.pos_at_endof_lastride()
        distance_to=abs(car_ij[0]-self.starti)+abs(car_ij[1]-self.startj)
        time_to_make_it=time_left(t)-distance_to
        time_to_make_it_bonus=to-time_left_bonus(t)-distance_to
        return [time_to_make_it,time_to_make_it_bonus]
