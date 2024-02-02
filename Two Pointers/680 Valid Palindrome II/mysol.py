import re

class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        reversed_s = cleaned_s[::-1].lower()
        
        for i in range(len(reversed_s)):
            iteration = cleaned_s[:i] + cleaned_s[i+1:]
            reversed_iteration = iteration[::-1]
            print(iteration,reversed_iteration)
            
            if iteration == reversed_iteration:
                return True
                
        return False
