#!/bin/python2
import ride
from ride import *
import car
import sys
import parser
import random

def do(r, c, t):
    c.do_this_ride(r, t)
    r.isDone=True

def pick_from_available_cars(r, available_cars, t):
    bonus_cars=[]
    deadline_cars=[]
    for c in available_cars:
        time_to_make_itAND_bonus_list=r.time_to_make_itAND_bonus(c,t)
        spare_toDEADLINE = int(time_to_make_itAND_bonus_list[0])
        spare_toBONUS = int(time_to_make_itAND_bonus_list[1])
        if(spare_toDEADLINE==0):
            deadline_cars.append(c)
        elif(spare_toDEADLINE>0):
            deadline_cars.append(c)
            if(spare_toBONUS>=0):
                bonus_cars.append(c)
    d=len(deadline_cars)
    b=len(bonus_cars)
    if (d==0):
        print "no car could make it to ride on time for ride " + str(ride_list.index(r))
    elif (d==1):
        c=deadline_cars[0]
        print "only car " +  str(car_list.index(c)) + " could make it to ride  " + str(ride_list.index(r))
        do(r,c,t)
    elif (d>1):
        if (b==0):
            print "no car could get the bonus on time for ride " + str(ride_list.index(r))
            c_index=random.randint(0,len(deadline_cars)-1)
            c=deadline_cars[c_index]
            print "picked car " +  str(car_list.index(c)) + " to do the ride  " + str(ride_list.index(r))
            do(r,c,t)
        elif (b==1):
            c=bonus_cars[0]
            print "only car " +  str(car_list.index(c)) + " could get bonus on ride  " + str(ride_list.index(r))
            do(r,c,t)
        elif (b>1):
            c_index=random.randint(0,len(bonus_cars)-1)
            c=bonus_cars[c_index]
            print "picked car " +  str(car_list.index(c)) + " to get bonus on ride  " + str(ride_list.index(r))
            do(r,c,t)
    return True

filename = sys.argv[1]
f = open(filename)
passed_list=[]
passed_list = parser.read(f)
f.close()
I=int(passed_list[0])
J=int(passed_list[1])
F=int(passed_list[2])
R=int(passed_list[3])
B=int(passed_list[4])
T=int(passed_list[5])
car_list=passed_list[6]
ride_list=passed_list[7]

t=0
while t <= T:
    #for all rides
    #if !isDone
    #if ride_is_possible at t
    for r in ride_list:
        if(r.ride_is_possible(int(t))):
            #for all cars
            #if car.is_available(t)==True
            available_cars=[]
            for c in car_list:
                #remove r is done to try diff ways
                if(c.is_available(t)):
                    available_cars.append(c)
            if (len(available_cars)==0):
                print "no car available for ride " + str(ride_list.index(r)) + " at time " + str(t)
            else:
                print "We can pick " + str(len(available_cars)) + " cars for ride " + str(ride_list.index(r)) + " at time " + str(t)
                pick_from_available_cars(r, available_cars, t)
    t+=1
outputfilename = filename .rstrip('in')
outputfilename += "out"
o = open(outputfilename, "w")
parser.save(o, car_list, ride_list)
o.close()
