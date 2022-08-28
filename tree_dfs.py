# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:06:39 2022

@author: Reza Kakooee
"""

from tree import Node

from collections import defaultdict


#%%
class TreeDFS:
    def __init__(self, node):
        self.node = node
        
        
    def dfs(self, node, data, depth=0):
        if node is None:
            return data
        data[depth].append(node.val)
        self.dfs(node.left, data, depth+1)
        self.dfs(node.right, data, depth+1)
    
    
    def traverse(self):
        data = defaultdict(list)
        self.dfs(self.node, data, depth=0)
        return dict(data.items())



#%%
if __name__ == '__main__':
    node = Node(4)
    node.left = Node(7)
    node.left.left = Node(10)
    node.left.right = Node(2)
    node.left.right.right = Node(6)
    node.left.right.right.left = Node(2)
    node.right = Node(9)
    node.right.right = Node(6)
    
    
    dfs = TreeDFS(node)
    data = dfs.traverse()
    from pprint import pprint
    pprint(data)

