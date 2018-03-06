#!/bin/python2
from car import Car
from ride import Ride

def parse(f):
    lines = f.readlines()
    passed_list = lines[0].split(' ')
    ride_list=[]
    car_list=[]
    print "B is: " + str(passed_list[4])

    print "F is: " + str(passed_list[2])
    for i in range(0,int(passed_list[2])):
        i=0
        j=0
        listOfDoneRides=[]
        this_car=Car(listOfDoneRides,i,j)
        car_list.append(this_car)
    print "Check Fleet is of size: " + str(len(car_list)) + " initiated."

    print "R is: " + str(passed_list[3])

    for line in lines[1:] :
        ride_details=line.split(' ')
        starti= int(ride_details[0])
        startj= int(ride_details[1])
        endi= int(ride_details[2])
        endj= int(ride_details[3])
        earliest= int(ride_details[4])
        latest= int(ride_details[5])
        this_ride=Ride(starti, startj, endi, endj, earliest, latest)
        ride_list.append(this_ride)

    print "Check RideList is of size: " + str(len(ride_list)) + " initiated."

    passed_list.append(car_list)
    passed_list.append(ride_list)

    return passed_list

def save():
    return True
