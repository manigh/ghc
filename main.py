#!/bin/python2
import ride
from ride import *
import car
import sys
import parser

def do(r, c, t):
    if(r.is_Done==False):
        car_do_this_ride_check=[]
        car_do_this_ride_check=c.do_this_ride(r, t)
        r.do_it()
        cars_new_ij=[]
        cars_new_ij=car_do_this_ride_check[0]
        cars_new_avalability=car_do_this_ride_check[1]
        if(r.ride_is_possible(t) or (r.is_Done == False)):
            raise ValueError('ride has not been marked done')
        elif(not(r in c.listOfDoneRides)):
            raise ValueError('ride doesnt have this_ride in its list')
        elif(cars_new_ij!=r.get_drop_off_loc()):
            raise ValueError('car didnt end up where it should have')
        elif(cars_new_avalability>T):
            raise ValueError('ride took too long')
        elif(cars_new_avalability>T):
            raise ValueError('ride took too long')
        else:
            print "car index " + str(car_list.index(c)) + " is assigned to ride " + str(ride_list.index(r))

def pick_from_available_cars(r, available_cars, t):
    number_of_bonus_cars=0
    for c in available_cars:
        time_to_make_itAND_bonus_list=r.time_to_make_itAND_bonus(c,t)
        spare_toDEADLINE = int(time_to_make_itAND_bonus_list[0])
        spare_toBONUS = int(time_to_make_itAND_bonus_list[1])
        if(spare_toDEADLINE<0):
            print "car index " + str(car_list.index(c)) + " was unable to pick ride " + str(ride_list.index(r))
        elif(spare_toDEADLINE==0):
            #change later, but so far it will pick the car that has the last chance to get it
            do(r,c,t)
            #bonus not calculated
        elif(spare_toDEADLINE>0):
            if(spare_toBONUS<0):
                #missed bonus so maybe dont
                do(r,c,t)
            elif(spare_toBONUS==0):
                #change later, but defo do it now
                number_of_bonus_cars+=1
                do(r,c,t)
            elif(spare_toBONUS>0):
                #has time to get bonus so maybe prefer above
                number_of_bonus_cars+=1
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
        if(r.ride_is_possible(int(t)) and (r.is_Done==False)):
            #for all cars
            #if car.is_available(t)==True
            available_cars=[]
            for c in car_list:
                #remove r is done to try diff ways
                if(c.is_available(t)):
                    available_cars.append(c)
                    #if car at ij ,t: time_to_make_itAND_bonus(car,t)=[_,_]
                    #time_to_make_itAND_bonus[0]=can get to DEADLINE and have this time to spare (int)
                    #time_to_make_itAND_bonus[1]=can get to BONUS and have this time to spare (int)
                    time_to_make_itAND_bonus_list=r.time_to_make_itAND_bonus(c,t)
                    spare_toDEADLINE = int(time_to_make_itAND_bonus_list[0])
                    spare_toBONUS = int(time_to_make_itAND_bonus_list[1])
                    #if time_to_make_itAND_bonus[0]<0 car cant do it(check others) !!! if no other can, isDone=True

                    #if time_to_make_itAND_bonus[0]=0 last chance for this car just to make it
                    #-if time_to_make_itAND_bonus[1]=0 last chance for this car to BONUS
                    #-if time_to_make_itAND_bonus[1]>0 car has time to spare to BONUS
                    #-if time_to_make_itAND_bonus[1]<0 car has MISSED BONUS
                    #if time_to_make_itAND_bonus[0]>0 car has time to spare just to make it
                    #-if time_to_make_itAND_bonus[1]=0 last chance for this car to BONUS
                    #-if time_to_make_itAND_bonus[1]>0 car has time to spare to BONUS
                    #-if time_to_make_itAND_bonus[1]<0 car has MISSED BONUS

                    if(spare_toDEADLINE<0):
                        print "car index " + str(car_list.index(c)) + " was unable to pick ride " + str(ride_list.index(r))
                    elif(spare_toDEADLINE==0):
                        #change later, but so far it will pick the car that has the last chance to get it
                        do(r,c,t)
                        #bonus not calculated
                    elif(spare_toDEADLINE>0):
                        if(spare_toBONUS<0):
                            #missed bonus so maybe dont
                            do(r,c,t)
                        elif(spare_toBONUS==0):
                            #change later, but defo do it now
                            do(r,c,t)
                        elif(spare_toBONUS>0):
                            #has time to get bonus so maybe prefer above
                            do(r,c,t)
            if (len(available_cars)==0):
                print "no car available for ride " + str(ride_list.index(r)) + " at time " + str(t)
            else:
                c=pick_from_available_cars(r, available_cars, t)
                do(r,c,t)
                r.is_Done=True
    t+=1
outputfilename = filename .rstrip('in')
outputfilename += "out"
o = open(outputfilename, "w")
parser.save(o, car_list, ride_list)
o.close()
