# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:26:20 2016

@author: yagnesh
"""
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedvertex = {}
        
    def addNeighbor(self, neighbor, weight = 0):
        self.connectedvertex[neighbor] = weight
        
    def getConnections(self):
        return self.connectedvertex.keys()
    
    def getWeight(self, neighbor):
        return self.connectedvertex[neighbor]
        
class Graph:
    def __init__(self):
        #Dictionar to store the vertices 
        self.vertexlist = {}
        self.numVertex = 0

    def addVertex(self, key):
        self.numVertex = self.numVertex + 1
        newVertex = Vertex(key)
        self.vertexlist[key] = newVertex
        return newVertex
        
    def addEdge(self, fromVer, toVer, weight = 0):
        if fromVer not in self.vertexlist:
            newVer = self.addVertex(fromVer)
        if toVer not in self.vertexlist:
            newVer = self.addVertex(toVer)
        self.vertexlist[fromVer].addNeighbor(self.vertexlist[toVer], weight)
        