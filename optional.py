class Optional(object):
    def get(self, default=None):
        pass


class Just(Optional):
    def __init__(self, value):
        self.value = value

    def __nonzero__(self):
        return True

    def get(self, default=None):
        return self.value


class Empty(Optional):
    def __nonzero__(self):
        return False

    def get(self, default=None):
        return default


def optional_of(thing):
    return Just(thing)


def empty():
    return Empty()


def optional_of_nullable(thing):
    if thing is None:
        return empty()
    else:
        optional_of(thing)
