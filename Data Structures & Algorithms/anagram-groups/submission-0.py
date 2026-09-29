class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            temp = "".join(sorted(str))
            if temp in anagrams:
                anagrams[temp].append(str)
            else:
                anagrams[temp] = [str]
        return list(anagrams.values())
