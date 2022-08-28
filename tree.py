# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:39:37 2022

@author: Reza Kakooee
"""


#%%
class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

    
    

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
    

