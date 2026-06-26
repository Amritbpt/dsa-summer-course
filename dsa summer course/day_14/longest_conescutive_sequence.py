# this solution is usint sorted techinque which gives us the complexity of O(n logn)

def longest_consecutive(nums):
    if not nums:
         return 0
    
    nums.sort()
    length=1
    best=1
    
    for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                length+=1
            elif nums[i]==nums[i-1]:
                 continue
            else:
                 length=1
            
            best=max(length,best)

    return best

print(longest_consecutive([100,4,200,1,3,2,201,202]))

# now this solution is using hashmap technique with complexity of O(n)

def longest_sequence(nums):
    if not nums:
        return 0
     
    num_set=set(nums)
    best=0
    for num in num_set:
        if num-1 not in num_set:
            curr=num
            length=1
            while curr+1 in num_set:
                length+=1
                curr+=1
            best=max(best,length)


    return best

print(longest_sequence([100,4,200,1,3,2,201,202]))
            
