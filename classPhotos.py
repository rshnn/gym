


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    
    redShirtHeights.sort() 
    blueShirtHeights.sort() 

    reds = redShirtHeights
    blue = blueShirtHeights 

    reds_top = None 


    for idx in range(len(reds)): 

        if reds[idx] == blue[idx]: 
            return False  

        if reds[idx] > blue[idx]: 
            # red at idx is higher 

            if reds_top is None: 
                reds_top = True 
            elif reds_top is False: 
                return False 
        else: 
            # blue at idx is highe r
            if reds_top is None: 
                reds_top = False 
            elif reds_top is True: 
                return False 

    return True 




if __name__ == '__main__':

    redShirtHeights = [1, 1]
    blueShirtHeights = [1, 1]
    expected = True
    actual = classPhotos(redShirtHeights, blueShirtHeights)

    print(actual) 