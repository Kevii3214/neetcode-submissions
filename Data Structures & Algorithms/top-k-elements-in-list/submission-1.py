class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter[num] = 1
        tupleTopK = [(0,0)] * k
        for key in counter:
            if counter[key] > tupleTopK[0][0]:
                tupleTopK[0] = (counter[key], key)
                tupleTopK.sort()
        topK = []
        for value in tupleTopK:
            topK.append(value[1])
        return topK
