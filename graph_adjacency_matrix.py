# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:52:40 2022

@author: Reza Kakooee
"""

class GraphAdjacencyMatrix:
    def __init__(self, n_nodes=4):
        self.n_nodes = n_nodes
        
        self.adj_vec = [0 for _ in range(self.n_nodes)]
        
        self.adj_mat = [self.adj_vec for _ in range(self.n_nodes)]
        
        self.adj_mat = []
        for _ in range(self.n_nodes):
            self.adj_mat.append([0 for _ in range(self.n_nodes)])
    
    def add_edge(self, u, v):
        self.adj_mat[u][v] = 1
        self.adj_mat[v][u] = 1
        
    
    def remove_edge(self, u, v):
        self.adj_mat[u][v] = 0
        self.adj_mat[v][u] = 0
        
    def print_adjacency_matrix(self):
        print("\nThe adjacency matrix is:")
        for av in self.adj_mat:
            print(av)
            
       
    def __len__(self):
        return self.n_nodes

#%%
if __name__ == '__main__':
    gam = GraphAdjacencyMatrix(n_nodes=4)
    gam.print_adjacency_matrix()
    gam.add_edge(1, 2)
    gam.add_edge(0, 1)
    gam.add_edge(0, 2)
    gam.print_adjacency_matrix()
    
    gam.remove_edge(0, 2)
    gam.print_adjacency_matrix()
        
    
        
