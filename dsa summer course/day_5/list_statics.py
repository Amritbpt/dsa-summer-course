nums = [3,7,1,9,4,6,2,8]
min = nums[0]
max = nums[0]
sum = 0
len = 0
for n in nums:
    if n > max:
        max = n

    if n < min:
        min = n

    sum += n
    len += 1

print(f"list : {nums}, minimum : {min}, maximum : {max}, sum : {sum}, average : {sum//len}")
nums.sort()
print(f"sorted list : {nums}")
nums.sort(reverse=True)
print(f"revese sorted list : {nums}")
print(f"splited list : {nums[-3:]}")