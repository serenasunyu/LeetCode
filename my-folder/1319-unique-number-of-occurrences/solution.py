class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numFreq = {}

        for num in arr:
            if num in numFreq.keys():
                numFreq[num] += 1
            else:
                numFreq[num] = 1

        UniqueOcc = set(numFreq.values())
        
        return len(numFreq) == len(UniqueOcc)



