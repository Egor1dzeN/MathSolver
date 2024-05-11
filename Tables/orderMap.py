from noOrderMap import noOrderMap
import bisect
from pair import Pair


class orderMap(noOrderMap):
    def __init__(self, map_=None):
        # print('Test')
        if map_ is None:
            map_ = {}
        map_ = dict(sorted(map_.items()))
        super().__init__(map_)

    def put(self, index, value=0):
        # пользуемся легальными читами по вставке элемента в отсортированный список (бинарная вставка)
        bisect.insort(self.no_order_map, Pair(index, value), key=lambda x: x.first)
        # super().put(index, value)

    def get(self, index, default=-1):
        low = 0
        arr = self.no_order_map
        high = len(arr) - 1
        mid = len(arr) // 2

        while arr[mid].first != index and low <= high:
            if index > arr[mid].first:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            return default
        else:
            return arr[mid]
