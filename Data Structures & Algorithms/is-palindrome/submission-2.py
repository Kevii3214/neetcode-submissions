class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = []
        for char in list(s):
            if (char != " " and char != "!" and char != "?" and char != "." and char != "," and char != "'" and char != '"' and char != ":" and char != ";"):
                newString.append(char)
        newString = "".join(newString).lower()
        for i in range(len(newString)//2):
            if newString[i] != newString[len(newString)-i-1]:
                return False
        return True