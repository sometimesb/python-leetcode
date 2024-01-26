class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sentence = (s.split())
        print(sentence,sentence[-1])
        return len(sentence[-1])
