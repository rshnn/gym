




coins = [5, 7, 1, 1, 2, 3, 22]




def nonConstructibleChange(coins):
    # Write your code here.
    

    if not coins: 
        return 1 

    coins.sort() 

    change_possible_and_less = 0 
    for coin in coins: 

        if coin > change_possible_and_less + 1: 
            return change_possible_and_less + 1 

        else: 
            change_possible_and_less += coin 


    return change_possible_and_less + 1 



print(nonConstructibleChange(coins))



