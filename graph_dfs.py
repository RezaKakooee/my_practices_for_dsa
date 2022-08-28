# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:37:47 2022

@author: Reza Kakooee
"""

import random

from graph import Graph



#%%
class GraphDFS:
    def __init__(self, graph):
        self.graph = graph

    def _dfs(self, visited, node):
        visited.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs(visited, neighbor) # the next node is the neighbor

    def traverse(self, start_node=None):
        if start_node is None:
            start_node = random.choices(list(self.graph.keys()), k=1)[0]
        visited = []
        self._dfs(visited, start_node)
        return visited



#%%
if __name__ == '__main__':
        
    g = Graph()
      
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('a', 'd')
    g.add_edge('b', 'e')
    g.add_edge('c', 'f')
    g.add_edge('c', 'g')
    g.add_edge('d', 'h')
    g.add_edge('f', 'j')
    g.add_edge('e', 'i')
    g.add_edge('f', 'a')
    
    
    dfs = GraphDFS(g.graph)
    visited = dfs.traverse('d')
    print(f"Traverse the graph from start node of '{visited[0]}':")
    print(visited)

    
    import networkx as nx
    g = nx.DiGraph(g.graph)
    nx.draw_networkx(g)
    

