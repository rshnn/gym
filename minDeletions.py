"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

"""

from collections import Counter

def minDeletions(s): 
    table = Counter(s) 

    ftable = dict() 
    cost = 0 

    for key, val in table.items(): 

        cost += add_to_freq_table(val, ftable)

    return cost


def add_to_freq_table(val, ftable): 

    cost = 0 
    done = False 

    while not done: 
        if val not in ftable.keys(): 
            ftable[val] = 1 
            done = True 

        else: 
            cost += 1 
            val -= 1 

        if val == 0: 
            done = True 

    return cost 


if __name__ == "__main__":
    s = "bbcebab"
    print(minDeletions(s))