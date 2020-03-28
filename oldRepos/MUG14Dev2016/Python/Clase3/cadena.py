from abc import ABCMeta, abstractmethod
import sys

class ChainBase:
    __metaclass__ = ABCMeta

    _next = None

    def set_next(self, next_block):
        self._next = next_block

    def move_on(self, data):
        if self._next is not None:
            self._next.process(data)

    @abstractmethod
    def process(self, data):
        pass

class ByShort(ChainBase):
    def process(self, data):
        if len(data) < 4:
            raise Exception('El password es muy corto')
        self.move_on(data)

class ByLong(ChainBase):
    def process(self, data):
        if len(data) > 10:
            raise Exception('El password es muy largo')
        self.move_on(data)

def main(password):
    chain = ByShort()
    chain.set_next(ByLong())
    chain.process(password)
    print 'OK'


if __name__ == '__main__':
    parametro = sys.argv[1]
    main(parametro)
