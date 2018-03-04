#!/bin/python2
import ride
import car
import sys
import parser

filename = sys.argv[1]
f = open(filename)
passed_list=[]
passed_list = parser.parse(f)
f.close()
I=int(passed_list[0])
J=int(passed_list[1])
F=int(passed_list[2])
R=int(passed_list[3])
B=int(passed_list[4])
T=int(passed_list[5])
car_list=passed_list[6]
ride_list=passed_list[7]
