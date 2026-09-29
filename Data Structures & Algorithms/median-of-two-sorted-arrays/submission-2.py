class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The brutal solution is sorted merging the two list and find the median value, O(n+m) complexity

        The median value is counting from smallest to largest the kth number,
        k = (m+n)//2 if m+n is odd, k = (m+n)//2 and the following number if m+n is even

        So, the question is equivalent to finding the kth smallest number in two lists

        If we compare the midval of two lists, mid1, mid2
        if mid1 > mid2
        it's safe to determine all the left half of the element in list2 are smaller than list1
        let's say i, j = len(list1,2)//2, we will then need to find the k-i-1 smallest number in list1[i+1:] and list2[:]
        within the comparison:
        if k == 1, return min(list1[0], list2[1])
        if list1 is empty: return list2[k-1]
        if list2 is empty: return list1[k-1]

        The question looks like a typical recursive problem
        there is a small issue when k < len(list1,2)//2
        We actually don't have to compare mid value, but we can just compare some indices that are surely smaller than k
        let compare_idx = min(k//2, len(list1,2))
        """

        def get_kth_min(l1: list[int], l2: list[int], k: int) -> int:

            if len(l1) == 0:
                return l2[k - 1]

            if len(l2) == 0:
                return l1[k - 1]

            if k == 1:
                return min(l1[0], l2[0])

            i, j = min(k // 2 - 1, len(l1) - 1), min(k // 2 - 1, len(l2) - 1)

            c_i, c_j = l1[i], l2[j]

            if c_i > c_j:
                k_min = get_kth_min(l1[:], l2[j + 1 :], k - j - 1)
            else:
                k_min = get_kth_min(l1[i + 1 :], l2[:], k - i - 1)

            return k_min

        total_len = len(nums1) + len(nums2)
        if total_len % 2 != 0:
            k = (total_len + 1) // 2
            median = get_kth_min(nums1, nums2, k)
        else:
            k1 = get_kth_min(nums1, nums2, total_len // 2)
            k2 = get_kth_min(nums1, nums2, total_len // 2 + 1)
            median = (k1 + k2) / 2
        return median
