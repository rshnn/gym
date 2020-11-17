"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 
"""




class Transaction(): 

    def __init__(self, buy, sell, profit, next=None): 
        self.buy = buy 
        self.sell = sell 
        self.profit = profit 
        self.next = next 


    def __str__(self): 
        return "({}, {}, {})".format(self.buy, self.sell, self.profit)


    def __repr__(self): 
        return str(self)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        matrix = create_matrix(prices) 

        print_matrix(matrix)
        print('\n\n\n')

        build_possible_transaction_paths(matrix, prices) 

        # curr_day = 0 
        # while curr_day < len(prices): 

        #     trans_to_consider = matrix[curr_day][curr_day+1:]
        #     print(trans_to_consider)

        #     curr_day += 1


        return 







def build_possible_transaction_paths(matrix, prices): 


    resulting_cost_list = []

    for i, day in enumerate(matrix): 

        if i == 0: 
            continue 

        for transaction in day: 
            print(transaction)
            
            break 

        break 









def create_matrix(prices): 
    
    matrix = list() 
    l = len(prices)

    for i in range(l):

        matrix.append(list())
        curr = matrix[i]

        for j in range(l): 

            if j < i:
                continue  

            val = prices[j] - prices[i]

            if val <= 0:
                continue  

            t = Transaction(i, j, val)
            matrix[i].append(t)

    return matrix


        

def print_matrix(matrix): 
    for item in matrix:
        print(item)



if __name__ == "__main__": 

    soln = Solution()

    prices = [7,1,5,3,6,4]
    print(soln.maxProfit(prices))

