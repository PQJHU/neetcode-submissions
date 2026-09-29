class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


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
            # else c_i < c_j:
            else:
                k_min = get_kth_min(l1[i + 1 :], l2[:], k - i - 1)
            # else:
            #     k_min = get_kth_min(l1[i + 1 :], l2[j + 1 :], k - i - j - 2)

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
