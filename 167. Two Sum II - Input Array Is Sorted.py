def twoSum( numbers, target):
    numbers.sort()
    l = []
    for i,n in enumerate(numbers):
        for j, num in enumerate(numbers):
            test = n+ num
            if target == test:
                if i == j:
                    break
                else:
                    l.append(i+1)
                    l.append(j+1)

    l = l[0:2]
    l.sort()
    return l

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
               i+=1 
        
        return []

            
numbers = [2,7,11,15]
target = 9
twoSum(numbers, target)
print(twoSum(numbers, target))