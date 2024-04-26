class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # set1 = set(nums1)
        # set2 = set(nums2)

        # set1Diff = set1.difference(set2)
        # set2Diff = set2.difference(set1)

        # return [list(set1Diff), list(set2Diff)]
        
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
