


def reverseString(s):
    
    left = 0
    right = len(s) - 1 

    while left <= right: 
        tmp = s[left] 
        s[left] = s[right]
        s[right] = tmp 

        left += 1
        right -= 1 




if __name__ == '__main__':
    s = []
    print(s)
    print(reverseString(s)) 
    print(s)