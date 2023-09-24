s = "A man, a plan, a canal: Panama"
new_str = ''.join(char for char in s if char.isalnum())
print(new_str.lower()== new_str.lower()[::-1])
print(new_str.lower())    
print(new_str.lower()[::-1])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = ''.join(char for char in s if char.isalnum())
        if new_str.lower()== new_str.lower()[::-1]:
            return True
        else:
            return False 
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)



        return x == x[::-1]
