nums = [1,1,5,6,4,6,5,7,7,8,3]
m=0
for n in range(len(nums)-1):
    m=n+1
    while m<len(nums):
        if nums[n]==nums[m]:
            del nums[m]
            m=m
        else:
            m=m+1


print(nums)
