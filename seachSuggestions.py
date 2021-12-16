


#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

class TrieNode(): 

    def __init__(self, val, full_word=False, children=None): 
        self.val = val 
        self.full_word = False 
        self.children = dict()    

    def __str__(self): 
        return str(self.val)  

    def __repr__(self): 
        return self.__str__() 


    def insert(self, s): 
        
        curr = self 

        for char in s: 

            if char in curr.children.keys():  
                curr = curr.children[char] 
                continue 

            tmp = TrieNode(char) 
            curr.children[char] = tmp 

            curr = tmp 

        curr.full_word = True 
        return 


    def search(self, s): 
        
        curr = self 

        for char in s: 

            if char in curr.children.keys():  
                 curr = curr.children[char] 
                 continue 

            else: 
                return False 

        return curr.full_word 


    def startsWith(self, s): 

        curr = self 

        for char in s: 
            if char in curr.children.keys():  
                 curr = curr.children[char] 
                 continue 
            else: 
                return None  
        
        # curr points to substring endpoint 

        stack = deque() 
        stack.append((curr, s))
        results = list() 

        while stack: 
            tmp, substring_so_far = stack.pop() 
            
            if tmp.full_word: 
                results.append(substring_so_far)
                if len(results) == 3: 
                    return results 

            for child in tmp.children.values(): 
                stack.append((child, substring_so_far + child.val))  

        return results 
#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#



def searchSuggestions(repository, customerQuery):
    # Write your code here
    if len(customerQuery) < 2: 
        return None 

    trie = TrieNode(-1) 
    for word in repository: 
        trie.insert(word)


    up_to_left = 2

    results = list() 

    while up_to_left <= len(customerQuery): 
        substring = customerQuery[:up_to_left]

        substring_list = trie.startsWith(substring)
        results.append(substring_list) 


        up_to_left += 1 
    

    return results 


if __name__ == '__main__':
    
    words = "mobile mouse moneypot monitor mousepad".split() 
    customerQuery = "mouse"

    r = searchSuggestions(words, customerQuery)

    print(r)