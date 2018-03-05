#!/bin/python2
import car

class Ride:
    global variable

    def __init__(self, starti, startj, endi, endj, earliest, latest, B):
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
        self.B=int(B)


    #for all rides
    #if !isDone
    #if is_possible at t

    #for all cars
    #if car.is_available(t)==True
    #car.get_pos_at_endof_lastride[], based on this:
    #car do_this_ride: returns[pos_at_endof_lastride [], available_time (int)]
    #!!! if available_time (int)>T => raise ValueError('ride took too long')
    #!!! if pos_at_endof_lastride [] != ride.get_drop_off_loc [] => raise ValueError('ride went somewhere else')

    #if car at ij ,t: time_to_make_itAND_bonus(car,t)=[_,_]
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
    #this_car.do_this_ride.do_this_ride()
    #updates this_car.listOfDoneRides
    #updates this_car.available_time set to t+this_ride.duration+this_car.distance_to_next_ride(this_ride)
    #updates this_car.ij -> set to get_drop_off_loc
    #also calls do_it(this_car,t) returns bonus_awarded and updates ride.isDone to True

    def get_pick_up_loc(self):
        return [self.starti, self.startj]

    def get_drop_off_loc(self):
        return [self.endi, self.endj]

    def do_it(self, t):
        self.is_Done = True
        return [get_drop_off_loc(),bonus_at_time(t)]

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
                bonus+=self.B
            bonus+=self.distance
        return bonus

    #this car, at time t, we already have checked if its availble
    def time_to_make_itAND_bonus(self, this_car, t):
        car_ij=this_car.pos_at_endof_lastride()
        distance_to=this_car.distance_to_next_ride(get_pick_up_loc)
        time_to_make_it=time_left(t)-distance_to
        time_to_make_it_bonus=to-time_left_bonus(t)-distance_to
        return [time_to_make_it,time_to_make_it_bonus]
