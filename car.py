#!/bin/python2
import ride

class Car:
    def __init__(self, listOfDoneRides, i, j):
        self.i= i
        self.j= j
        self.listOfDoneRides= []
        self.available_time=0
        self.pos_at_endof_lastride=[self.i,self.j]


    #at time t:
    #if is_available(t)==True
    #car.get_pos_at_endof_lastride[], based on this:
    #car do_this_ride: returns[pos_at_endof_lastride [], available_time (int)]
    #!!! if available_time (int)>T => raise ValueError('ride took too long')
    #!!! if pos_at_endof_lastride [] != ride.get_drop_off_loc [] => raise ValueError('ride went somewhere else')

    def time_of_last_ride(self):
        return self.available_time

    def get_listOfDoneRides(self):
        return listOfDoneRides

    def get_pos_at_endof_lastride(self):
        return self.pos_at_endof_lastride

    def set_pos(self,location_list):
        self.i= location_list[0]
        self.j= location_list[1]
        self.pos_at_endof_lastride=[self.i, self.j]

    def distance_to_next_ride(self, ij):
        myij=self.pos_at_endof_lastride
        distance_to_next_ride=0
        distance_to_next_ride=abs(int(ij[0])-int(myij[0]))+abs(int(ij[1])-int(myij[1]))
        return int(distance_to_next_ride)

    def do_this_ride(self, this_ride, t):
        self.listOfDoneRides.append(this_ride)
        self.available_time=int(t)+int(this_ride.duration)+int(self.distance_to_next_ride(this_ride.get_pick_up_loc()))
        ij=this_ride.get_drop_off_loc()
        self.set_pos(ij)
        check_ij_from_ride=this_ride.do_it()
        if(check_ij_from_ride!=ij):
            raise ValueError('ride end is not same as car ij after done ride')
        return [self.get_pos_at_endof_lastride(),self.available_time]

    def is_available(self,t):
        return (self.available_time <= t)
