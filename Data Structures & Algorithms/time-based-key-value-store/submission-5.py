from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.timemap[key]
        low = 0
        high = len(data) - 1
        result = ""

        while low <= high:
            mid = low + (high - low) // 2

            if data[mid][1] <= timestamp:
                result = data[mid][0]
                low = mid + 1
            else:
                high = mid - 1

        return result
            

