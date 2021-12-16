#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY codeList
#  2. STRING_ARRAY shoppingCart
#


def foo(codeList, shoppingCart):
    # Write your code here

    idx_cart = 0 
    idx_code_block = 0  
    
    while idx_cart < len(shoppingCart): 
        
        first_in_curr_codeblock = codeList[idx_code_block][0]
        if shoppingCart[idx_cart] == first_in_curr_codeblock or first_in_curr_codeblock == 'anything': 
            
            tmp_cart_idx = idx_cart  
            
            # check if code block is satisfied 
            for idx, fruit in enumerate(codeList[idx_code_block]): 

                if shoppingCart[tmp_cart_idx] == fruit or fruit == 'anything':   # handle anything case later                       
                    tmp_cart_idx += 1 

                else:    
                    idx_cart += 1
                    break 
                
                if idx == len(codeList[idx_code_block]) - 1: 
                    idx_code_block += 1
                    idx_cart = tmp_cart_idx  
        
        else: 
            idx_cart += 1 
    
    return idx_code_block == len(codeList) 


    
    
if __name__ == '__main__':


    codeList = [["orange"], ["apple", "anything"], "banana anything apple".split(), ["banana"]]
    codeList = [["orange anything"], ["apple apple"]]
    cart = "orange apple apple banana orange apple banana".split() 

    r = foo(codeList, cart) 

    print(r) 