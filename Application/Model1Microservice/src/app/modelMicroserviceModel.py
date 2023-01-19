#!/usr/bin/env python
# encoding: utf-8


from inspect import _Object
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

class modelMicroserviceModel(_Object):

    latencyList1=[]
    latencyList2=[]
    latencyList3=[]
    """cpu=0
    numNode=0
    ram=0"""

    def __init__(self, latencyList1, latencyList2, latencyList3):
        self.latencyList1=latencyList1
        self.latencyList2=latencyList2
        self.latencyList3=latencyList3

    def getLatencyList1():
        return self.latencyList1

    def setLatencyList1(latenceList1):
        self.latencyList1=latencyList1

    def getLatencyList2():
        return self.latencyList2

    def setLatencyList2(latenceList2):
        self.latencyList2=latencyList2

    def getLatencyList3():
        return self.latencyList3

    def setLatencyList3(latenceList3):
        self.latencyList3=latencyList3

    """
    def getCPU():
        return self.cpu

    def setCPU(cpu1):
        self.cpu=cpu1

    def getNumNode():
        return self.numNode

    def setNumNode(numNode1):
        self.numNode=numNode1

    def getRAM():
        return self.ram

    def setRAM(ram1):
        self.ram=ram1
    """