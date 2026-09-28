class TimeMap:

    """
    The challenging part of this question is getting the state of an object with given timestamp, while the timestamp
    is not necessary existing and should be referring to the previous existing timestamp
    A naive way is having a nested dict, {name: {ts: state}}, and looping over the ts one by one

    A simpler way is using two lists in a dict: {name: [[ts1,ts2,...], [s1, s2, ...]]}
    [1,3, 100]
    ["h", "s", "h"]
    50 = ?
    The equivalent question is finding the max number that is smaller than the target, a binary search since
    the assumption is that the timestamp is strictly increasing
    """

    def __init__(self):
        self.records: dict[str, list[list]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records.setdefault(key, [[], []])[0].append(timestamp)
        self.records.setdefault(key, [[], []])[1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""

        _ts = self.records[key][0]

        if timestamp < _ts[0]:
            return ""

        left, right = 0, len(_ts) - 1
        while left < right:
            mid = (left + right + 1) // 2  # right biased
            l_val, mid_val, r_val = _ts[left], _ts[mid], _ts[right]
            if mid_val <= timestamp:
                left = mid
            else:
                right = mid - 1
        target_idx = right
        return self.records[key][1][target_idx]
