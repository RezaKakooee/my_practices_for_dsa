# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:06:39 2022

@author: Reza Kakooee
"""

from tree import Node

from collections import defaultdict


#%%
class TreeBFS:
    def __init__(self, node):
        self.node = node
        self.queue = []
        
    def bfs(self, node, data, depth=0):
        if node is None:
            return data
        queue = [(depth, node)]
        data[0] = [node.val]
        while len(queue) > 0:
            depth, node = queue.pop()
            if node.left is not None:
                queue.append((depth+1, node.left))
                data[depth+1].append(node.left.val)
            if node.right is not None:
                queue.append((depth+1, node.right))
                data[depth+1].append(node.right.val)
        return data
    
    
    def rbfs(self, node, data, depth=0):
        if node is None:
            return data
        
        if 0 not in data.keys(): # only executes in the very begining
            data[0] = [node.val]
            
        if node.left is not None:
            data[depth+1].append(node.left.val)
            self.queue.append((depth+1, node.left))
        
        if node.right is not None:
            data[depth+1].append(node.right.val)
            self.queue.append((depth+1, node.right))
            
        if self.queue:
            depth, node = self.queue.pop()
            self.rbfs(node, data, depth)
            
        return data
    
    
    def traverse(self):
        data = defaultdict(list)
        self.bfs(self.node, data, depth=0)
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

    bfs = TreeBFS(node)
    data = bfs.traverse()
    print(data)

