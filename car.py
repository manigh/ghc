#!/bin/python2
import ride

class Car:
    def __init__(self, listOfDoneRides, i, j):
        self.i= i
        self.j= j
        self.listOfDoneRides= []
        self.schedule = {}
        self.available_time=0
        self.pos_at_endof_lastride=[0,0]


    #at time t:
    #if is_available(t)==True
    #get_pos_at_endof_lastride[] based on this:
    #if we decided that the car can make it based on its distance and t
    #car do_this_ride: returns[pos_at_endof_lastride [], available_time (int)]

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

    def do_this_ride(self, this_ride, t):
        self.listOfDoneRides.append(this_ride)
        self.available_time=t+this_ride.duration
        ij=this_ride.get_drop_off_loc()
        set_pos(ij)
        return [get_pos_at_endof_lastride(),self.available_time]


    def is_available(self,t):
        return (time_of_last_ride() <= t)
