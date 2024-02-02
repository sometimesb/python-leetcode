import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        reversed_s = cleaned_s[::-1].lower()
        return cleaned_s == reversed_s
