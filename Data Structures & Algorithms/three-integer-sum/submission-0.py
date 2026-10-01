class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        i = 0    
        output = []
        for i in range (len(nums)):
            j = i+1
            k = len(numbers) -1
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            target = -numbers[i]
            while (j < k):
                if numbers[j] + numbers[k] > target:
                    k -= 1
                elif numbers[j] + numbers[k] < target:
                    j += 1
                else:
                    output.append([numbers[i], numbers[j], numbers[k]])
                    j += 1
                    k -= 1
                    while j < k and numbers[j] == numbers[j-1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k+1]:
                        k -= 1
        return output