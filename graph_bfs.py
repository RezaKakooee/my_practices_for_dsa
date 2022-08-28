# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:35:27 2022

@author: Reza Kakooee
"""

import random

from graph import Graph



#%%
class GraphBFS:
    def __init__(self, graph):
        self.graph = graph
        self.queue = []
        
        
    def _bfs(self, visited, node):
        if node not in visited:
            visited.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                self.queue.append(neighbor)
        
        if self.queue:
            n = self.queue.pop()
            self._bfs(visited, n) # the next node is being popped from the queue
        
        
    def traverse(self, start_node=None):
        if start_node is None:
            start_node = random.choices(list(self.graph.keys()), k=1)[0]
        visited = []
        self._bfs(visited, start_node) 
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
    g.add_edge('e', 'i')
    g.add_edge('f', 'j')
    
    from pprint import pprint
    print("Graph:")
    pprint(g.graph)
    
    bfs = GraphBFS(g.graph)
    visited = bfs.traverse()
    print(f"Traverse the graph from start node of '{visited[0]}':")
    print(visited)

    
    import networkx as nx
    g = nx.DiGraph(g.graph)
    nx.draw_networkx(g)
    