nums = [1,2,3,4,5,6,7]
k = 3
for i in range(k):
        nums.insert(0, nums[-i-1])
res = nums[:(len(nums)-k)]
print(res)
for i in range(k):
    nums.pop()
print(nums)



