class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Index of the last element in nums1
        i = m - 1

        # Index of the last element in nums2
        j = n - 1

        # Index where the next element should be written in the merged array
        k = m + n - 1

        # Enter a while loop that continues until all elements from nums2 are merged into nums1
        while j >= 0:
            # Check if there are remaining elemets in both nums1 and nums2
            if i >= 0 and nums1[i] > nums2[j]:
                # If th elements in nums1 is greater that the element in nums2
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1







