from pair import Pair
from Tables.node import Node


def hash(index) -> int:
    res = 0
    for item in str(index):
        res += ord(item)
    # print(index, res)
    return res % 100


class HashMap:
    def __init__(self, map_={}):
        self.__hashlist = []
        for key, value in map_.items():
            # print(key, hash(key))
            if self.contains(hash(key)):
                for pair in self.hashlist:
                    if pair.first == hash(key):
                        node = pair.second
                        while node.hasNext():
                            node = node.next
                        node.next = Node(key, value)
            else:
                root = Node()
                root.next = Node(key, value)
                # print(root.next)
                self.hashlist.append(Pair(hash(key), root))

    @property
    def hashlist(self):
        return self.__hashlist

    def contains(self, index):
        # print(index)
        for pair in self.hashlist:
            if pair.first == index:
                return True
        return False

    def get(self, key, default=None):
        if self.contains(hash(key)):
            for pair in self.hashlist:
                if pair.first == hash(key):
                    node = pair.second
                    node = node.next
                    if node.key == key:
                        return node.key
                    while node.hasNext():
                        if node.key == key:
                            return node.key
                    return default
        return default

    def put(self, key, value):
        # print(self.contains(hash(key)))

        if self.contains(hash(key)):
            for pair in self.hashlist:
                if pair.first == hash(key):
                    node = pair.second
                    node = node.next
                    if node.key == key:
                        node.value = value
                        return
                    while node.hasNext():
                        node = node.next
                        if node.key == key:
                            node.key = value
                            return
                    node.next = Node(key, value)
        else:
            root = Node()
            root.next = Node(key, value)
            # print(root.next)
            self.hashlist.append(Pair(hash(key), root))

    def __str__(self):
        res = 'Hash  |  Linked list\n'

        for pair in self.hashlist:
            res += str(pair.first) + ' -- '
            root = pair.second
            while root.hasNext():
                res += f'[{root.key}, {root.value}] -> '
                root = root.next
            res += f'[{root.key}, {root.value}]'
            res += '\n'
        return res
