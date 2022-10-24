
class Predication(object):
    def predicate(self, n):
        pass


class Times(Predication):
    def __init__(self, base) -> None:
        self.base = base

    def predicate(self, n):
        return n % self.base == 0
    pass