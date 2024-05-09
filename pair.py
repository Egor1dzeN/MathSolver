class Pair:
    def __init__(self, first, second):
        self.__first = first
        self.__second = second

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, first):
        self.__first = first

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        self.__second = second

    def __str__(self) -> str:
        return f'Pair({self.first}, {self.second})'

    def __eq__(self, other):
        print('Eq pair')
        return self.__first == other.first and self.second == other.second
