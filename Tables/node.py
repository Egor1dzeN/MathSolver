class Node:
    def __init__(self, key=None, value=None):
        self.__key = key
        self.__value = value
        self.__next = None

    def __str__(self):
        res = f'{self.key}, {self.value} - '
        return res

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        self.__next = next_

    def hasNext(self):
        return self.next is not None
