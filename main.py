# Put your function here
def timesTable(nums):
    nums = nums + 1
    combinedArr = []
    
    for i in range(nums - 1):
        arr = []
        nums = nums - 1
        multiplier = 0
        for i in range(0, 5):
            multiplier +=1 
            arr.append(nums * (multiplier))
            #print(arr)
        combinedArr.append(arr)
        
      
    return(combinedArr)

# testing
nums = int(input())
print(timesTable(nums))
