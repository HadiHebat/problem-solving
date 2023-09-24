
def rotate(nums, k):

    for i in range(k):
        nums.insert(0, nums[-i-1])
    nums = nums[1:(len(nums)-k)]

    return nums
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))