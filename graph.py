# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:13:28 2022

@author: Reza
"""

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph = {}
        
        
    def add_node(self, n):
        self.graph.update({n:[]})
    
    def add_edge(self, u, v):
        if u not in self.graph.keys():
            self.add_node(u)
        if v not in self.graph.keys():
            self.add_node(v)
            
        self.graph[u].append(v)
        
        if not self.directed:
            self.graph[v].append(u)