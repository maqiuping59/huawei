# -*- coding:utf-8 -*-
'''
    @authon 马秋平
    华为精英挑战赛
'''
import pprint
import numpy as np
road = open('Road.txt','r')
roads = road.readlines()
roads = roads[1:]
Roads = {}
for item in roads:
    if item != '\n':
        item = item.strip('\n')
        item = item.strip('(')
        item = item.strip(')')
        item = item.split(',')
        Road={}
        Road['length'] = item[1]
        Road['speed'] = item[2]
        Road['channel'] = item[3]
        Road['from'] = item[4]
        Road['to'] = item[5]
        Road['isDuplex'] = item[6]
        Roads[item[0]] = Road
        print(item)

pprint.pprint(Roads)


car = open('Car.txt','r')
cars = car.readlines()
cars = cars[1:]
Cars = {}
for i in cars:
    if i != '\n':
        i = i.strip('\n')
        i = i.strip('(')
        i = i.strip(')')
        i = i.split(',')
        Car={}
        Car['from'] = i[1]
        Car['to'] = i[2]
        Car['speed'] = i[3]
        Car['time'] = i[4]
        Cars[i[0]] = Car
        print(i)

pprint.pprint(Cars)


cross = open('Cross.txt','r')
crosses = cross.readlines()
crosses = crosses[1:]
Crosses = {}
for item in crosses:
    if item != '\n':
        item = item.strip('\n')
        item = item.strip('(')
        item = item.strip(')')
        item = item.split(',')
        Cross={}
        Cross['up'] = item[1]
        Cross['right'] = item[2]
        Cross['down'] = item[3]
        Cross['left'] = item[4]
        Crosses[item[0]] = Cross
        print(item)

pprint.pprint(Crosses)

dis = len(Crosses.keys())
map = np.zeros((dis,dis))
print(map)
for i in Roads.values():
    start = int(i['from'])
    end = int(i['to'])
    print(start,end)
    map[start-1,end-1] = 1
    # print(type(i['isDuplex']))
    if int(i['isDuplex']) == 1:
        map[end-1,start-1] = 1


print(map)

state = np.zeros((1,dis))
for pre_car in Cars.keys():
    start_place = int(Cars[pre_car]['from'])
    end_place = Cars[pre_car]['to']
    pre_state = state
    pre_state[0,start_place-1] = 1
    print(pre_state)


