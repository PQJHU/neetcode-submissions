class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combines = []
        candidates.sort()

        def path_search(target: int, path: list[int], search_start: int):
            if target == 0:
                # _path_sorted = sorted(path[:])
                # if _path_sorted not in combines:
                combines.append(path.copy())
                return
            elif target < 0:
                return
            else:
                for i in range(search_start, len(candidates)):
                    if i > search_start and candidates[i] == candidates[i-1]:
                        continue
                    path.append(candidates[i])
                    path_search(target - candidates[i], path, i + 1)
                    path.pop()

        path_search(target, [], 0)
        return combines
