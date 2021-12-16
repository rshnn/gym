


def binary_search(arr, target): 

  left = 0 
  right = len(arr)  

  while left <= right and left < len(arr) and right >= 0: 
    mid = left + ((right - left) // 2)  

    if arr[mid] == target: 
      return True 
    elif target < arr[mid]: 
      right = mid - 1
    else: 
      left = mid + 1 

  return False 

def FindIntersection(strArr):

  arr1, arr2 = strArr[0], strArr[1]  


arr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]


arr1 = arr[0]
arr1 = [int(char) for char in "".join(filter(str.isnumeric, arr1))]
print(arr1) 

# print(FindIntersection(arr))
