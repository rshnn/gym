




compet = ["A B".split(), "B C".split(), "C A".split()]
results = [0, 0, 1]



def who_won(compet, results): 

    score_dict = dict() 

    for idx, game in enumerate(compet):    

        if results[idx] == 0: 
            # away team won, idx 1 
            winner = game[1] 

        else: 
            # home team won, idx 0 
            winner = game[0] 

        if winner not in score_dict.keys(): 
            score_dict[winner] = 3 
        else: 
            score_dict[winner] += 3 


    # loop through dict to find most points 
    most_points_so_far = [0, None]  #score, team name   

    for key, val in score_dict.items(): 

        if val > most_points_so_far[0]: 
            most_points_so_far = [val, key] 


    return most_points_so_far[1] 




print(who_won(compet, results))  