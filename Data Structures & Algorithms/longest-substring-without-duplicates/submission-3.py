class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        right = 0
        longest = 0
        while (right < len(s)):
            if s[right] in seen:
                longest = max(len(seen), longest)
                while s[right] in seen:
                    del seen[s[left]]
                    left += 1
            seen[s[right]] = True
            right += 1
            longest = max(len(seen), longest)
        return longest

                
        