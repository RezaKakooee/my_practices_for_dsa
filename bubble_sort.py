# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 12:25:46 2022

@author: Reza
"""

#%%
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(arr)
        self.time_step = 0
    
    
    def sort(self):
        for i in range(self.arr_len):
            
            swapped = False
            for j in range(1, self.arr_len - i):
                if self.arr[j-1] > self.arr[j]:
                    self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j-1]
                    swapped = True
                    
            if not swapped:
                break
            
        self.time_step = i
        print(f"time: {self.time_step}")
        return self.arr
    
    

#%%
if __name__ == '__main__':
    arr = [3, 7, 2, 8, 9, 6]
    bs = BubbleSort(arr)
    sorted_arr = bs.sort()
    
    print(f"arr: \n{arr}")
    print(f"sorted arr: \n{sorted_arr}")
        
        
        
        
        