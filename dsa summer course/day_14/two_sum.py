# in this problem an array(nums) and a target is given such that nums[i]+nums[j]==target where i and j are the indices of values in nums

# this whole code is the execution of the problem discussed above
def two_sum(nums,target):

# the best time complexity for this solution id O(n) which is achieved by using hashmap technique

    seen={}
    for index,value in enumerate(nums):
        comp=target-value
        if comp in seen:
            return [seen[comp],index]
        seen[value]=index
    return "nothing found"

print(two_sum([1,2,7,5,6],9))