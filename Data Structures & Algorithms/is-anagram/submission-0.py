class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
            else:
                return False
        for v in letters.values():
            if v != 0:
                return False
        return True