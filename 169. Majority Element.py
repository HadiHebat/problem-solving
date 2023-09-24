nums = [3,3,4]
dicts={}
for i, n in enumerate(nums):
    dicts.update({n:nums.count(n)})
    
sorted_dict = sorted(dicts.items(), key=lambda x:x[1], reverse=True)

res = sorted_dict[0][0]
print(res)


"""      for i, n in enumerate(nums):
            dict.update({n:nums.count(n)})
        myKeys = list(dict.keys())
        myKeys.sort(reverse=True)
        sorted_dict = {i: dict[i] for i in myKeys}
            
        res = list(sorted_dict.keys())[0]
        return res """
nums = [2,2,1,1,1,1,2,2,3,5,6,7,8,3,3,3,3,3,3,3,3,3,3,3,3]       
nums.sort()
n= len(nums)
print(nums[n//2])
