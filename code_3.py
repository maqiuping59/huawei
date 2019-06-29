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
        #print(item)

#pprint.pprint(Roads)


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
        #print(i)

#pprint.pprint(Cars)


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
        #print(item)

#pprint.pprint(Crosses)

dis = len(Crosses.keys())
map = np.zeros((dis,dis))
#print(map)
for i in Roads.values():
    start = int(i['from'])
    end = int(i['to'])
    #print(start,end)
    map[start-1,end-1] = 1
    # print(type(i['isDuplex']))
    if int(i['isDuplex']) == 1:
        map[end-1,start-1] = 1


#print(map)

state = np.zeros((1,dis))
for pre_car in Cars.keys():
    start_place = int(Cars[pre_car]['from'])
    end_place = int(Cars[pre_car]['to'])
    pre_state = state
    pre_state[0,start_place-1] = 1
    path = []
    gone_place = [start_place]
    #  用来存放已经走过的路径，如果发现有回头的情况，则舍弃
    last_state = []
    while True:

        if pre_state[0,end_place-1] !=0:
            break
        for i in range(dis):
            if pre_state[0, i] == 1:
                last_state.append(i+1)

        pre_state = np.dot(pre_state, map)
        print('上一状态')
        print(last_state)
        print('当前状态')
        print(pre_state)
        for i in range(dis):
            if pre_state[0, i] != 0:
                if i+1 in gone_place:
                    pre_state[0,i] = 0
                else:
                    gone_place.append(i + 1)
                    pre_state[0,i] = 1
                    for way in Roads.keys():
                        for j in last_state:
                            if int(Roads[way]['from']) == j and int(Roads[way]['to']) == i + 1:
                                path.append([way])

        last_state = []
    print('最终路径')
    print(path)
    print('经过的地方')
    print(gone_place)



# state = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
# print(state)
# print(np.dot(state,map))
# path = []
# new_state = np.dot(state, map)
# gone_place = [1]
# #  用来存放已经走过的路径，如果发现有回头的情况，则舍弃
# for i in range(dis):
#     if new_state[0,i] == 1:
#         if i+1 not in gone_place:
#             gone_place.append(i+1)
#             for way in Roads.keys():
#                 count = 0
#                 if int(Roads[way]['from']) == 1 and int(Roads[way]['to']) == i+1:
#                     path.append([way])
#
#
# print(path)
# print(gone_place)


