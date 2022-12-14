#!/usr/bin/env python
# encoding: utf-8


from inspect import _Object
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

class modelMicroserviceModel(_Object):

    latenceList=[]
    cpu=0
    numNode=0
    ram=0

    def __init__(self, latenceList1, cpu1, numNode1, ram1):
        self.latenceList=latenceList1
        self.cpu=cpu1
        self.numNode=numNode1
        self.ram=ram1

    def getLatenceList():
        return self.latenceList

    def setLatenceList(latenceList1):
        self.latenceList=latenceList1

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