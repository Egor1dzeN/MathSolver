from pair import Pair


class noOrderMap:
    def __init__(self, map_=None):
        if map_ is None:
            map_ = {}
        self.__no_order_map = []
        for key, value in map_.items():
            # print(key, value)
            self.__no_order_map.append(Pair(key, value))

    @property
    def no_order_map(self):
        return self.__no_order_map

    # @no_order_map.setter
    def get(self, index, default=0):
        for pair in self.no_order_map:
            if pair.first == index:
                return pair.second
        return default

    def put(self, index, value=0):
        for pair in self.no_order_map:
            if pair.first == index:
                pair.second = value
                return
        self.no_order_map.append(Pair(index, value))

    def __str__(self):
        res = 'NoOrderMap['
        for pair in self.no_order_map:
            res += f'(key={pair.first}, second={pair.second}),'
        res = res[0:len(res) - 1]  # удаляем последнюю запятую
        res += ']'
        return res
