nums = [2,5,8,9,1,3,4,7]
target = 9

for index , num in enumerate(nums):
    #print(index, num)
    for j in range(index+1, len(nums)):
        if nums[index] + nums[j] == target:
            print([index,j])