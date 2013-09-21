import numpy
from vector import Vector
from car import Car
from curve import CurveData


import random

class AI(object):

    def __init__(self,memSize=10,maxSpeed=10):
    	self.memorySize=10+random.randint(-2,2)
    	self.maxSpeed = 10.0+random.gauss(0,2)
        self.lastAcc=[];
        self.lastVel=[];
        self.lastStatus=[];
        for i in range(self.memorySize):
        	self.lastAcc.append(0)
        	self.lastVel.append(Vector(0,0))
        	self.lastStatus.append(1)

        

    def update(self, dt, car, curve,curve_p):
    	self.lastVel.pop(0)
        self.lastVel.append(car.velocity)

        acc=0
        """Calculate the amount of gas"""
        height = 0#car.position.y - curve.value_at_x(car.position.x)
        self.lastStatus.pop(0)
        if (height>0.1):
       		self.lastStatus.append(0)
       	else:
       		self.lastStatus.append(1)

       	meanSpeed=0
       	for vel in self.lastVel:
       		meanSpeed = meanSpeed + vel.length()
       	meanSpeed=meanSpeed/self.memorySize

       	if (meanSpeed<self.maxSpeed):
       		acc=1-meanSpeed/float(self.maxSpeed)

        # Always accelerate for now.
        self.lastAcc.pop(0)
        self.lastAcc.append(acc)
        return acc

    def mutate(self):
    	newMemsize=self.memorySize+random.randint(-2,2)
    	newMaxspeed=self.maxSpeed+random.gauss(0,2)
    	if (newMemsize<1):
    		newMemsize=1
    	if (newMaxspeed<1):
    		newMaxspeed=1
    	return AI(newMemsize,newMaxspeed)


ai= AI()



ai.update(1,Car(Vector(1,1)),1,1)


