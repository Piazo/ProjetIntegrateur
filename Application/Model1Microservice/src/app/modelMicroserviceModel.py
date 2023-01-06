#!/usr/bin/env python
# encoding: utf-8


from inspect import _Object
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

class modelMicroserviceModel(_Object):

    latencyList=[]
    """cpu=0
    numNode=0
    ram=0"""

    def __init__(self, latencyList1):
        self.latencyList=latencyList1

    def getLatencyList():
        return self.latencyList

    def setLatencyList(latenceList1):
        self.latencyList=latencyList1

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